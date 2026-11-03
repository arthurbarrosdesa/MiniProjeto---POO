from src.veiculo import Veiculo
from src.pessoa import Motorista
from src.alocacao import Alocacao
from src.persistencia_json import (
    carregar_dados,
    JsonRepository
)
import tempfile
from pathlib import Path
import json
import pytest
from src.excecoes import RepositorioError
repositorio = JsonRepository()

def test_carregar_json_invalido(tmp_path):
    arquivo = tmp_path / "dados_invalidos.json"
    arquivo.write_text("{ conteúdo inválido }", encoding="utf-8")

    with pytest.raises(RepositorioError):
        carregar_dados(Veiculo, arquivo)

def test_salvar_dados_com_objeto_invalido(tmp_path):
    arquivo = tmp_path / "dados.json"

    objeto = object()

    with pytest.raises(RepositorioError):
        repositorio.salvar([objeto], arquivo)


veiculo = Veiculo(
    placa="ABC1D23",
    marca="Toyota",
    modelo="Corolla",
    ano=2022,
    quilometragem=15000,
    consumo_medio=12.5,
)

motorista = Motorista(
    cpf="12345678900",
    nome="Motorista Teste",
    categoria_cnh="B",
    tempo_experiencia=5,
    disponibilidade=True,
)

alocacao = Alocacao(
    motorista=motorista,
    veiculo=veiculo,
    origem="Fortaleza",
    destino="Caucaia",
    dist_percorrida=20,
)

with tempfile.TemporaryDirectory() as pasta:
    caminho_veiculos = Path(pasta) / "veiculos.json"
    caminho_motoristas = Path(pasta) / "motoristas.json"
    caminho_alocacoes = Path(pasta) / "alocacoes.json"

    repositorio.salvar([veiculo], caminho_veiculos)
    repositorio.salvar([motorista], caminho_motoristas)
    repositorio.salvar([alocacao], caminho_alocacoes)

    veiculos_carregados = carregar_dados(Veiculo, caminho_veiculos)
    motoristas_carregados = carregar_dados(Motorista, caminho_motoristas)
    if not Path(caminho_alocacoes).exists():
        alocacoes_carregadas = []
    else:
        with open(caminho_alocacoes, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        alocacoes_carregadas = [Alocacao.from_dict(dado, motoristas_carregados, veiculos_carregados) for dado in dados]
    
    print("Veículos carregados:", len(veiculos_carregados))
    print("Motoristas carregados:", len(motoristas_carregados))
    print("Alocações carregadas:", len(alocacoes_carregadas))

    alocacao_carregada = alocacoes_carregadas[0]

    print(
        "Motorista correto:",
        alocacao_carregada.motorista is motoristas_carregados[0],
    )
    print(
        "Veículo correto:",
        alocacao_carregada.veiculo is veiculos_carregados[0],
    )