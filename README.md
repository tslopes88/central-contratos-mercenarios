# Central de Contratos de Mercenários

Aplicação de terminal em Python para cadastrar e acompanhar contratos de operação atribuídos a mercenários. Cada contrato recebe um código automático e registra o tipo da missão, a recompensa, o agente responsável e o status. Os dados permanecem em memória durante a execução e são descartados quando o programa é encerrado.

## Requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa

## Como executar

Abra o terminal nesta pasta e rode:

```text
python main.py
```

Escolha **Cadastrar contrato de operação** e informe o nome do mercenário, sua especialidade, o tipo da missão/contrato e o valor da recompensa. O sistema gera um código como `OP-001`. Enquanto a sessão estiver aberta, é possível listar e buscar ordens, além de editar o tipo, a recompensa e o status. Valores podem ser informados com vírgula ou ponto decimal.

## Organização e POO

- `models.py`: classes `Mercenario` e `OrdemOperacao`; validam e representam os dados do domínio.
- `gerenciador.py`: classe `CentralOperacoes`, responsável por criar, buscar, listar e editar ordens em memória.
- `main.py`: menu e interação com o usuário pelo terminal.

O projeto aplica classes e objetos, encapsulamento por propriedades validadas e composição: cada ordem de operação mantém o mercenário responsável, e a central mantém uma coleção de ordens.

## Testes

Execute os testes automatizados com:

```text
python -m unittest discover -s tests -v
```
