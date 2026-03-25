class Produto:
    def __init__(self, nome, preco_compra, preco_venda, validade, quantidade):
        # Nome do produto
        self.nome = nome
        
        # Preço que a cantina pagou
        self.preco_compra = preco_compra
        
        # Preço que será vendido
        self.preco_venda = preco_venda
        
        # Data de validade (string simples para facilitar)
        self.validade = validade
        
        # Quantidade disponível no estoque
        self.quantidade = quantidade

    def retirar_estoque(self, qtd):
        # Método para retirar produtos do estoque
        if self.quantidade >= qtd:
            self.quantidade -= qtd
            return True
        else:
            return False

    def adicionar_estoque(self, qtd):
        # Método para adicionar produtos ao estoque
        self.quantidade += qtd
