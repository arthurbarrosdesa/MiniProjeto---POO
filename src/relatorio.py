from src.veiculo import Veiculo
from src.pessoa import Motorista
from src.alocacao import Alocacao

class Relatorio:

    """
    Classe "Relatório" armazena os dados necessários para a emissão de um relatório.

    Atributos:
    Custo total e médio de manutenção por tipo de veículo;
    Ranking de eficiência;
    Total de viagens por motorista;
    Quilometragem média por tipo de veículo.

    Métodos:
    ranking_eficiencia( );
    emitir_relatorio( ).
    custo_manu_tipo(): dict;
    total_viagens_motorista(): dict;
    quilometragem_media_tipo(): dict;
    relatorio_consumo(): list
    """

    def __init__(self, motoristas, alocacoes):
        self.__motoristas = motoristas
        self.__alocacoes = alocacoes

    @property
    def motoristas(self):
        return self.__motoristas

    @property
    def alocacoes(self):
        return self.__alocacoes

    def ranking_eficiencia(self):
        veiculos = []

        for alocacao in self.alocacoes:
            veiculo = alocacao.veiculo

            if veiculo not in veiculos:
                veiculos.append(veiculo)
        
        veiculos = sorted(
            veiculos,
            key=lambda veiculo: veiculo.consumo_medio,
            reverse=True
        )

        resultado = []

        for veiculo in veiculos:
            resultado.append({
                "placa": veiculo.placa,
                "consumo_medio": veiculo.consumo_medio
            })

        return resultado

    def emitir_relatorio(self):
        pass
    

    def custo_manu_tipo(self):
        pass
    

    def total_viagens_motorista(self):
        resultado = {}

        for motorista in self.motoristas:
            contador = 0

            for alocacao in self.alocacoes:
                if motorista.cpf == alocacao.motorista.cpf:
                    contador += 1
            
            resultado[motorista.cpf] = contador
            
        return resultado    
    

    def quilometragem_media_tipo(self):
        pass
    

    def relatorio_consumo(self):
        pass

    

