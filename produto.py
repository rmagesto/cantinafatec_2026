# =============================
# ARQUIVO 1 - produto.py
# =============================

class Produto:
    """
    Classe que representa um produto da cantina.
    Ela armazena todas as informações necessárias para o controle de estoque.
    """

    def __init__(self, nome, data_validade, preco_compra, preco_venda, quantidade):
        # Nome do produto (string)
        self.nome = nome

        # Data de validade (string - simplificado)
        self.data_validade = data_validade

        # Preço de compra (float)
        self.preco_compra = preco_compra

        # Preço de venda (float)
        self.preco_venda = preco_venda

        # Quantidade em estoque (int)
        self.quantidade = quantidade

    def reduzir_estoque(self, quantidade):
        """
        Reduz a quantidade do produto no estoque
        """
        if self.quantidade >= quantidade:
            self.quantidade = self.quantidade - quantidade
            return True
        else:
            return False

    def adicionar_estoque(self, quantidade):
        """
        Aumenta a quantidade do produto no estoque
        """
        self.quantidade = self.quantidade + quantidade
