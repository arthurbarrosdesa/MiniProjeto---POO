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
## Modelagem Orientada a Objetos

### UML textual:

> #### Classe: Veiculo
> Classe-base que representa os veículos da frota.
>
> ##### Atributos:
> - Placa: str;
> - Marca: str;
> - Modelo: str;
> - Ano: int;
> - Quilometragem: float;
> - Consumo Médio (Km/L): float;
> - Status (ativo, manutenção, inativo);
> - Histórico de eventos: list.
> 
> ##### Métodos:
> - alterar_status(novo_status: StatusVeiculo): void;
> - atualizar_quilometragem(): void;
> - registrar_evento(): void;
> - __str__(): str;
> - __repr__(): str;
> - __eq__(): bool;
> - __lt__(): bool;
> - __iter__(): Iterator.

> #### Classe: Pessoa
> Representa uma pessoa no sistema.
> 
> ##### Atributos:
> - CPF: str;
> - Nome: str.
> 
> ##### Métodos:
> - __str__();
> - __repr__().

> #### Classe: Alocação
> Responsável por relacionar motoristas e veículos às viagens.
> 
> ##### Atributos:
> - Motorista: Motorista;
> - Veículo: Veículo;
> - Origem: str;
> - Destino: str;
> - Distância percorrida: float;
> - Combustível gasto: float.
> 
> ##### Métodos:
> - realizar_viagem( ).

> #### Classe: Manutenção
> Responsável por registrar manutenções preventivas e corretivas.
> 
> ##### Atributos:
> - Data: str;
> - Tipo (preventiva ou corretiva);
> - Custo: float;
> - Descrição: str.
> 
> ##### Métodos:
> - __str__().

> #### Classe: Abastecimento
> Responsável por registrar os abastecimentos realizados.
> 
> ##### Atributos:
> - Data: str;
> - Tipo de combustível: str;
> - Litros: float;
> - Valor pago: float.
> 
> ##### Métodos:
> - __str__().

> #### Classe: Políticas
> Responsável por centralizar regras e parâmetros configuráveis.
> 
> ##### Atributos:
> - Padrão de consumo: float;
> - Compatibilidade CNH-Veículo: dict;
> - Quilometragem para manutenção preventiva: float;
> - Custo de manutenção: float.
> 
> ##### Métodos:
> - verificar_alocacao( );
> - verificar_manu_prev( );
> - verificar_cnh( );
> - verificar_consumo().

> #### Classe: Relatório
> Responsável por apresentar informações relevantes sobre a frota.
> 
> ##### Atributos:
> - Custo total e médio de manutenção por tipo de veículo: float;
> - Ranking de eficiência: list;
> - Total de viagens por motorista: int;
> - Quilometragem média por tipo de veículo: float
> 
> ##### Métodos:
> - ranking_eficiencia( );
> - custo_manu_tipo(): dict;
> - total_viagens_motorista(): dict;
> - quilometragem_media_tipo(): dict;
> - relatorio_consumo(): list
> - emitir_relatorio( ).

> #### Classe: Motorista (*É uma pessoa*)
> Subclasse de Pessoa, representa um motorista cadastrado no sistema.
> 
> ##### Atributos:
> - Categoria CNH: str;
> - Tempo de experiência: int;
> - Disponibilidade: bool;
> - Histórico de viagens.
> 
> ##### Métodos:
> - registrar_viagem();
> - atualizar_disponibilidade();
> - __str__().

> #### Classe: Carro (*É um veículo*)
> 
> ##### Atualmente, essa classe herda a estrutura e os comportamentos de Veiculo, sem atributos ou métodos específicos adicionais.

> #### Classe: Moto (*É um veículo*)
>
> ##### Atualmente, essa classe herda a estrutura e os comportamentos de Veiculo, sem atributos ou métodos específicos adicionais.


> #### Classe: Caminhão (*É um veículo*)
> 
> ##### Atualmente, essa classe herda a estrutura e os comportamentos de Veiculo, sem atributos ou métodos específicos adicionais.

