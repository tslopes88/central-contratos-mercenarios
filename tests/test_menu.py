import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from main import menu_principal


class TestMenuPrincipal(unittest.TestCase):
    def test_opcao_guia_mostra_instrucoes_e_retorna_ao_menu(self):
        saida = StringIO()
        with patch("builtins.input", side_effect=["5", "0"]):
            with redirect_stdout(saida):
                menu_principal()

        texto = saida.getvalue()
        self.assertIn("[5] Guia de uso", texto)
        self.assertIn("=== GUIA DE USO ===", texto)
        self.assertIn("Use a opção 2 para listar", texto)
        self.assertIn("DISPONÍVEL, EM ANDAMENTO, CONCLUÍDA e CANCELADA", texto)
        self.assertIn("as ordens desta sessão são apagadas", texto)
        self.assertIn("Sessão encerrada.", texto)

    def test_opcao_invalida_lista_nova_opcao_de_guia(self):
        saida = StringIO()
        with patch("builtins.input", side_effect=["9", "0"]):
            with redirect_stdout(saida):
                menu_principal()

        self.assertIn("Escolha 0, 1, 2, 3, 4 ou 5.", saida.getvalue())


if __name__ == "__main__":
    unittest.main()
