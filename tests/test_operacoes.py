import unittest

from gerenciador import CentralOperacoes


class TestCentralOperacoes(unittest.TestCase):
    def setUp(self):
        self.central = CentralOperacoes()

    def criar_ordem(self):
        return self.central.criar_ordem(
            "Alex Silva", "Reconhecimento", "Escolta de comboio", 2500
        )

    def test_cria_ordem_com_codigo_e_guarda_dados_na_sessao(self):
        ordem = self.criar_ordem()

        self.assertRegex(ordem.codigo, r"^OP-\d{3,}$")
        self.assertIs(self.central.buscar_ordem(ordem.codigo.lower()), ordem)
        self.assertIn(ordem.resumo(), self.central.listar_ordens())
        self.assertEqual(ordem.mercenario.nome, "Alex Silva")

    def test_edita_tipo_recompensa_e_status(self):
        ordem = self.criar_ordem()

        self.central.editar_ordem(
            ordem.codigo, "Resgate", 3200, "EM ANDAMENTO"
        )

        self.assertEqual(ordem.tipo_operacao, "Resgate")
        self.assertEqual(ordem.valor, 3200)
        self.assertEqual(ordem.status, "EM ANDAMENTO")

    def test_rejeita_dados_invalidos_e_codigo_desconhecido(self):
        with self.assertRaises(ValueError):
            self.central.criar_ordem("", "Reconhecimento", "Escolta", 100)
        with self.assertRaises(ValueError):
            self.central.criar_ordem("Alex", "Reconhecimento", "Escolta", -1)
        with self.assertRaises(ValueError):
            self.central.editar_ordem("OP-999", valor=100)

        self.assertEqual(self.central.ordens, [])

    def test_edicao_invalida_nao_aplica_alteracao_parcial(self):
        ordem = self.criar_ordem()

        with self.assertRaises(ValueError):
            self.central.editar_ordem(ordem.codigo, "Resgate", -1)

        self.assertEqual(ordem.tipo_operacao, "Escolta de comboio")
        self.assertEqual(ordem.valor, 2500)


if __name__ == "__main__":
    unittest.main()
