# =============================
# ARQUIVO 2 - estoque.py
# =============================

class Estoque:
    """
    Classe responsável por gerenciar todos os produtos.
    """

    def __init__(self):
        # Lista interna de produtos
        self.produtos = []

    def adicionar_produto(self, produto):
        # Adiciona um produto ao estoque
        self.produtos.append(produto)

    def listar_produtos(self):
        # Mostra todos os produtos
        for p in self.produtos:
            print(f"{p.nome} - Estoque: {p.quantidade}")

    def buscar_produto(self, nome):
        # Procura produto pelo nome
        for p in self.produtos:
            if p.nome == nome:
                return p
        return None
