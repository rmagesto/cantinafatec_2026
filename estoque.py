class Estoque:
    def __init__(self):
        # Lista interna de produtos
        self.produtos = []

    def adicionar_produto(self, produto):
        # Adiciona um produto ao estoque
        self.produtos.append(produto)

    def buscar_produto(self, nome):
        # Procura um produto pelo nome
        for p in self.produtos:
            if p.nome == nome:
                return p
        return None

    def listar_produtos(self):
        # Exibe todos os produtos
        for p in self.produtos:
            print(f"{p.nome} | Qtd: {p.quantidade} | Validade: {p.validade}")
