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

    def exibir_detalhes(self):
        print("\n--- DETALHE DA VENDA ---")
        print(f"Produto: {self.produto.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Consumido por: {self.pagamento.nome}")
        print(f"Categoria: {self.pagamento.categoria}")
        print(f"Curso: {self.pagamento.curso}")
        print(f"Valor pago: R$ {self.pagamento.valor:.2f}")
        print(f"Data/Hora: {self.pagamento.data_hora}")
