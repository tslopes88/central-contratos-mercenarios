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

## 🎤 Roteiro curto para apresentar

1. Explique que o sistema organiza contratos de missão para mercenários.
2. Cadastre uma ordem e mostre o código gerado.
3. Liste e consulte a ordem pelo código.
4. Edite a recompensa ou o status.
5. Aponte as classes `Mercenario`, `OrdemOperacao` e `CentralOperacoes` e explique que os dados desaparecem ao encerrar o programa.
