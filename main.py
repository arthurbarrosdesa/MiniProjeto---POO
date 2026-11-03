from src.persistencia_json import (
    carregar_motoristas,
    carregar_veiculos, 
    carregar_alocacoes,
    carregar_abastecimentos,
    salvar_veiculos,
    salvar_motoristas,
    salvar_alocacoes,
    salvar_abastecimentos
)
from src.veiculo import Veiculo, Carro, Moto, Caminhao
from src.pessoa import Motorista
from src.alocacao import Alocacao
from src.abastecimento import Abastecimento
from datetime import datetime
import argparse


veiculos = carregar_veiculos()

motoristas = carregar_motoristas()

alocacoes = carregar_alocacoes(motoristas, veiculos)

abastecimentos = carregar_abastecimentos(veiculos)


parser = argparse.ArgumentParser(description="SISTEMA DE GERENCIAMENTO DE FROTAS")


subparsers = parser.add_subparsers(required=True)


parser_veiculos = subparsers.add_parser("listar-veiculos")

parser_motoristas = subparsers.add_parser("listar-motoristas")

parser_alocacoes = subparsers.add_parser("listar-alocacoes")

parser_cadastrar_veiculo = subparsers.add_parser("cadastrar-veiculo")
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

parser_cadastrar_motorista = subparsers.add_parser("cadastrar-motorista")
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

parser_cadastrar_alocacao = subparsers.add_parser("cadastrar-alocacao")
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

parser_cadastrar_abastecimento = subparsers.add_parser("cadastrar-abastecimento")
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


parser_veiculos.set_defaults(acao="veiculos")

parser_motoristas.set_defaults(acao="motoristas")

parser_alocacoes.set_defaults(acao="alocacoes")

parser_cadastrar_veiculo.set_defaults(acao="cadastro_veiculo")

parser_cadastrar_motorista.set_defaults(acao="cadastro_motorista")

parser_cadastrar_alocacao.set_defaults(acao="cadastro_alocacao")

parser_cadastrar_abastecimento.set_defaults(acao="cadastro_abastecimento")


args = parser.parse_args()

if args.acao == "motoristas":
    if not motoristas:
        print("Nenhum motorista registrado.")
    else:
        for motorista in motoristas:
            print(motorista)
elif args.acao == "veiculos":
    if not veiculos:
        print("Nenhum veículo registrado.")
    else:
        for veiculo in veiculos:
            print(veiculo)
elif args.acao == "alocacoes":
    if not alocacoes:
        print("Nenhuma alocação registrada.")
    else:
        for alocacao in alocacoes:
            print(alocacao)
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
        veiculo_criado = classe_veiculo(
            placa=args.placa,
            marca=args.marca,
            modelo=args.modelo,
            ano=args.ano,
            consumo_medio=args.consumo_medio
        )
        veiculos.append(veiculo_criado)
        salvar_veiculos(veiculos)
        print("Cadastro concluído com sucesso.")
elif args.acao == "cadastro_motorista":
    cpf_existe = False
    for motorista in motoristas:
        if args.cpf == motorista.cpf:
            cpf_existe = True
            print("Já existe um motorista registrado com esse CPF.")
            break
    if not cpf_existe:
        motorista_criado = Motorista(
            cpf=args.cpf,
            nome=args.nome,
            categoria_cnh=args.categoria_cnh,
            tempo_experiencia=args.tempo_experiencia,
            disponibilidade=True
        )
        motoristas.append(motorista_criado)
        salvar_motoristas(motoristas)
        print("Cadastro concluído com sucesso.")
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
        alocacao = Alocacao(
            motorista = motorista_encontrado,
            veiculo = veiculo_encontrado,
            origem = args.origem,
            destino = args.destino,
            dist_percorrida = args.dist_percorrida
        )
        try:
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
        abastecimento = Abastecimento(
            veiculo = veiculo_encontrado,
            data = datetime.fromisoformat(args.data),
            tipo_comb = args.tipo_comb,
            valor_pago = args.valor_pago,
            litros = args.litros
        )
        try:
            abastecimento.veiculo.registrar_abastecimento(abastecimento)
            abastecimentos.append(abastecimento)
            salvar_veiculos(veiculos)
            salvar_abastecimentos(abastecimentos)

            print("Abastecimento cadastrado com sucesso.")
        except ValueError as erro:
            print(f"Não foi possível registrar o abastecimento: {erro}")