# 🪖 Central de Operações de Mercenários

**Missões, agentes e recompensas em um só terminal.**

Projeto acadêmico em Python para praticar Programação Orientada a Objetos com um sistema de contratos de operação. O usuário cadastra um mercenário, descreve a missão, informa a recompensa e recebe um código automático para acompanhar a ordem.

> **Importante:** os dados ficam na memória durante a execução. Ao encerrar o programa, as ordens são apagadas.

## 🎯 O que o sistema faz

| Opção | Ação |
| --- | --- |
| `[1]` | Cadastra um contrato e gera seu código, como `OP-001` |
| `[2]` | Lista os contratos da sessão |
| `[3]` | Busca uma ordem pelo código |
| `[4]` | Edita tipo da operação, recompensa e status |
| `[0]` | Encerra a sessão |

Cada contrato guarda o mercenário responsável, sua especialidade, o tipo de missão, o valor da recompensa e o status.

## 🕹️ Exemplo rápido

Na opção `[1]`, informe:

```text
Nome do mercenário: Agente Teste
Especialidade: Reconhecimento
Tipo da missão/contrato: Escolta de comboio
Valor da recompensa (R$): 2500
```

O programa cria e apresenta a ordem:

```text
OP-001 | Escolta de comboio | Mercenário: Agente Teste (Reconhecimento) | Recompensa: R$ 2500.00 | Status: DISPONÍVEL
```

Use `[2]` para listar, `[3]` para consultar pelo código ou `[4]` para editar. Na edição, pressione ENTER nos campos que deseja manter.

## 📖 Guia passo a passo

1. **Inicie o programa** com `python main.py`. O menu oferece cadastro, listagem, busca, edição e encerramento.
2. **Cadastre um contrato** escolhendo `[1]`. Informe nome, especialidade, missão e recompensa. O sistema valida os campos e gera o código da ordem.
3. **Confira os contratos** com `[2]`. A lista mostra os registros criados desde que o programa foi iniciado.
4. **Consulte uma ordem** com `[3]` e digite o código, por exemplo `OP-001`. A busca aceita letras maiúsculas ou minúsculas.
5. **Edite uma ordem** com `[4]`. Digite o código e informe o novo tipo de missão, recompensa e status. Pressione ENTER para manter qualquer campo sem alteração.

Os status disponíveis na edição são:

| Número | Status |
| --- | --- |
| `1` | DISPONÍVEL |
| `2` | EM ANDAMENTO |
| `3` | CONCLUÍDA |
| `4` | CANCELADA |

6. **Encerre** com `[0]`. Como o projeto usa somente memória, as ordens deixam de existir quando o programa fecha.

## 🧠 Onde aparece a POO

| Classe | Responsabilidade |
| --- | --- |
| `Mercenario` | Guarda e valida nome e especialidade do agente |
| `OrdemOperacao` | Representa a missão, o valor, o status e o código da ordem |
| `CentralOperacoes` | Cria, busca, lista e edita as ordens da sessão |

O encapsulamento aparece nas propriedades validadas dos modelos. Uma `OrdemOperacao` está associada ao objeto `Mercenario` responsável. A interface (`main.py`), o gerenciamento (`gerenciador.py`) e os modelos (`models.py`) ficam separados para cada parte ter uma função clara.

## 🚀 Executar no computador

É necessário ter **Python 3.8 ou superior**. O projeto não usa bibliotecas externas.

```bash
git clone https://github.com/tslopes88/central-contratos-mercenarios.git
cd central-contratos-mercenarios
python main.py
```

## 🌐 Executar pelo navegador

O GitHub Codespaces abre um ambiente de desenvolvimento no navegador. A aplicação continua sendo de terminal — não é uma interface web.

1. Abra o [repositório](https://github.com/tslopes88/central-contratos-mercenarios).
2. Clique em **Code** e selecione a aba **Codespaces**.
3. Escolha **Create codespace on main** e aguarde o ambiente iniciar.
4. No terminal integrado, rode:

```bash
python main.py
```

O acesso ao Codespaces depende dos limites e da disponibilidade na conta GitHub.

## 🗂️ Arquivos do projeto

```text
.
├── main.py                 # Menu e interação pelo terminal
├── gerenciador.py          # Operações da central
├── models.py               # Classes Mercenario e OrdemOperacao
└── tests/
    └── test_operacoes.py  # Testes das regras principais
```

## ✅ Testes

Para executar os testes automatizados:

```bash
python -m unittest discover -s tests -v
```

## 🎤 Explicação para apresentar

> Este projeto é uma central de operações de mercenários feita em Python e executada pelo terminal. O usuário cadastra um agente, descreve uma missão e define sua recompensa. O programa gera um código para a ordem e permite listar, consultar e editar os contratos durante a sessão. A Programação Orientada a Objetos aparece nas classes `Mercenario`, `OrdemOperacao` e `CentralOperacoes`: cada uma representa uma parte do sistema. As propriedades validam os dados, e cada ordem mantém uma associação com o mercenário responsável. A central guarda as ordens em memória; por isso, elas são apagadas quando o programa é encerrado. Vou demonstrar criando uma ordem, consultando seu código e alterando seu status.
