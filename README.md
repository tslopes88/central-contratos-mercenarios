# Central de Operações de Mercenários

Projeto de terminal em Python para cadastrar contratos de missão. Cada ordem fica ligada a um mercenário, recebe um código automático e guarda o tipo da operação, a recompensa e o status. Os dados ficam na memória durante a execução e são apagados ao fechar o programa.

## Executar

É necessário ter Python 3.8 ou superior. Não há dependências externas.

```text
python main.py
```

O menu permite cadastrar, listar, buscar e editar ordens. Para cadastrar, informe o nome e a especialidade do mercenário, o tipo da missão e o valor da recompensa. Valores podem usar vírgula ou ponto decimal.

## Executar pelo navegador

O programa continua funcionando pelo terminal, mas o terminal pode ser aberto dentro do navegador usando o GitHub Codespaces:

1. Abra o [repositório no GitHub](https://github.com/tslopes88/central-contratos-mercenarios).
2. Clique em **Code** e abra a aba **Codespaces**.
3. Escolha **Create codespace on main** e aguarde o ambiente carregar.
4. No terminal integrado, execute:

```text
python main.py
```

Isso não transforma o projeto em uma aplicação web: a interação ainda acontece pelo terminal. O uso do Codespaces depende da disponibilidade e dos limites da conta GitHub.

## Como o programa está organizado

- `main.py` mostra o menu, lê as respostas e chama as operações.
- `gerenciador.py` contém `CentralOperacoes`, que mantém as ordens da sessão.
- `models.py` contém `Mercenario` e `OrdemOperacao`, que representam os dados.

As propriedades de `Mercenario` e `OrdemOperacao` validam os dados antes de aceitá-los. Uma `OrdemOperacao` está associada a um objeto `Mercenario`; a `CentralOperacoes` mantém a coleção de ordens. Essa separação permite que o menu cuide da entrada e saída, enquanto as classes cuidam dos dados e das regras.

## Roteiro para demonstrar

1. Execute `python main.py` e escolha `[1]`.
2. Cadastre, por exemplo, `Agente Teste`, `Reconhecimento`, `Escolta de comboio` e `2500`.
3. Mostre o código gerado, como `OP-001`, e escolha `[2]` para listar as ordens.
4. Escolha `[4]`, informe o código e altere a recompensa ou o status.
5. Escolha `[3]` para consultar a ordem atualizada e `[0]` para encerrar.

Ao terminar, explique que os dados são mantidos apenas enquanto o programa está aberto.

## Testes

```text
python -m unittest discover -s tests -v
```
