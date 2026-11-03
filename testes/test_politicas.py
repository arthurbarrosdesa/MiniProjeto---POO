import pytest
from src.excecoes import PoliticaNaoAtendidaError
from src.pessoa import Motorista
from src.veiculo import Carro, StatusVeiculo
from src.politicas import Politicas
from src.excecoes import AlocacaoInvalidaError, AbastecimentoInvalidoError, ManutencaoInvalidaError
from datetime import datetime
from src.abastecimento import Abastecimento
from src.manutencao import Manutencao



def test_alocacao_com_motorista_indisponivel():
    motorista = Motorista("12345678900", "Arthur", "B", 3, False)

    veiculo = Carro(
        "JJJ-0000",
        "Fiat",
        "Uno",
        2020,
        14.0
    )

    politicas = Politicas()

    with pytest.raises(AlocacaoInvalidaError):
        politicas.verificar_alocacao(motorista, veiculo)


def test_alocacao_com_veiculo_inativo():
    motorista = Motorista("12345678900", "Arthur", "B", 3, True)

    veiculo = Carro(
        "JJJ-0000",
        "Fiat",
        "Uno",
        2020,
        14.0,
        status=StatusVeiculo.INATIVO
    )

    politicas = Politicas()

    with pytest.raises(AlocacaoInvalidaError):
        politicas.verificar_alocacao(motorista, veiculo)


def test_alocacao_com_cnh_incompativel():
    motorista = Motorista("12345678900", "Arthur", "A", 3, True)

    veiculo = Carro(
        "JJJ-0000",
        "Fiat",
        "Uno",
        2020,
        14.0
    )

    politicas = Politicas()

    with pytest.raises(PoliticaNaoAtendidaError):
        politicas.verificar_alocacao(motorista, veiculo)

def test_abastecimento_em_veiculo_diferente():
    veiculo1 = Carro("JJJ-0000", "Fiat", "Uno", 2020, 14.0)
    veiculo2 = Carro("ABC-1234", "Ford", "Ka", 2021, 12.0)

    abastecimento = Abastecimento(
        data=datetime(2026, 11, 3),
        tipo_comb="gasolina",
        litros=30.0,
        valor_pago=150.0,
        veiculo=veiculo1
    )

    with pytest.raises(AbastecimentoInvalidoError):
        veiculo2.registrar_abastecimento(abastecimento)

def test_manutencao_em_veiculo_diferente():
    veiculo1 = Carro("JJJ-0000", "Fiat", "Uno", 2020, 14.0)
    veiculo2 = Carro("ABC-1234", "Ford", "Ka", 2021, 12.0)

    manutencao = Manutencao(
        data=datetime(2026, 11, 3),
        tipo_manu="preventiva",
        custo=300.0,
        descricao="Troca de óleo",
        veiculo=veiculo1
    )

    with pytest.raises(ManutencaoInvalidaError):
        veiculo2.registrar_manutencao(manutencao)

def test_politica_cnh_nao_atendida():
    motorista = Motorista("12345678900", "Arthur", "A", 3, True)
    veiculo = Carro("JJJ-0000", "Fiat", "Uno", 2020, 14.0)

    politicas = Politicas()

    with pytest.raises(PoliticaNaoAtendidaError):
        politicas.verificar_alocacao(motorista, veiculo)