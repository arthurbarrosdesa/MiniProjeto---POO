from src.veiculo import Veiculo
from src.pessoa import Motorista
from src.alocacao import Alocacao
from src.persistencia_json import (
    salvar_veiculos,
    carregar_veiculos,
    salvar_motoristas,
    carregar_motoristas,
    salvar_alocacoes,
    carregar_alocacoes,
)


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

salvar_veiculos([veiculo])
salvar_motoristas([motorista])

veiculos_carregados = carregar_veiculos()
motoristas_carregados = carregar_motoristas()

print("Veículos carregados:", len(veiculos_carregados))
print(veiculos_carregados[0])

print("Motoristas carregados:", len(motoristas_carregados))
print(motoristas_carregados[0])

alocacao = Alocacao(
    motorista=motorista,
    veiculo=veiculo,
    origem="Fortaleza",
    destino="Caucaia",
    dist_percorrida=20,
)

salvar_alocacoes([alocacao])

alocacoes_carregadas = carregar_alocacoes(
    motoristas_carregados,
    veiculos_carregados,
)

print("Alocações carregadas:", len(alocacoes_carregadas))
alocacao_carregada = alocacoes_carregadas[0]

print("Motorista:", alocacao_carregada.motorista.nome)
print("Veículo:", alocacao_carregada.veiculo.placa)
print("Origem:", alocacao_carregada.origem)
print("Destino:", alocacao_carregada.destino)
print("Distância:", alocacao_carregada.dist_percorrida)

print(
    "Motorista correto:",
    alocacao_carregada.motorista is motoristas_carregados[0],
)

print(
    "Veículo correto:",
    alocacao_carregada.veiculo is veiculos_carregados[0],
)