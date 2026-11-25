"""Gerenciamento em memória dos contratos de operação."""

from models import Mercenario, OrdemOperacao


class CentralOperacoes:
    """Cria, consulta, lista e edita ordens durante a sessão."""

    def __init__(self):
        self._ordens = []

    @property
    def ordens(self):
        return list(self._ordens)

    def criar_ordem(self, nome_mercenario, especialidade, tipo_operacao, valor):
        mercenario = Mercenario(nome_mercenario, especialidade)
        ordem = OrdemOperacao(mercenario, tipo_operacao, valor)
        self._ordens.append(ordem)
        return ordem

    def buscar_ordem(self, codigo):
        if not isinstance(codigo, str):
            return None
        codigo = codigo.strip().upper()
        for ordem in self._ordens:
            if ordem.codigo == codigo:
                return ordem
        return None

    def listar_ordens(self):
        if not self._ordens:
            return "Nenhuma ordem de operação cadastrada nesta sessão."
        return "\n".join(ordem.resumo() for ordem in self._ordens)

    def editar_ordem(self, codigo, tipo_operacao=None, valor=None, status=None):
        ordem = self.buscar_ordem(codigo)
        if ordem is None:
            raise ValueError("Ordem '{}' não encontrada.".format(codigo))
        ordem.editar(tipo_operacao=tipo_operacao, valor=valor, status=status)
        return ordem
