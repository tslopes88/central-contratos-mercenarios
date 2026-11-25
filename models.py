"""Modelos para a central de contratos de mercenários."""

from itertools import count
import math


class Mercenario:
    """Agente que pode receber contratos de operação."""

    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome do mercenário não pode ficar vazio.")
        self._nome = valor.strip()

    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("A especialidade não pode ficar vazia.")
        self._especialidade = valor.strip()


class OrdemOperacao:
    """Contrato de operação vinculado a um mercenário."""

    _gerador_codigo = count(1)
    STATUS_VALIDOS = ("DISPONÍVEL", "EM ANDAMENTO", "CONCLUÍDA", "CANCELADA")

    def __init__(self, mercenario, tipo_operacao, valor, status="DISPONÍVEL"):
        self.mercenario = mercenario
        self.tipo_operacao = tipo_operacao
        self.valor = valor
        self.status = status
        self._codigo = "OP-{:03d}".format(next(self._gerador_codigo))

    @property
    def codigo(self):
        return self._codigo

    @property
    def mercenario(self):
        return self._mercenario

    @mercenario.setter
    def mercenario(self, valor):
        if not isinstance(valor, Mercenario):
            raise TypeError("A ordem precisa estar vinculada a um mercenário.")
        self._mercenario = valor

    @property
    def tipo_operacao(self):
        return self._tipo_operacao

    @tipo_operacao.setter
    def tipo_operacao(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O tipo de operação não pode ficar vazio.")
        self._tipo_operacao = valor.strip()

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        try:
            valor = float(valor)
        except (TypeError, ValueError, OverflowError):
            raise ValueError("O valor da recompensa deve ser numérico.")
        if not math.isfinite(valor) or valor < 0:
            raise ValueError("O valor da recompensa deve ser finito e não negativo.")
        self._valor = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O status não pode ficar vazio.")
        valor = valor.strip().upper()
        if valor not in self.STATUS_VALIDOS:
            raise ValueError("Status inválido. Escolha: {}.".format(", ".join(self.STATUS_VALIDOS)))
        self._status = valor

    def editar(self, tipo_operacao=None, valor=None, status=None):
        """Aplica as alterações informadas sem deixar atualizações parciais."""
        anteriores = (self._tipo_operacao, self._valor, self._status)
        try:
            if tipo_operacao is not None:
                self.tipo_operacao = tipo_operacao
            if valor is not None:
                self.valor = valor
            if status is not None:
                self.status = status
        except (TypeError, ValueError):
            self._tipo_operacao, self._valor, self._status = anteriores
            raise

    def resumo(self):
        return (
            "{} | {} | Mercenário: {} ({}) | Recompensa: R$ {:.2f} | Status: {}"
        ).format(
            self.codigo,
            self.tipo_operacao,
            self.mercenario.nome,
            self.mercenario.especialidade,
            self.valor,
            self.status,
        )

    def __str__(self):
        return self.resumo()
