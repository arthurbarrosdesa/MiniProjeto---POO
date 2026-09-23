# MiniProjeto---POO

---

## Projeto do curso de Engenharia de Software da UFCA

---

## Descrição do projeto

### Tema 2: Sistema de Gerenciamento de frotas de veículos

#### Visão Geral:

Desenvolver um sistema de linha de comando (CLI) ou uma API mínima (FastAPI ou Flask, opcional) para gerenciar a frota de veículos de uma empresa de transporte.
O sistema deve permitir o cadastro de veículos, controle de manutenções, alocação a motoristas, registro de abastecimentos, cálculo de custos médios e relatórios de desempenho. O sistema deve aplicar conceitos de encapsulamento, herança (simples e múltipla), métodos especiais, regras de negócio configuráveis. A persistência pode ser feita em JSON ou SQLite, com um repositório desacoplado do domínio.

---
## Modelagem OO

### UML textual:

#### Classe: Veículos

##### Atributos:
- Placa: str;
- Marca: str;
- Modelo: str;
- Ano: int;
- Tipo (carro, moto, caminhão): str;
- Quilometragem: float;
- Consumo Médio (Km/L): float;
- Status (ativo, manutenção, inativo).

##### Métodos:
- cadastrar_veículo( );
- alterar_status( ):
- registrar_eventos( );

#### Classe: Pessoa

##### Atributos:
- 

##### Métodos:
- 

#### Classe: Alocação

##### Atributos:
- Origem: str;
- Destino: str;
- Distância percorrida: float;

##### Métodos:
- atualizar_quilometragem( );
- registrar_viagem( );

#### Classe: Manutenção

##### Atributos:
- Data: str;
- Tipo (preventiva ou corretiva);
- Custo: float;
- Descrição: str.

##### Métodos:
- calcular_custo( );
- atualizar_status_veículo( ).

#### Classe: Abastecimento

##### Atributos:
- 

##### Métodos:
- 

#### Classe: Políticas

##### Atributos:
- 

##### Métodos:
- 

#### Classe: Relatório

##### Atributos:
- 

##### Métodos:
- 

#### Classe: Motorista (*É uma pessoa*)

##### Atributos:
- Nome: str;
- CPF: str;
- Categoria CNH: str;
- Tempo de experiência: int;
- Disponibilidade: bool;
- Histórico de viagens.

##### Métodos:
- cadastrar_motorista( );
- editar_info_motorista( );

#### Classe: Carro (*É um veículo*)

##### Atributos:
- 

##### Métodos:
- 

#### Classe: Moto (*É um veículo*)

##### Atributos:
- 

##### Métodos:
- 

#### Classe: Caminhão (*É um veículo*)

##### Atributos:
- 

##### Métodos:
- 
