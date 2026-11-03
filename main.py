from src.seed import inicializar_dados
from src.persistencia_json import (
    carregar_motoristas,
    carregar_veiculos, 
    carregar_alocacoes,
    carregar_abastecimentos,
    carregar_manutencoes,
    salvar_veiculos,
    salvar_motoristas,
    salvar_alocacoes,
    salvar_abastecimentos,
    salvar_manutencoes
)
from src.veiculo import Veiculo, Carro, Moto, Caminhao, StatusVeiculo
from src.pessoa import Motorista
from src.alocacao import Alocacao
from src.abastecimento import Abastecimento
from src.manutencao import Manutencao
from src.relatorio import Relatorio
from datetime import datetime
import argparse

def converter_booleano(valor):
    valor = valor.lower()

    if valor in ("sim", "true", "1"):
        return True
    elif valor in ("nao", "não", "false", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError(
            "Informe sim ou nao."
        )

if __name__ == "__main__":
    inicializar_dados()

    veiculos = carregar_veiculos()

    motoristas = carregar_motoristas()

    alocacoes = carregar_alocacoes(motoristas, veiculos)

    abastecimentos = carregar_abastecimentos(veiculos)

    manutencoes = carregar_manutencoes(veiculos)

    relatorio = Relatorio(motoristas, alocacoes, veiculos)


parser = argparse.ArgumentParser(
    description=(
        "SISTEMA DE GERENCIAMENTO DE FROTAS\n\n"
        "Gerencie veículos, motoristas, viagens, abastecimentos "
        "e manutenções.\n"
        "Também permite consultar relatórios e acompanhar os "
        "dados da frota."
    ),
    epilog=(
        "Exemplo de uso:\n"
        "  python main.py listar-veiculos\n"
        "  python main.py relatorios eficiencia\n"
        "  python main.py cadastrar-motorista --help"
    ),
    formatter_class=argparse.RawDescriptionHelpFormatter
)


subparsers = parser.add_subparsers(
    required=True,
    title="Comandos disponíveis",
    description="Selecione uma das operações abaixo."
)


parser_veiculos = subparsers.add_parser(
    "listar-veiculos",
    help="Exibe todos os veículos cadastrados",
    description="Lista os veículos e suas principais informações."
)

parser_motoristas = subparsers.add_parser(
    "listar-motoristas",
    help="Exibe todos os motoristas cadastrados",
    description="Lista os motoristas registrados no sistema."
)

parser_alocacoes = subparsers.add_parser(
    "listar-alocacoes",
    help="Exibe as viagens e alocações registradas",
    description="Lista as alocações realizadas."
)

parser_listar_abastecimentos = subparsers.add_parser(
    "listar-abastecimentos",
    help="Exibe os abastecimentos registrados.",
    description="Lista os abastecimentos realizados."
    )
parser_listar_abastecimentos.set_defaults(acao="abastecimentos")

parser_listar_manutencoes = subparsers.add_parser(
    "listar-manutencoes",
    help="Exibe as manutenções registradas",
    description="Lista as manutenções registradas"
    )
parser_listar_manutencoes.set_defaults(acao="manutencoes")

parser_cadastrar_veiculo = subparsers.add_parser(
    "cadastrar-veiculo",
    help="Cadastra um novo veículo",
    description="Registra um veículo na frota."
)
parser_cadastrar_veiculo.add_argument(
    '--tipo',
    type = str,
    choices = ["carro", "moto", "caminhao"],
    required = True
)
parser_cadastrar_veiculo.add_argument(
    '--placa',
    type = str,
    required = True
)
parser_cadastrar_veiculo.add_argument(
    '--marca',
    type = str,
    required = True
)
parser_cadastrar_veiculo.add_argument(
    '--modelo',
    type = str,
    required = True
)
parser_cadastrar_veiculo.add_argument(
    '--ano',
    type = int,
    required = True
)
parser_cadastrar_veiculo.add_argument(
    '--consumo-medio',
    type = float,
    required = True
)

parser_cadastrar_motorista = subparsers.add_parser(
    "cadastrar-motorista",
    help="Cadastra um motorista no sistema.",
    description="Registra um novo motorista."
    )
parser_cadastrar_motorista.add_argument(
    '--cpf',
    type = str,
    required = True
)
parser_cadastrar_motorista.add_argument(
    '--nome',
    type = str,
    required = True
)
parser_cadastrar_motorista.add_argument(
    '--categoria-cnh',
    type = str,
    required = True
)
parser_cadastrar_motorista.add_argument(
    '--tempo-experiencia',
    type = int,
    required = True
)

parser_cadastrar_alocacao = subparsers.add_parser(
    "cadastrar-alocacao",
    help="Cadastra uma alocação no sistema.",
    description="Registra uma nova alocação."
    )
parser_cadastrar_alocacao.add_argument(
    '--cpf',
    type = str,
    required = True
)
parser_cadastrar_alocacao.add_argument(
    '--placa',
    type = str,
    required = True
)
parser_cadastrar_alocacao.add_argument(
    '--origem',
    type = str,
    required = True
)
parser_cadastrar_alocacao.add_argument(
    '--destino',
    type = str,
    required = True
)
parser_cadastrar_alocacao.add_argument(
    '--dist-percorrida',
    type = float,
    required = True
)

parser_cadastrar_abastecimento = subparsers.add_parser(
    "cadastrar-abastecimento",
    help="Cadastra um abastecimento no sistema.",
    description="Resistra um novo abastecimento."
    )
parser_cadastrar_abastecimento.add_argument(
    '--data',
    type = str,
    required = True
)
parser_cadastrar_abastecimento.add_argument(
    '--tipo-comb',
    type = str,
    required = True
)
parser_cadastrar_abastecimento.add_argument(
    '--litros',
    type = float,
    required = True
)
parser_cadastrar_abastecimento.add_argument(
    '--valor-pago',
    type = float,
    required = True
)
parser_cadastrar_abastecimento.add_argument(
    '--placa',
    type = str,
    required = True
)

parser_cadastrar_manutencao = subparsers.add_parser(
    "cadastrar-manutencao",
    help="Cadastra uma manutenção no sistema.",
    description="Registra uma nova manutenção."
    )
parser_cadastrar_manutencao.add_argument(
    '--data',
    type = str,
    required = True
)
parser_cadastrar_manutencao.add_argument(
    '--tipo-manu',
    type = str,
    choices = ["preventiva", "corretiva"],
    required = True
)
parser_cadastrar_manutencao.add_argument(
    '--custo',
    type = float,
    required = True
)
parser_cadastrar_manutencao.add_argument(
    '--placa',
    type = str,
    required = True
)
parser_cadastrar_manutencao.add_argument(
    '--descricao',
    type = str,
    required = True
)

parser_relatorios = subparsers.add_parser(
    "relatorios",
    help="Consulta os relatórios da frota",
    description="Gera relatórios sobre eficiência, custos, viagens, quilometragem e consumo."
)
subparsers_relatorios = parser_relatorios.add_subparsers(
    required=True,
    title="Relatórios disponíveis",
    description="Selecione o relatório desejado."
)

parser_relatorio_eficiencia = subparsers_relatorios.add_parser(
    "eficiencia",
    help="Exibe o ranking de eficiência dos veículos",
    description="Apresenta os veículos classificados por eficiência."
)
parser_relatorio_eficiencia.set_defaults(acao="relatorio_eficiencia")

parser_relatorio_custos = subparsers_relatorios.add_parser(
    "custos-manutencao",
    help="Consulta os custos de manutenção",
    description="Apresenta os custos de manutenção dos veículos."
)
parser_relatorio_custos.set_defaults(acao="relatorio_custos")

parser_relatorio_viagens = subparsers_relatorios.add_parser(
    "viagens",
    help="Consulta a quantidade de viagens por motorista",
    description="Apresenta o total de viagens realizadas pelos motoristas."
)
parser_relatorio_viagens.set_defaults(acao="relatorio_viagens")

parser_relatorio_quilometragem = subparsers_relatorios.add_parser(
    "quilometragem",
    help="Consulta a quilometragem média por tipo de veículo",
    description="Apresenta a quilometragem média dos veículos agrupados por tipo."
)
parser_relatorio_quilometragem.set_defaults(acao="relatorio_quilometragem")

parser_relatorio_consumo = subparsers_relatorios.add_parser(
    "consumo",
    help="Consulta os dados de consumo dos veículos",
    description="Apresenta informações sobre o consumo dos veículos."
)
parser_relatorio_consumo.set_defaults(acao="relatorio_consumo")

parser_atualizar_veiculo = subparsers.add_parser(
    "atualizar-veiculo",
    help="Atualiza a placa de um veículo",
    description="Altera a placa de identificação de um veículo cadastrado."
)
parser_atualizar_veiculo.add_argument(
    '--placa-atual',
    type=str,
    required=True
)
parser_atualizar_veiculo.add_argument(
    '--nova-placa',
    type=str,
    required=True
)

parser_excluir_veiculo = subparsers.add_parser(
    "excluir-veiculo",
    help="Exclui um veículo do cadastro",
    description="Remove um veículo, respeitando as restrições relacionadas ao seu histórico."
)
parser_excluir_veiculo.add_argument('--placa', type=str, required=True)
parser_excluir_veiculo.set_defaults(acao="excluir_veiculo")

parser_atualizar_motorista = subparsers.add_parser(
    "atualizar-motorista",
    help="Atualiza os dados de um motorista",
    description="Altera os dados pessoais, a CNH, a experiência e a disponibilidade de um motorista."
)
parser_atualizar_motorista.add_argument('--cpf', type=str, required=True)
parser_atualizar_motorista.add_argument('--nome', type=str, required=True)
parser_atualizar_motorista.add_argument('--categoria-cnh', type=str, required=True)
parser_atualizar_motorista.add_argument('--experiencia', type=int, required=True)
parser_atualizar_motorista.add_argument('--disponibilidade', type=converter_booleano, required=True)
parser_atualizar_motorista.set_defaults(acao="atualizar_motorista")

parser_excluir_motorista = subparsers.add_parser(
    "excluir-motorista",
    help="Exclui um motorista do cadastro",
    description="Remove um motorista, respeitando as restrições relacionadas ao seu histórico."
)
parser_excluir_motorista.add_argument('--cpf', type=str, required=True)
parser_excluir_motorista.set_defaults(acao="excluir_motorista")

parser_concluir_manutencao = subparsers.add_parser(
    "concluir-manutencao",
    help="Conclui uma manutenção",
    description="Registra a conclusão da manutenção de um veículo."
)
parser_concluir_manutencao.add_argument('--placa', type=str, required=True)
parser_concluir_manutencao.set_defaults(acao="concluir_manutencao")


parser_atualizar_veiculo.set_defaults(acao="atualizar_veiculo")

parser_veiculos.set_defaults(acao="veiculos")

parser_motoristas.set_defaults(acao="motoristas")

parser_alocacoes.set_defaults(acao="alocacoes")

parser_cadastrar_veiculo.set_defaults(acao="cadastro_veiculo")

parser_cadastrar_motorista.set_defaults(acao="cadastro_motorista")

parser_cadastrar_alocacao.set_defaults(acao="cadastro_alocacao")

parser_cadastrar_abastecimento.set_defaults(acao="cadastro_abastecimento")

parser_cadastrar_manutencao.set_defaults(acao="cadastro_manutencao")


args = parser.parse_args()

if args.acao == "motoristas":
    if not motoristas:
        print("Nenhum motorista registrado.")
    else:
        print("\n=== MOTORISTAS CADASTRADOS ===")
        for motorista in motoristas:
            print(motorista)
            print("-----------------------")

elif args.acao == "veiculos":
    if not veiculos:
        print("Nenhum veículo registrado.")
    else:
        print("\n=== VEÍCULOS CADASTRADOS ===")
        for veiculo in veiculos:
            print(veiculo)
            print("-----------------------")

elif args.acao == "alocacoes":
    if not alocacoes:
        print("Nenhuma alocação registrada.")
    else:
        print("\n=== HISTÓRICO DE ALOCAÇÕES ===")
        for alocacao in alocacoes:
            print(alocacao)
            print("-----------------------")


elif args.acao == "abastecimentos":
    if not abastecimentos:
        print("Nenhum abastecimento registrado.")
    else:
        print("\n=== HISTÓRICO DE ABASTECIMENTOS ===")

        for abastecimento in abastecimentos:
            print(abastecimento)
            print("-----------------------")


elif args.acao == "manutencoes":
    if not manutencoes:
        print("Nenhuma manutenção registrada.")
    else:
        print("\n=== HISTÓRICO DE MANUTENÇÕES ===")

        for manutencao in manutencoes:
            print(manutencao)
            print("-----------------------")


elif args.acao == "cadastro_veiculo":
    if args.tipo == "carro":
        classe_veiculo = Carro
    elif args.tipo == "moto":
        classe_veiculo = Moto
    else:
        classe_veiculo = Caminhao
    placa_existe = False
    for veiculo in veiculos:
        if args.placa == veiculo.placa:
            placa_existe = True
            print("Já existe um veículo registrado com essa placa.")
            break
    if not placa_existe:
        try:
            veiculo_criado = classe_veiculo(
                placa=args.placa,
                marca=args.marca,
                modelo=args.modelo,
                ano=args.ano,
                consumo_medio=args.consumo_medio
            )
            veiculos.append(veiculo_criado)
            salvar_veiculos(veiculos)
            print("Veículo cadastrado com sucesso.")
        except ValueError as erro:
            print(f"Não foi possível cadastrar o veículo: {erro}")
elif args.acao == "cadastro_motorista":
    cpf_existe = False
    for motorista in motoristas:
        if args.cpf == motorista.cpf:
            cpf_existe = True
            print("Já existe um motorista registrado com esse CPF.")
            break
    if not cpf_existe:
        try:
            motorista_criado = Motorista(
                cpf=args.cpf,
                nome=args.nome,
                categoria_cnh=args.categoria_cnh,
                tempo_experiencia=args.tempo_experiencia,
                disponibilidade=True
            )
            motoristas.append(motorista_criado)
            salvar_motoristas(motoristas)
            print("Motorista cadastrado com sucesso.")
        except ValueError as erro:
            print(f"Não foi possível cadastrar o motorista: {erro}")
elif args.acao == "cadastro_alocacao":
    motorista_encontrado = None
    veiculo_encontrado = None

    for motorista in motoristas:
        if motorista.cpf == args.cpf:
            motorista_encontrado = motorista
            break

    for veiculo in veiculos:
        if veiculo.placa == args.placa:
            veiculo_encontrado = veiculo
            break
    if motorista_encontrado is None:
        print("Motorista não encontrado.")
    elif veiculo_encontrado is None:
        print("Veículo não encontrado.")
    else:
        try:
            alocacao = Alocacao(
                motorista = motorista_encontrado,
                veiculo = veiculo_encontrado,
                origem = args.origem,
                destino = args.destino,
                dist_percorrida = args.dist_percorrida
            )
            alocacao.realizar_viagem()
            alocacoes.append(alocacao)
            salvar_alocacoes(alocacoes)
            salvar_motoristas(motoristas)
            salvar_veiculos(veiculos)

            print("Alocação cadastrada com sucesso.")
        except ValueError as erro:
            print(f"Não foi possível realizar a viagem: {erro}")
elif args.acao == "cadastro_abastecimento":
    veiculo_encontrado = None

    for veiculo in veiculos:
        if veiculo.placa == args.placa:
            veiculo_encontrado = veiculo
            break

    if veiculo_encontrado is None:
        print("Veículo não encontrado.")
    else:
        try:
            abastecimento = Abastecimento(
                veiculo = veiculo_encontrado,
                data = datetime.fromisoformat(args.data),
                tipo_comb = args.tipo_comb,
                valor_pago = args.valor_pago,
                litros = args.litros
            )
            abastecimento.veiculo.registrar_abastecimento(abastecimento)
            abastecimentos.append(abastecimento)
            salvar_veiculos(veiculos)
            salvar_abastecimentos(abastecimentos)

            print("Abastecimento cadastrado com sucesso.")
        except ValueError as erro:
            print(f"Não foi possível registrar o abastecimento: {erro}")

elif args.acao == "cadastro_manutencao":
    veiculo_encontrado = None

    for veiculo in veiculos:
        if veiculo.placa == args.placa:
            veiculo_encontrado = veiculo
            break

    if veiculo_encontrado is None:
        print("Veículo não encontrado.")
    else:
        try:
            manutencao = Manutencao(
                veiculo = veiculo_encontrado,
                data = datetime.fromisoformat(args.data),
                tipo_manu = args.tipo_manu,
                custo = args.custo,
                descricao = args.descricao
            )
        
            manutencao.veiculo.registrar_manutencao(manutencao)
            manutencoes.append(manutencao)
            salvar_veiculos(veiculos)
            salvar_manutencoes(manutencoes)

            print("Manutenção cadastrada com sucesso.")
        except ValueError as erro:
            print(f"Não foi possível registrar a manutenção: {erro}")
elif args.acao == "relatorio_eficiencia":
    resultado = relatorio.ranking_eficiencia()

    if not veiculos:
        print("Nenhum veículo registrado para gerar o relatório.")
    else:
        print("\n=== RANKING DE EFICIÊNCIA ===")
        for item in resultado:
            print(
                f"Placa: {item['placa']} | "
                f"Consumo médio: {item['consumo_medio']} km/L"
            )

elif args.acao == "relatorio_custos":
    resultado = relatorio.custo_manu_tipo()

    if not veiculos:
        print("Nenhum veículo registrado para gerar o relatório.")
    else:
        print("\n=== RELATÓRIO CUSTO DE MANUTENÇÃO POR TIPO ===")
        for tipo, dados in resultado.items():
            print(f"Tipo: {tipo}")
            print(f"Quantidade: {dados['qtd_manu']}")
            print(f"Custo total: R$ {dados['total']:.2f}")
            print(f"Custo médio: R$ {dados['media']:.2f}")
            print("-----------------------")

elif args.acao == "relatorio_viagens":
    resultado = relatorio.total_viagens_motorista()

    if not motoristas:
        print("Nenhum motorista registrado para gerar o relatório.")
    else:
        print("\n=== TOTAL DE VIAGENS POR MOTORISTA ===")
        for cpf, quantidade in resultado.items():
            print(f"Motorista: {cpf}")
            print(f"Quantidade de viagens: {quantidade}")
            print("-----------------------")

elif args.acao == "relatorio_quilometragem":
    resultado = relatorio.quilometragem_media_tipo()
    
    if not veiculos:
        print("Nenhum veículo registrado para gerar o relatório.")
    else: 
        print("\n=== RELATÓRIO QUILOMETRAGEM POR TIPO ===")
        for tipo, dados in resultado.items():
            print(f"Tipo: {tipo}")
            print(f"Total de veículos: {dados['qtd_total']}")
            print(f"Quilometragem total: {dados['km_total']:.2f}")
            print(f"Quilometragem média: {dados['km_media']:.2f}")
            print("-----------------------")

elif args.acao == "relatorio_consumo":
    resultado = relatorio.relatorio_consumo()

    if not resultado:
        print("Nenhum veículo fora do padrão de consumo registrado.")
    else:
        print("\n=== RELATÓRIO DE CONSUMO ===")
        for item in resultado:
            print(
                f"Placa: {item['veiculo']} | "
                f"Consumo médio: {item['consumo']} km/L"
            )

elif args.acao == "atualizar_veiculo":
    veiculo_encontrado = None
    placa_existe = False

    for veiculo in veiculos:
        if veiculo.placa == args.placa_atual:
            veiculo_encontrado = veiculo
        elif veiculo.placa == args.nova_placa:
            placa_existe = True
            

    if veiculo_encontrado is None:
        print("Veículo não encontrado.")
    elif placa_existe:
        print("Já existe um veículo com essa placa.")
    else:
        try:
            veiculo_encontrado.atualizar_placa(args.nova_placa)

            salvar_veiculos(veiculos)
            salvar_abastecimentos(abastecimentos)
            salvar_alocacoes(alocacoes)
            salvar_manutencoes(manutencoes)

            print("Placa do veículo atualizada com sucesso.")
        except ValueError as erro:
            print(f"Não foi possível atualizar o veículo: {erro}")

elif args.acao == "excluir_veiculo":
    veiculo_encontrado = None

    for veiculo in veiculos:
        if veiculo.placa == args.placa:
            veiculo_encontrado = veiculo
            break       

    if veiculo_encontrado is None:
        print("Veículo não encontrado.")
    else:
        possui_historico = (
            any(alocacao.veiculo is veiculo_encontrado for alocacao in alocacoes)
            or any(abastecimento.veiculo is veiculo_encontrado for abastecimento in abastecimentos)
            or any(manutencao.veiculo is veiculo_encontrado for manutencao in manutencoes)
        )

        if possui_historico:
            print("Não é possível excluir este veículo: existem registros históricos associados.")
            print("Altere o status do veículo para INATIVO para mantê-lo no sistema.")
        else:
            veiculos.remove(veiculo_encontrado)
            salvar_veiculos(veiculos)
            print("Veículo excluído com sucesso.")

elif args.acao == "atualizar_motorista":
    motorista_encontrado = None

    for motorista in motoristas:
        if motorista.cpf == args.cpf:
            motorista_encontrado = motorista
            break
            

    if motorista_encontrado is None:
        print("Motorista não encontrado.")
    else:
        try:
            motorista_encontrado.atualizar_dados(args.nome, args.categoria_cnh, args.experiencia)
            motorista_encontrado.atualizar_disponibilidade(args.disponibilidade)

            salvar_motoristas(motoristas)

            print("Dados do motorista atualizados com sucesso.")
        except ValueError as erro:
            print(f"Erro ao atualizar motorista: {erro}")

elif args.acao == "excluir_motorista":
    motorista_encontrado = None

    for motorista in motoristas:
        if motorista.cpf == args.cpf:
            motorista_encontrado = motorista
            break       

    if motorista_encontrado is None:
        print("Motorista não encontrado.")
    else:
        possui_historico = (
            any(alocacao.motorista is motorista_encontrado for alocacao in alocacoes)
            or bool(motorista_encontrado.historico_viagens)
        )

        if possui_historico:
            print("Não é possível excluir este motorista: existem registros históricos associados.")
            print("O histórico de viagens deve ser preservado.")
        else:
            motoristas.remove(motorista_encontrado)
            salvar_motoristas(motoristas)
            print("Motorista excluído com sucesso.")

elif args.acao == "concluir_manutencao":
    veiculo_encontrado = None

    for veiculo in veiculos:
        if veiculo.placa == args.placa:
            veiculo_encontrado = veiculo
            break

    if veiculo_encontrado is None:
        print("Veículo não encontrado.")
    elif veiculo_encontrado.status != StatusVeiculo.MANUTENCAO:
        print("Este veículo não está em manutenção.")
    else:
        try:
            veiculo_encontrado.concluir_manutencao()
            salvar_veiculos(veiculos)
            print("Manutenção concluída. Veículo voltou ao status ativo.")
        except ValueError as erro:
            print(f"Não foi possível concluir a manutenção: {erro}")
