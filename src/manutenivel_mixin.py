from src.excecoes import ManutencaoInvalidaError

class ManutenivelMixin:

    """
    Mixin responsável pelas operações de manutenção dos veículos.
    """

    def registrar_manutencao(self, manutencao) -> None:
        if manutencao.veiculo is not self:
            raise ManutencaoInvalidaError("A manutenção não pertence a este veículo.")

        self.registrar_evento(manutencao)

        from src.veiculo import StatusVeiculo
        self.alterar_status(StatusVeiculo.MANUTENCAO)

    def concluir_manutencao(self) -> None:
        from src.veiculo import StatusVeiculo

        if self.status != StatusVeiculo.MANUTENCAO:
            raise ValueError("O veículo não está em manutenção.")

        self.alterar_status(StatusVeiculo.ATIVO)