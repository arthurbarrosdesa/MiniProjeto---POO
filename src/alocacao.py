from .veiculo import Veiculo, StatusVeiculo
from .pessoa import Motorista

class Alocacao:

    """
    Classe "Alocacao" armazena os dados nescessários para registrar uma alocação.

    Atributos:
    Origem;
    Destino;
    Distância percorrida.

    Métodos:
    realizar_viagem( ).
    """

    def __init__ (self, motorista: Motorista, veiculo: Veiculo, origem: str, destino: str, dist_percorrida: float):
        self.__motorista = motorista
        self.__veiculo = veiculo
        self.__origem = origem
        self.__destino = destino
        if dist_percorrida < 0:
            raise ValueError("A distância percorrida não pode ser negativa.")
        self.__dist_percorrida = dist_percorrida
    
    @property
    def motorista(self) -> Motorista:
        return self.__motorista
    
    @property
    def veiculo(self) -> Veiculo:
        return self.__veiculo
    
    @property
    def origem(self) -> str:
        return self.__origem

    @property
    def destino(self) -> str:
        return self.__destino

    @property
    def dist_percorrida(self) -> float:
        return self.__dist_percorrida

    def to_dict(self):
        return {
            "cpf_motorista": self.motorista.cpf,
            "placa_veiculo": self.veiculo.placa,
            "origem": self.origem,
            "destino": self.destino,
            "dist_percorrida": self.dist_percorrida,
        }
    
    @classmethod
    def from_dict(cls, dados, motoristas, veiculos):
        motorista = next(
            motorista for motorista in motoristas
            if motorista.cpf == dados["cpf_motorista"]
        )
        veiculo = next(
            veiculo for veiculo in veiculos
            if veiculo.placa == dados["placa_veiculo"]
        )
        return cls(
            motorista = motorista,
            veiculo = veiculo,
            origem = dados["origem"],
            destino = dados["destino"],
            dist_percorrida = dados["dist_percorrida"],
        )

    def realizar_viagem(self):
        if not self.__motorista.disponibilidade:
            raise ValueError("Motorista indisponível")
        if self.__veiculo.status != StatusVeiculo.ATIVO:
            raise ValueError("Veículo inativo ou em manutenção.")
        self.__veiculo.atualizar_quilometragem(self.__dist_percorrida)
        self.__motorista.registrar_viagem(f"Viagem: {self.__origem} -> {self.__destino}; Distância percorrida: {self.__dist_percorrida}; Placa do veículo: {self.__veiculo.placa}.")
        

