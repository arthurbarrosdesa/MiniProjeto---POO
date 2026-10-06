from pessoa import Pessoa, Motorista

def test_criar_pessoa():
    pessoa = Pessoa("12345678900", "Arthur")
    assert pessoa.cpf == "12345678900"
    assert pessoa.nome == "Arthur"

def test_motorista_herda_de_pessoa():
    motorista = Motorista("12345678900", "Arthur", "B", 3, True)
    assert isinstance(motorista, Pessoa)

def test_criar_motorista():
    motorista = Motorista("12345678900", "Arthur", "B", 3, True)
    assert motorista.categoria_cnh == "B"
    assert motorista.tempo_experiencia == 3
    assert motorista.disponibilidade is True

def test_atualizar_disponibilidade_motorista():
    motorista = Motorista("12345678900", "Arthur", "B", 3, True)
    motorista.atualizar_disponibilidade(False)
    assert motorista.disponibilidade is False

def test_registrar_viagem_motorista():
    motorista = Motorista("12345678900", "Arthur", "B", 3, True)
    motorista.registrar_viagem("Viagem 001")
    assert "Viagem 001" in motorista.historico_viagens

def test_str_motorista():
    motorista = Motorista("12345678900", "Arthur", "B", 3, True)
    assert str(motorista) == "Motorista: Arthur (CPF: 12345678900) - Categoria CNH: B - Experiência: 3 anos - Disponível: Sim"

def test_historico_viagens_inicialmente_vazio():
    motorista = Motorista("12345678900", "Arthur", "B", 3, True)
    assert motorista.historico_viagens == []