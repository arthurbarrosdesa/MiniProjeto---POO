from src.veiculo import Veiculo, StatusVeiculo
from src.pessoa import Motorista
import json
from pathlib import Path
from src.manutencao import Manutencao

class Politicas:

    """
    Classe "Politicas" armazena as políticas e normas que regem os outros processos do sistema.

    Atributos:
    Padrão de consumo;
    Compatibilidade CNH-Veículo;
    Verificar alocação;
    Quilometragem para manutenção preventiva;
    Custo por tipo de manutenção.

    Métodos:
    verificar_consumo( );
    verificar_alocacao( );
    verificar_manu_prev( );
    verificar_cnh( ).
    """

    def __init__(self):
        caminho_config = Path(__file__).resolve().parent.parent / "settings.json"

        with open(caminho_config, "r", encoding="utf-8") as arquivo:
            self.configuracoes = json.load(arquivo)

    def verificar_consumo(self, veiculo: Veiculo):
        faixa_padrao = self.configuracoes["faixa_consumo"]

        minimo = faixa_padrao["minimo"]
        maximo = faixa_padrao["maximo"]

        return minimo <= veiculo.consumo_medio <= maximo


    def verificar_alocacao(self, motorista: Motorista, veiculo: Veiculo):
        if not motorista.disponibilidade:
            raise ValueError("Motorista indisponível")

        if veiculo.status != StatusVeiculo.ATIVO:
            raise ValueError("Veículo inativo ou em manutenção.")

        if not self.verificar_cnh(motorista, veiculo):
            raise ValueError("Categoria CNH incompatível com o veículo.")

        return True


    def verificar_manu_prev(self, veiculo: Veiculo):
        lim_quilo = self.configuracoes["limite_km_revisao_preventiva"]

        manu_preventivas = [
            evento for evento in veiculo.historico_eventos
            if isinstance(evento, Manutencao) and evento.tipo_manu == "preventiva"
        ]

        if manu_preventivas:
            ultima_manu = max(
                manu_preventivas,
                key=lambda manutencao: manutencao.data
            )
            km_ultima_manu = ultima_manu.quilometragem
        else:
            km_ultima_manu = 0

        return veiculo.quilometragem - km_ultima_manu >= lim_quilo


    def verificar_cnh(self, motorista : Motorista, veiculo : Veiculo) -> bool:
        compat_cnh = self.configuracoes["categorias_cnh"]

        categorias = compat_cnh.get(veiculo.tipo, [])

        return motorista.categoria_cnh.upper() in categorias