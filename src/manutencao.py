from datetime import datetime
from src.veiculo import Veiculo

class Manutencao:

    """
    Classe "Manutencao" armazena os dados nescessários para registrar uma manutenção.

    Atributos:
    Data;
    Tipo (preventiva ou corretiva);
    Custo;
    Descrição;
    Veiculo relacionado.
    """

    def __init__(self, data: datetime, tipo_manu: str, custo: float, descricao: str, veiculo: Veiculo, quilometragem: float = None):
        if not isinstance(data, datetime):
            raise TypeError("Data deve ser um objeto datetime.")
        if tipo_manu not in ("preventiva", "corretiva"):
            raise ValueError("Manutenção deve ser preventiva ou corretiva.")
        if custo < 0:
            raise ValueError("Custo não pode ser negativo.")
        if not isinstance(veiculo, Veiculo):
            raise TypeError("Veículo deve ser um objeto Veiculo.")
        self.__data = data
        self.__tipo_manu = tipo_manu
        self.__custo = custo
        self.__descricao = descricao
        self.__veiculo = veiculo
        self.__quilometragem = (
            veiculo.quilometragem if quilometragem is None else quilometragem
        )

    @property
    def data(self):
        return self.__data

    @property
    def tipo_manu(self):
        return self.__tipo_manu

    @property
    def custo(self):
        return self.__custo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def quilometragem(self):
        return self.__quilometragem

    def __str__(self):
        return (
            f"Manutenção {self.tipo_manu} - "
            f"Veículo: {self.veiculo.placa} - "
            f"Data: {self.data.strftime('%d/%m/%Y')} - "
            f"Custo: R${self.custo:.2f} - "
            f"Descrição: {self.descricao}"
        )

    def to_dict(self):
        return {
            "tipo": self.tipo_manu,
            "veiculo": self.veiculo.placa,
            "quilometragem": self.quilometragem,
            "data": self.data.isoformat(),
            "custo": self.custo,
            "descricao": self.descricao,
        }

    @classmethod
    def from_dict(cls, dados, veiculos):
        veiculo = next(
            veiculo for veiculo in veiculos
            if veiculo.placa == dados["veiculo"]
        )

        return cls(
            data = datetime.fromisoformat(dados["data"]),
            tipo_manu = dados["tipo"],
            custo = dados["custo"],
            descricao = dados["descricao"],
            veiculo = veiculo,
            quilometragem = dados.get("quilometragem", veiculo.quilometragem),
        )