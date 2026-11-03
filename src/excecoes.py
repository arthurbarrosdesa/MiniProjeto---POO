class AlocacaoInvalidaError(ValueError):
    """Erro relacionado às regras de alocação de veículos."""
    pass

class AbastecimentoInvalidoError(ValueError):
    """Erro relacionado ao registro de abastecimentos."""
    pass

class ManutencaoInvalidaError(ValueError):
    """Erro relacionado ao registro de manutenções."""
    pass

class PoliticaNaoAtendidaError(ValueError):
    """Erro relacionado ao descumprimento de políticas do sistema."""
    pass

class RepositorioError(Exception):
    """Erro relacionado ao salvamento e carregamento de dados."""
    pass
    