from src.veiculo import Carro, Moto, Caminhao
from src.manutencao import Manutencao
from src.politicas import Politicas

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
    custo_manu_tipo(): dict;
    total_viagens_motorista(): dict;
    quilometragem_media_tipo(): dict;
    relatorio_consumo(): list
    """

    def __init__(self, motoristas, alocacoes, veiculos):
        self.__motoristas = motoristas
        self.__alocacoes = alocacoes
        self.__veiculos = veiculos
        self.__politicas = Politicas()

    @property
    def motoristas(self):
        return self.__motoristas

    @property
    def alocacoes(self):
        return self.__alocacoes

    @property
    def veiculos(self):
        return self.__veiculos

    @property
    def politicas(self):
        return self.__politicas

    def ranking_eficiencia(self):
        veiculos = sorted(
            self.veiculos,
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

    def custo_manu_tipo(self):
        qtd_carro = 0
        qtd_moto = 0
        qtd_caminhao = 0
        soma_carro = 0
        soma_moto = 0
        soma_caminhao = 0

        for veiculo in self.veiculos:
            for evento in veiculo.historico_eventos:
                if isinstance(evento, Manutencao):
                    if isinstance(evento.veiculo, Carro):
                        soma_carro += evento.custo
                        qtd_carro += 1
                    elif isinstance(evento.veiculo, Moto):
                        soma_moto += evento.custo
                        qtd_moto += 1
                    elif isinstance(evento.veiculo, Caminhao):
                        soma_caminhao += evento.custo
                        qtd_caminhao += 1

        media_carro = soma_carro / qtd_carro if qtd_carro > 0 else 0
        media_moto = soma_moto / qtd_moto if qtd_moto > 0 else 0
        media_caminhao = soma_caminhao / qtd_caminhao if qtd_caminhao > 0 else 0

        resultado = {
            "carro": {
                "qtd_manu": qtd_carro,
                "total": soma_carro,
                "media": media_carro
            },
            "moto": {
                "qtd_manu": qtd_moto,
                "total": soma_moto,
                "media": media_moto
            },
            "caminhao": {
                "qtd_manu": qtd_caminhao,
                "total": soma_caminhao,
                "media": media_caminhao
            },
        }

        return resultado



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
        qtd_carro = 0
        qtd_moto = 0
        qtd_caminhao = 0
        soma_carro = 0
        soma_moto = 0
        soma_caminhao = 0

        for veiculo in self.veiculos:
            if isinstance(veiculo, Carro):
                soma_carro += veiculo.quilometragem
                qtd_carro += 1
            elif isinstance(veiculo, Moto):
                soma_moto += veiculo.quilometragem
                qtd_moto += 1
            elif isinstance(veiculo, Caminhao):
                soma_caminhao += veiculo.quilometragem
                qtd_caminhao += 1

        media_carro = soma_carro / qtd_carro if qtd_carro > 0 else 0
        media_moto = soma_moto / qtd_moto if qtd_moto > 0 else 0
        media_caminhao = soma_caminhao / qtd_caminhao if qtd_caminhao > 0 else 0

        resultado = {
            "carro": {
                "qtd_total": qtd_carro,
                "km_total": soma_carro,
                "km_media": media_carro
            },
            "moto": {
                "qtd_total": qtd_moto,
                "km_total": soma_moto,
                "km_media": media_moto
            },
            "caminhao": {
                "qtd_total": qtd_caminhao,
                "km_total": soma_caminhao,
                "km_media": media_caminhao
            },
        }

        return resultado


    def relatorio_consumo(self):
        resultado = []

        for veiculo in self.veiculos:
            if not self.politicas.verificar_consumo(veiculo):
                resultado.append({
                    "veiculo": veiculo.placa,
                    "consumo": veiculo.consumo_medio
                })

        return resultado