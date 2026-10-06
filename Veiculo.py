class StatusVeiculo:

    """
    Classe "StatusVeiculo" armazena os status possíveis para veículos.

    Atributos:
    ATIVO;
    MANUTENCAO;
    INATIVO.

    Métodos:
    str(): str;
    repr(): str;
    eq(): bool;
    lt(): bool.
    """

    ATIVO = "ativo"
    MANUTENCAO = "manutenção"
    INATIVO = "inativo"


class Veiculo:

    """
    Classe "Veiculo" armazena informações gerais sobre veículos.

    Atributos:
    Placa;
    Marca;
    Modelo;
    Ano;
    Tipo (carro, moto, caminhão);
    Quilometragem;
    Consumo Médio (Km/L);
    Status (ativo, manutenção, inativo).

    Métodos:
    alterar_status(novo_status: StatusVeiculo): void;
    atualizar_quilometragem(): void;
    registrar_evento(): void;
    str(): str;
    repr(): str;
    eq(): bool;
    lt(): bool;
    iter(): Iterator.
    """

    def __init__(self, placa: str, marca: str, modelo: str, ano: int, tipo: str, quilometragem: float, consumo_medio: float, status: str):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__tipo = tipo
        self.__quilometragem = quilometragem
        self.__consumo_medio = consumo_medio
        self.__status = status

    @property
    def placa(self) -> str:
        return self.__placa

    @property
    def marca(self) -> str:
        return self.__marca

    @property
    def modelo(self) -> str:
        return self.__modelo

    @property
    def ano(self) -> int:
        return self.__ano

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def quilometragem(self) -> float:
        return self.__quilometragem

    @property
    def consumo_medio(self) -> float:
        return self.__consumo_medio

    @property
    def status(self) -> str:
        return self.__status

    def alterar_status(self, novo_status: StatusVeiculo) -> None:
        """
        Altera o status do veículo.

        Parâmetros:
        novo_status (str): Novo status do veículo.
        """
        self.__status = novo_status

    def atualizar_quilometragem(self, nova_quilometragem: float) -> None:
        """
        Atualiza a quilometragem do veículo.

        Parâmetros:
        nova_quilometragem (float): Nova quilometragem do veículo.
        """
        self.__quilometragem = nova_quilometragem

    def registrar_evento(self, evento: str) -> None:
        """
        Registra um evento relacionado ao veículo.

        Parâmetros:
        evento (str): Descrição do evento.
        """
        # Implementação para registrar o evento (pode ser armazenado em uma lista ou banco de dados)
        pass

    def __str__(self) -> str:
        return f"Veículo: {self.marca} {self.modelo} ({self.ano}) - Placa: {self.placa} - Tipo: {self.tipo} - Quilometragem: {self.quilometragem} km - Consumo Médio: {self.consumo_medio} km/L - Status: {self.status}"

    def __repr__(self) -> str:
        return f"Veiculo(placa='{self.placa}', marca='{self.marca}', modelo='{self.modelo}', ano={self.ano}, tipo='{self.tipo}', quilometragem={self.quilometragem}, consumo_medio={self.consumo_medio}, status='{self.status}')"

    def __eq__(self, other) -> bool:
        if isinstance(other, Veiculo):
            return self.placa == other.placa
        return False

    def __lt__(self, other) -> bool:
        if isinstance(other, Veiculo):
            return self.ano < other.ano
        return NotImplemented

    def __iter__(self):
        yield self.placa
        yield self.marca
        yield self.modelo
        yield self.ano
        yield self.tipo
        yield self.quilometragem
        yield self.consumo_medio
        yield self.status


class Carro(Veiculo):

    """
    Classe "Carro" armazena os dados específicos para carros.

    Atributos:


    Métodos:

    """
    pass


class Moto(Veiculo):

    """
    Classe "Moto" armazena os dados específicos para motos.

    Atributos:


    Métodos:

    """
    pass


class Caminhao(Veiculo):

    """
    Classe "Caminhao" armazena os dados específicos para caminhões.

    Atributos:


    Métodos:

  """
    pass


carro = Carro("ABC-1234", "Toyota", "Corolla", 2022, 10000, 12.5)

print(carro)
