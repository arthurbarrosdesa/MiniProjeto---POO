from src.veiculo import Carro, Moto, Caminhao, StatusVeiculo
from src.pessoa import Motorista

from src.persistencia_json import (
    salvar_veiculos,
    salvar_motoristas,
    carregar_veiculos,
    carregar_motoristas
)

def inicializar_dados():
    veiculos = carregar_veiculos()
    motoristas = carregar_motoristas()

    if veiculos or motoristas:
        return

    veiculos = [
        Carro("ABC1D23", "Toyota", "Corolla", 2022, 12.5, 35000),
        Carro("DEF4G56", "Chevrolet", "Onix", 2023, 13.0, 18000),

        Moto("GHI7J89", "Honda", "CG 160", 2022, 35.0, 12000),
        Moto("KLM1N23", "Yamaha", "Fazer 250", 2024, 30.0, 5000),

        Caminhao("OPQ4R56", "Volvo", "FH 460", 2021, 3.5, 85000),
        Caminhao("STU7V89", "Mercedes-Benz", "Actros", 2023, 3.8, 42000),
    ]
    motoristas = [
        Motorista("00000000001", "João Silva", "A", 5, True),
        Motorista("00000000002", "Maria Souza", "B", 8, True),
        Motorista("00000000003", "Pedro Santos", "C", 10, True),
        Motorista("00000000004", "Ana Oliveira", "AB", 3, True),
    ]
    salvar_veiculos(veiculos)
    salvar_motoristas(motoristas)