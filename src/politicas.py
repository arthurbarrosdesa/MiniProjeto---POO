from src.veiculo import Carro, Moto, Caminhao
from src.pessoa import Motorista

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

    def verificar_consumo(self):
        pass


    def verificar_alocacao(self):
        pass


    def verificar_manu_prev(self):
        pass


    def verificar_cnh(self, motorista : Motorista, veiculo : Veiculo) -> bool:
        compat_cnh = {
            "carro": ["B"],
            "moto": ["A"],
            "caminhao": ["C", "D", "E"],
        }
        
        categorias = compat_cnh.get(veiculo.tipo, [])

        return motorista.categoria_cnh.upper() in categorias