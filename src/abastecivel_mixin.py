from src.excecoes import AbastecimentoInvalidoError

class AbastecivelMixin:

    """
    Mixin responsável pelas operações de abastecimento dos veículos.
    """

    def registrar_abastecimento(self, abastecimento) -> None:
        if abastecimento.veiculo is not self:
            raise AbastecimentoInvalidoError("O abastecimento não pertence a este veículo.")

        self.registrar_evento(abastecimento)

        novo_consumo = abastecimento.calcular_cons_medio()
        self.atualizar_consumo_medio(novo_consumo)