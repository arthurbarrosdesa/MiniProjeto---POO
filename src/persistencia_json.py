import json
from pathlib import Path
from .veiculo import Veiculo
from .pessoa import Motorista
from .alocacao import Alocacao

PASTA_DADOS = Path(__file__).resolve().parent.parent / "data"

ARQUIVO_VEICULOS = PASTA_DADOS / "veiculos.json"
ARQUIVO_MOTORISTAS = PASTA_DADOS / "motoristas.json"
ARQUIVO_ALOCACOES = PASTA_DADOS / "alocacoes.json"


def salvar_dados(objetos, caminho):
    Path(caminho).parent.mkdir(parents=True, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump([objeto.to_dict() for objeto in objetos], arquivo, ensure_ascii=False, indent=4)

def salvar_veiculos(veiculos):
    salvar_dados(veiculos, ARQUIVO_VEICULOS)

def salvar_motoristas(motoristas):
    salvar_dados(motoristas, ARQUIVO_MOTORISTAS)

def salvar_alocacoes(alocacoes):
    salvar_dados(alocacoes, ARQUIVO_ALOCACOES)

def carregar_dados(classe, caminho):
    if not Path(caminho).exists():
        return []
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return [classe.from_dict(dado) for dado in dados]
    
def carregar_veiculos():
    return carregar_dados(Veiculo, ARQUIVO_VEICULOS)

def carregar_motoristas():
    return carregar_dados(Motorista, ARQUIVO_MOTORISTAS)

def carregar_alocacoes(motoristas, veiculos):
    if not Path(ARQUIVO_ALOCACOES).exists():
        return []
    with open(ARQUIVO_ALOCACOES, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return [Alocacao.from_dict(dado, motoristas, veiculos) for dado in dados]