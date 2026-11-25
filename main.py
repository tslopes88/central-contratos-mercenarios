"""Interface de terminal para a central de contratos de mercenários."""

from gerenciador import CentralOperacoes
from models import OrdemOperacao


def _ler_texto(prompt):
    while True:
        try:
            valor = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            return None
        if valor:
            return valor
        print("O campo não pode ficar vazio.")


def _ler_valor(prompt, permitir_vazio=False):
    while True:
        try:
            entrada = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            return None
        if not entrada and permitir_vazio:
            return None
        try:
            valor = float(entrada.replace(",", "."))
        except ValueError:
            print("Digite um valor numérico, por exemplo 1250,50.")
            continue
        if valor < 0:
            print("O valor não pode ser negativo.")
            continue
        return valor


def _ler_texto_opcional(prompt):
    try:
        return input(prompt).strip() or None
    except (EOFError, KeyboardInterrupt):
        return None


def _nova_ordem(central):
    print("\n=== Novo contrato de operação ===")
    nome = _ler_texto("Nome do mercenário: ")
    if nome is None:
        return
    especialidade = _ler_texto("Especialidade: ")
    if especialidade is None:
        return
    tipo_operacao = _ler_texto("Tipo da missão/contrato: ")
    if tipo_operacao is None:
        return
    valor = _ler_valor("Valor da recompensa (R$): ")
    if valor is None:
        return
    try:
        ordem = central.criar_ordem(nome, especialidade, tipo_operacao, valor)
    except (TypeError, ValueError) as erro:
        print("Erro: {}".format(erro))
        return
    print("Contrato criado: {}".format(ordem.resumo()))


def _buscar_ordem(central):
    codigo = _ler_texto("Código da ordem (ex.: OP-001): ")
    if codigo is None:
        return
    ordem = central.buscar_ordem(codigo)
    if ordem is None:
        print("Ordem de operação não encontrada.")
    else:
        print(ordem.resumo())


def _editar_ordem(central):
    codigo = _ler_texto("Código da ordem a editar: ")
    if codigo is None:
        return
    ordem = central.buscar_ordem(codigo)
    if ordem is None:
        print("Ordem de operação não encontrada.")
        return

    print("Atual: {}".format(ordem.resumo()))
    print("Pressione ENTER para manter cada valor.")
    tipo_operacao = _ler_texto_opcional("Novo tipo da missão/contrato: ")
    valor = _ler_valor("Nova recompensa (R$): ", permitir_vazio=True)

    print("\nStatus disponíveis:")
    for indice, status in enumerate(OrdemOperacao.STATUS_VALIDOS, 1):
        print("  [{}] {}".format(indice, status))
    escolha = _ler_texto_opcional("Novo status (número ou ENTER): ")
    novo_status = None
    if escolha:
        try:
            novo_status = OrdemOperacao.STATUS_VALIDOS[int(escolha) - 1]
        except (ValueError, IndexError):
            print("Status inválido; nenhuma alteração de status aplicada.")

    if tipo_operacao is None and valor is None and novo_status is None:
        print("Nenhuma alteração informada.")
        return
    try:
        ordem = central.editar_ordem(codigo, tipo_operacao, valor, novo_status)
    except (TypeError, ValueError) as erro:
        print("Erro: {}".format(erro))
        return
    print("Ordem atualizada: {}".format(ordem.resumo()))


def _mostrar_guia():
    print(
        "\n=== GUIA DE USO ===\n"
        "1. Cadastre um contrato informando mercenário, especialidade, "
        "missão e recompensa.\n"
        "2. Anote o código gerado (por exemplo, OP-001) para localizar "
        "a ordem depois.\n"
        "3. Use a opção 2 para listar as ordens desta sessão ou a opção 3 "
        "para buscar uma pelo código.\n"
        "4. Use a opção 4 para editar uma ordem. Pressione ENTER nos campos "
        "que deseja manter.\n"
        "\nStatus disponíveis: DISPONÍVEL, EM ANDAMENTO, CONCLUÍDA e CANCELADA.\n"
        "A recompensa deve ser um valor numérico não negativo; vírgula ou "
        "ponto pode ser usado como separador decimal.\n"
        "\nOs contratos ficam somente na memória: ao encerrar o programa, "
        "as ordens desta sessão são apagadas."
    )


def menu_principal():
    central = CentralOperacoes()
    while True:
        print(
            "\n=== CENTRAL DE CONTRATOS DE MERCENÁRIOS ===\n"
            "[1] Cadastrar contrato de operação\n"
            "[2] Listar ordens da sessão\n"
            "[3] Buscar ordem por código\n"
            "[4] Editar ordem\n"
            "[5] Guia de uso\n"
            "[0] Encerrar sessão\n"
        )
        try:
            opcao = input("Escolha uma opção: ").strip()
        except (EOFError, KeyboardInterrupt):
            opcao = "0"

        if opcao == "1":
            _nova_ordem(central)
        elif opcao == "2":
            print("\n=== Ordens da sessão ===")
            print(central.listar_ordens())
        elif opcao == "3":
            _buscar_ordem(central)
        elif opcao == "4":
            _editar_ordem(central)
        elif opcao == "5":
            _mostrar_guia()
        elif opcao == "0":
            print("Sessão encerrada. Os contratos não são salvos ao fechar o programa.")
            break
        else:
            print("Opção inválida. Escolha 0, 1, 2, 3, 4 ou 5.")


if __name__ == "__main__":
    menu_principal()
