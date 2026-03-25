# =============================
# ARQUIVO 3 - pagamento.py
# =============================

class Pagamento:
    """
    Classe que representa um pagamento feito.
    """

    def __init__(self, nome, categoria, curso, valor, data_hora):
        self.nome = nome
        self.categoria = categoria
        self.curso = curso
        self.valor = valor
        self.data_hora = data_hora
