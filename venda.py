# =============================
# ARQUIVO 4 - venda.py
# =============================

class Venda:
    """
    Classe responsável por registrar uma venda.
    """

    def __init__(self, produto, quantidade, pagamento):
        self.produto = produto
        self.quantidade = quantidade
        self.pagamento = pagamento
