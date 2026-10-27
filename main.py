from src.persistencia_json import (
    carregar_motoristas,
    carregar_veiculos, 
    carregar_alocacoes,
    salvar_veiculos,
    salvar_motoristas
)
from src.veiculo import Veiculo, Carro, Moto, Caminhao
from src.pessoa import Motorista
import argparse

veiculos = carregar_veiculos()

motoristas = carregar_motoristas()

alocacoes = carregar_alocacoes(motoristas, veiculos)

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

parser_veiculos.set_defaults(acao="veiculos")

parser_motoristas.set_defaults(acao="motoristas")

parser_alocacoes.set_defaults(acao="alocacoes")

parser_cadastrar_veiculo.set_defaults(acao="cadastro_veiculo")

parser_cadastrar_motorista.set_defaults(acao="cadastro_motorista")

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