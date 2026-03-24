# ================================
# CLASSE PRODUTO (ESTOQUE)
# ================================

class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, validade, quantidade):
        # Aqui estamos criando os atributos do produto
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.validade = validade
        self.quantidade = quantidade

    def retirar_estoque(self, qtd):
        # Esse método diminui a quantidade no estoque
        if self.quantidade >= qtd:
            self.quantidade = self.quantidade - qtd
        else:
            print("Estoque insuficiente!")