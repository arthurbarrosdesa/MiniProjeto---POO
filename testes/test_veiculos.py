import pytest

from Veiculo import Veiculo, StatusVeiculo, Carro, Moto, Caminhao


def test_criar_veiculo():


    veiculo = Veiculo(
        "ABC-1234",
       "Toyota",
       "Corolla",
       2022,
       10000,
       12.5
       )

    assert veiculo.placa == "ABC-1234"
    assert veiculo.marca == "Toyota"
    assert veiculo.modelo == "Corolla"
    assert veiculo.ano == 2022
    assert veiculo.quilometragem == 10000
    assert veiculo.consumo_medio == 12.5

def test_status_padrao_ativo():
    veiculo = Veiculo(
        "XYZ-5678",
        "Honda",
        "Civic",
        2023,
        5000,
        11.0
        )

    assert veiculo.status == StatusVeiculo.ATIVO

def test_alterar_status():
    veiculo = Veiculo(
        "DEF-9012",
        "Ford",
        "Fiesta",
        2020,
        30000,
        10.0
        )

    veiculo.alterar_status(StatusVeiculo.MANUTENCAO)

    assert veiculo.status == StatusVeiculo.MANUTENCAO

def test_atualizar_quilometragem():
    veiculo = Veiculo(
        "GHI-3456",
        "Volkswagen",
        "Gol",
        2021,
        20000,
        11.5
        )

    veiculo.atualizar_quilometragem(25000)

    assert veiculo.quilometragem == 25000

def test_registrar_evento():
    veiculo = Veiculo(
        "JKL-7890",
        "Chevrolet",
        "Onix",
        2024,
        10000,
        13.0
        )

    veiculo.registrar_evento("Revisão realizada")

    assert "Revisão realizada" in veiculo.historico_eventos

def test_veiculos_iguais_pela_placa():
    veiculo1 = Veiculo(
        "ABC-1234",
        "Toyota",
        "Corolla",
        2022,
        10000,
        12.5
        )

    veiculo2 = Veiculo(
        "ABC-1234",
        "Honda",
        "Civic",
        2023,
        5000,
        11.0
        )

    assert veiculo1 == veiculo2

def test_comparar_veiculos_por_quilometragem():
    veiculo1 = Veiculo(
        "AAA-1111",
        "Toyota",
        "Corolla",
        2022,
        10000,
        12.5
        )

    veiculo2 = Veiculo(
        "BBB-2222",
        "Honda",
        "Civic",
        2023,
        20000,
        11.0
        )

    assert veiculo1 < veiculo2

def test_iterar_historico_eventos():
    veiculo = Veiculo(
        "CCC-3333",
        "Fiat",
        "Argo",
        2023,
        15000,
        12.0
        )

    veiculo.registrar_evento("Troca de óleo")
    veiculo.registrar_evento("Revisão dos freios")

    eventos = list(veiculo)

    assert eventos == ["Troca de óleo", "Revisão dos freios"]

def test_nao_permitir_quilometragem_negativa():
    veiculo = Veiculo(
        "DDD-4444",
        "Ford",
        "Ka",
        2020,
        10000,
        13.0
        )

    with pytest.raises(ValueError):
       veiculo.atualizar_quilometragem(-500)

def test_str_veiculo():
    veiculo = Veiculo(
        "EEE-5555",
        "Toyota",
        "Corolla",
        2022,
        10000,
        12.5
        )

    resultado = str(veiculo)

    assert "Toyota" in resultado
    assert "Corolla" in resultado
    assert "EEE-5555" in resultado

def test_repr_veiculo():
    veiculo = Veiculo(
        "FFF-6666",
        "Honda",
        "Civic",
        2023,
        5000,
        11.0
        )

    resultado = repr(veiculo)

    assert "FFF-6666" in resultado
    assert "Honda" in resultado
    assert "Civic" in resultado

def test_carro_herda_de_veiculo():
    carro = Carro(
        "GGG-7777",
        "Toyota",
        "Corolla",
        2022,
        10000,
        12.5
        )

    assert isinstance(carro, Veiculo)

def test_moto_herda_de_veiculo():
    moto = Moto(
        "HHH-8888",
        "Honda",
        "CG 160",
        2024,
        5000,
        35.0
        )

    assert isinstance(moto, Veiculo)

def test_caminhao_herda_de_veiculo():
    caminhao = Caminhao(
        "III-9999",
        "Volvo",
        "FH 540",
        2023,
        50000,
        2.5
        )

    assert isinstance(caminhao, Veiculo)

def test_historico_eventos_inicialmente_vazio():
    veiculo = Veiculo(
        "JJJ-0000",
        "Fiat",
        "Uno",
        2020,
        30000,
        14.0
        )

    assert veiculo.historico_eventos == []