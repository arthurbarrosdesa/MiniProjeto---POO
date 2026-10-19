class Pessoa:
    """
    Classe "Pessoa" representa uma pessoa no sistema.

    Atributos:
    CPF;
    Nome.

    Métodos:
    __str__();
    __repr__().
    """

    def __init__(self, cpf: str, nome: str):
        self.__cpf = cpf
        self.__nome = nome

    def __str__(self) -> str:
        return f"Pessoa: {self.__nome} (CPF: {self.__cpf})"

    def __repr__(self) -> str:
        return f"Pessoa(cpf='{self.__cpf}', nome='{self.__nome}')"

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cpf(self) -> str:
        return self.__cpf


class Motorista(Pessoa):
    """
    Classe "Motorista" representa um motorista no sistema.

    Atributos:
    Categoria CNH;
    Tempo de experiência;
    Disponibilidade;
    Histórico de viagens.

    Métodos:
    registrar_viagem();
    atualizar_disponibilidade();
    __str__().
    """

    def __init__(self, cpf: str, nome: str, categoria_cnh: str, tempo_experiencia: int, disponibilidade: bool, historico_viagens: list | None = None):
        super().__init__(cpf, nome)
        self.__categoria_cnh = categoria_cnh
        self.__tempo_experiencia = tempo_experiencia
        self.__disponibilidade = disponibilidade
        self.__historico_viagens = (
            historico_viagens if historico_viagens is not None else []
        )

    @property
    def categoria_cnh(self) -> str:
        return self.__categoria_cnh

    @property
    def tempo_experiencia(self) -> int:
        return self.__tempo_experiencia

    @property
    def disponibilidade(self) -> bool:
        return self.__disponibilidade

    @property
    def historico_viagens(self) -> list:
        return self.__historico_viagens
    
    def to_dict(self) -> dict:
        return {
            "cpf": self.cpf,
            "nome": self.nome,
            "categoria_cnh": self.categoria_cnh,
            "tempo_experiencia": self.tempo_experiencia,
            "disponibilidade": self.disponibilidade,
            "historico_viagens": self.historico_viagens,
        }
    
    @classmethod
    def from_dict(cls, dados):
        return cls(
            cpf = dados["cpf"],
            nome = dados["nome"],
            categoria_cnh = dados["categoria_cnh"],
            tempo_experiencia = dados["tempo_experiencia"],
            disponibilidade = dados["disponibilidade"],
            historico_viagens = dados["historico_viagens"],
        )

    def registrar_viagem(self, viagem: str) -> None:
        """
        Adiciona uma viagem ao histórico do motorista.

        Parâmetros:
        viagem (str): Descrição da viagem.
        """
        self.__historico_viagens.append(viagem)

    def atualizar_disponibilidade(self, nova_disponibilidade: bool) -> None:
        """
        Atualiza a disponibilidade do motorista.

        Parâmetros:
        nova_disponibilidade (bool): Nova disponibilidade do motorista.
        """
        self.__disponibilidade = nova_disponibilidade

    def __str__(self) -> str:
        return f"Motorista: {self.nome} (CPF: {self.cpf}) - Categoria CNH: {self.categoria_cnh} - Experiência: {self.tempo_experiencia} anos - Disponível: {'Sim' if self.disponibilidade else 'Não'}"
