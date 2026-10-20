from src.veiculo import Veiculo
from src.pessoa import Motorista
from src.alocacao import Alocacao
from src.persistencia_json import (
    salvar_dados,
    carregar_dados,
)
import tempfile
from pathlib import Path
import json


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

    salvar_dados([veiculo], caminho_veiculos)
    salvar_dados([motorista], caminho_motoristas)
    salvar_dados([alocacao], caminho_alocacoes)

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