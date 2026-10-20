from src.veiculo import Veiculo
from src.pessoa import Motorista
from src.alocacao import Alocacao
from src.relatorio import Relatorio

veiculo1 = Veiculo(
    placa="POP6B16",
    marca="Chevrolet",
    modelo="Spin",
    ano=2022,
    quilometragem=15000,
    consumo_medio=12.5,
)

veiculo2 = Veiculo(
    placa="KTD8N25",
    marca="Fiat",
    modelo="Uno",
    ano=2024,
    quilometragem=10000,
    consumo_medio=15.2,
)

motorista1 = Motorista(
    cpf="12345678900",
    nome="Alexander Baltimore",
    categoria_cnh="B",
    tempo_experiencia=8,
    disponibilidade=True,
)

motorista2 = Motorista(
    cpf="98765432100",
    nome="Caio Landim",
    categoria_cnh="B",
    tempo_experiencia=4,
    disponibilidade=True,
)

alocacao = Alocacao(
    motorista=motorista1,
    veiculo=veiculo2,
    origem="Barbalha",
    destino="Recife",
    dist_percorrida=600,
)

motoristas = [motorista1, motorista2]
alocacoes = [alocacao]

relatorio = Relatorio(motoristas, alocacoes)
resultado = relatorio.total_viagens_motorista()

print(resultado)