> #### Classe: AbastecivelMixin
> Responsável pelas operações de abastecimento e pelo histórico de abastecimentos.
>
> ##### Atributos:
> - Histórico de abastecimentos: list.
>
> ##### Métodos:
> - abastecer();
> - calcular_cons_medio().

> #### Classe: ManutenivelMixin
> Responsável pelo registro de manutenções e pelo controle relacionado à manutenção dos veículos.
>
> ##### Atributos:
> - Histórico de manutenções: list.
>
> ##### Métodos:
> - registrar_manutenção();
> - alterar_status_manu().

#### Diagrama UML gerado a partir das informações acima:

```mermaid
classDiagram

    class StatusVeiculo {
        <<enumeration>>
        ATIVO
        MANUTENCAO
        INATIVO
    }

    class Veiculo {
        -str placa
        -str marca
        -str modelo
        -int ano
        -float quilometragem
        -float consumo_medio
        -StatusVeiculo status
        -list historico_eventos
        +alterar_status(novo_status: StatusVeiculo) None
        +atualizar_quilometragem(nova_quilometragem: float) None
        +registrar_evento(evento: str) None
        +__str__() str
        +__repr__() str
        +__eq__(other) bool
        +__lt__(other) bool
        +__iter__()
    }

    class Carro
    class Moto
    class Caminhao

    class Pessoa {
        -str cpf
        -str nome
        +__str__() str
        +__repr__() str
    }

    class Motorista {
        -str categoria_cnh
        -int tempo_experiencia
        -bool disponibilidade
        -list historico_viagens
        +registrar_viagem(viagem: str) None
        +atualizar_disponibilidade(nova_disponibilidade: bool) None
        +__str__() str
    }

    class Alocacao {
        -Motorista motorista
        -Veiculo veiculo
        -str origem
        -str destino
        -float distancia_percorrida
        -float combustivel_gasto
        +realizar_viagem()
    }

    class Manutencao {
        -str data
        -str tipo
        -float custo
        -str descricao
        +__str__() str
    }

    class Abastecimento {
        -str data
        -str tipo_combustivel
        -float litros
        -float valor_pago
        +__str__() str
    }

    class Politicas {
        -float padrao_consumo
        -dict compatibilidade_cnh_veiculo
        -float quilometragem_manutencao_preventiva
        -float custo_manutencao
        +verificar_alocacao()
        +verificar_manu_prev()
        +verificar_cnh()
        +verificar_consumo()
    }

    class Relatorio {
        -float custo_total_medio_manutencao
        -list ranking_eficiencia
        -int total_viagens_motorista
        -float quilometragem_media_tipo
        +ranking_eficiencia()
        +custo_manu_tipo() dict
        +total_viagens_motorista() dict
        +quilometragem_media_tipo() dict
        +relatorio_consumo() list
        +emitir_relatorio()
    }

    class AbastecivelMixin {
        -list historico_abastecimentos
        +abastecer()
        +calcular_cons_medio()
    }

    class ManutenivelMixin {
        -list historico_manutencoes
        +registrar_manutencao()
        +alterar_status_manu()
    }

    Veiculo --> StatusVeiculo : utiliza

    Veiculo <|-- Carro
    Veiculo <|-- Moto
    Veiculo <|-- Caminhao

    Pessoa <|-- Motorista

    AbastecivelMixin <|-- Carro
    AbastecivelMixin <|-- Moto
    AbastecivelMixin <|-- Caminhao

    ManutenivelMixin <|-- Carro
    ManutenivelMixin <|-- Moto
    ManutenivelMixin <|-- Caminhao

    Motorista "1" --> "0..*" Alocacao : realiza
    Veiculo "1" --> "0..*" Alocacao : utiliza

    Veiculo "1" --> "0..*" Manutencao : possui
    Veiculo "1" --> "0..*" Abastecimento : possui

    Politicas --> Veiculo : verifica
    Politicas --> Motorista : valida CNH
    Politicas --> Alocacao : verifica

    Relatorio --> Veiculo : analisa
    Relatorio --> Motorista : analisa
    Relatorio --> Manutencao : calcula
    Relatorio --> Abastecimento : analisa
    Relatorio --> Alocacao : contabiliza
```
```
