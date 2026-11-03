import json
from pathlib import Path
from .veiculo import Veiculo
from .pessoa import Motorista
from .alocacao import Alocacao
from .manutencao import Manutencao
from .abastecimento import Abastecimento
from .excecoes import RepositorioError

PASTA_DADOS = Path(__file__).resolve().parent.parent / "data"

ARQUIVO_VEICULOS = PASTA_DADOS / "veiculos.json"
ARQUIVO_MOTORISTAS = PASTA_DADOS / "motoristas.json"
ARQUIVO_ALOCACOES = PASTA_DADOS / "alocacoes.json"
ARQUIVO_MANUTENCOES = PASTA_DADOS / "manutencoes.json"
ARQUIVO_ABASTECIMENTOS = PASTA_DADOS / "abastecimentos.json"

class JsonRepository:
    def salvar(self, objetos, caminho):
        try:
            Path(caminho).parent.mkdir(parents=True, exist_ok=True)

            with open(caminho, "w", encoding="utf-8") as arquivo:
                json.dump(
                    [objeto.to_dict() for objeto in objetos],
                    arquivo,
                    ensure_ascii=False,
                    indent=4
                )

        except (OSError, TypeError, ValueError, AttributeError) as erro:
            raise RepositorioError(
                f"Não foi possível salvar os dados em {caminho}: {erro}"
            ) from erro
    
    def carregar(self, classe, caminho, *args):
        try:
            if not Path(caminho).exists():
                return []
            with open(caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            return [classe.from_dict(dado, *args) for dado in dados]

        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as erro:
            raise RepositorioError(
                f"Não foi possível carregar os dados de {caminho}: {erro}"
            ) from erro
    
repositorio = JsonRepository()


def salvar_veiculos(veiculos):
    repositorio.salvar(veiculos, ARQUIVO_VEICULOS)

def salvar_motoristas(motoristas):
    repositorio.salvar(motoristas, ARQUIVO_MOTORISTAS)

def salvar_alocacoes(alocacoes):
    repositorio.salvar(alocacoes, ARQUIVO_ALOCACOES)

def salvar_manutencoes(manutencoes):
    repositorio.salvar(manutencoes, ARQUIVO_MANUTENCOES)

def salvar_abastecimentos(abastecimentos):
    repositorio.salvar(abastecimentos, ARQUIVO_ABASTECIMENTOS)

def carregar_dados(classe, caminho):
    return repositorio.carregar(classe, caminho)

def carregar_veiculos():
    return carregar_dados(Veiculo, ARQUIVO_VEICULOS)

def carregar_motoristas():
    return carregar_dados(Motorista, ARQUIVO_MOTORISTAS)

def carregar_alocacoes(motoristas, veiculos):
    alocacoes = repositorio.carregar(
        Alocacao,
        ARQUIVO_ALOCACOES,
        motoristas,
        veiculos
    )

    for alocacao in alocacoes:
        alocacao.veiculo.registrar_evento(str(alocacao))

    return alocacoes

def carregar_manutencoes(veiculos):
    manutencoes = repositorio.carregar(
        Manutencao,
        ARQUIVO_MANUTENCOES,
        veiculos
    )

    for manutencao in manutencoes:
        manutencao.veiculo.registrar_evento(manutencao)

    return manutencoes

def carregar_abastecimentos(veiculos):
    abastecimentos = repositorio.carregar(
        Abastecimento,
        ARQUIVO_ABASTECIMENTOS,
        veiculos
    )

    for abastecimento in abastecimentos:
        abastecimento.veiculo.registrar_evento(abastecimento)

    return abastecimentos
