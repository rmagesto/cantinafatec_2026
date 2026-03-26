# =============================
# ARQUIVO 2 - estoque.py
# =============================
class Estoque:

    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for p in self.produtos:
            print(f"{p.nome} | Validade: {p.data_validade} | Estoque: {p.quantidade}")

    def buscar_produto_fifo(self, nome):
        produtos_filtrados = [p for p in self.produtos if p.nome.lower() == nome.lower()]

        if not produtos_filtrados:
            return None

        produtos_ordenados = sorted(produtos_filtrados, key=lambda p: p.get_data_validade_obj())

        return produtos_ordenados[0]
