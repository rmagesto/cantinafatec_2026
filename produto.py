# =============================
# ARQUIVO 1 - produto.py
# =============================

from datetime import datetime

class Produto:
    """
    Classe que representa um produto da cantina.
    """

    def __init__(self, nome, data_validade, preco_compra, preco_venda, quantidade):
        self.nome = nome
        self.data_validade = data_validade
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade = quantidade

    def reduzir_estoque(self, quantidade):
        if self.quantidade >= quantidade:
            self.quantidade -= quantidade
            return True
        return False

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def get_data_validade_obj(self):
        """
        Converte a data de validade (MM/AAAA) para objeto datetime
        """
        return datetime.strptime(self.data_validade, "%m/%Y")
