from datetime import datetime
from src.veiculo import Veiculo

class Abastecimento:

    """
    Classe "Abastecimento" armazena os dados nescessários para registrar um abastecimento.

    Atributos:
    Data;
    Tipo de combustível;
    Litros;
    Valor pago;
    Veículo relacionado;
    Quilometragem atual.

    Métodos:
    __str__
    calcular_cons_medio()
    """

    def __init__(self, data: datetime, tipo_comb: str, litros: float, valor_pago: float, veiculo: Veiculo, quilometragem: float):
        if not isinstance(data, datetime):
            raise TypeError("Data deve ser um objeto datetime.")
        if litros <= 0:
            raise ValueError("Deve ser abastecido mais de 0L.")
        if valor_pago < 0:
            raise ValueError("Valor pago não pode ser negativo.")
        if not isinstance(veiculo, Veiculo):
            raise TypeError("Veículo deve ser um objeto Veiculo.")
        if quilometragem < 0:
            raise ValueError("Quilometragem não pode ser negativa.")

        self.__data = data
        self.__tipo_comb = tipo_comb
        self.__litros = litros
        self.__valor_pago = valor_pago
        self.__veiculo = veiculo
        self.__quilometragem = quilometragem

    @property
    def data(self):
        return self.__data

    @property
    def tipo_comb(self):
        return self.__tipo_comb

    @property
    def litros(self):
        return self.__litros

    @property
    def valor_pago(self):
        return self.__valor_pago

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def quilometragem(self):
        return self.__quilometragem

    def __str__(self):
        return (
            f"Veículo: {self.veiculo.placa} - "
            f"Data: {self.data.strftime('%d/%m/%Y')} - "
            f"Tipo de combustível: {self.tipo_comb} - "
            f"Litros: {self.litros}L - "
            f"Valor pago: R${self.valor_pago}"
        )

    def to_dict(self):
        return {
            "veiculo": self.veiculo.placa,
            "data": self.data.isoformat(),
            "tipo_comb": self.tipo_comb,
            "litros": self.litros,
            "valor_pago": self.valor_pago,
            "quilometragem": self.quilometragem
        }

    @classmethod
    def from_dict(cls, dados, veiculos):
        veiculo = next(
            veiculo for veiculo in veiculos
            if veiculo.placa == dados["veiculo"]
        )

        return cls(
            data = datetime.fromisoformat(dados["data"]),
            tipo_comb = dados["tipo_comb"],
            litros = dados["litros"],
            valor_pago = dados["valor_pago"],
            veiculo = veiculo,
            quilometragem = dados["quilometragem"]
        )

    def calcular_cons_medio(self):
        abastecimentos = []

        for evento in self.veiculo.historico_eventos:
            if isinstance(evento, Abastecimento):
                abastecimentos.append(evento)

        abastecimentos = sorted(
            abastecimentos,
            key=lambda abastecimento: abastecimento.quilometragem,
            reverse=True
        )

        dist_total = abastecimentos[0].quilometragem - abastecimentos[-1].quilometragem if len(abastecimentos) >= 2 else 0
        litros_total = 0

        for i in range(len(abastecimentos) - 1):
            litros_total += abastecimentos[i].litros

        if dist_total == 0 or litros_total == 0:
            return self.veiculo.consumo_medio

        consumo = dist_total / litros_total
        return consumo
