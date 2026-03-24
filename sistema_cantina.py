# ================================
# CLASSE CANTINA (SISTEMA)
# ================================

class Cantina:
    def __init__(self):
        # Lista de produtos
        self.produtos = []

        # Lista de pagamentos
        self.pagamentos = []

    def adicionar_produto(self, produto):
        # Adiciona um produto na lista
        self.produtos.append(produto)

    def mostrar_estoque(self):
        # Mostra todos os produtos
        print("\n=== ESTOQUE ===")
        for p in self.produtos:
            print(p.nome, "- Quantidade:", p.quantidade)

    def vender_produto(self, nome_produto, quantidade, nome_cliente, categoria, curso, data_hora):
        # Procura o produto pelo nome
        for p in self.produtos:
            if p.nome == nome_produto:

                # Retira do estoque
                p.retirar_estoque(quantidade)

                # Calcula valor total
                valor_total = p.preco_venda * quantidade

                # Cria um pagamento
                pagamento = Pagamento(nome_cliente, categoria, curso, valor_total, data_hora)

                # Salva o pagamento
                self.pagamentos.append(pagamento)

                print("Venda realizada com sucesso!")
                return

        print("Produto não encontrado!")

    def relatorio_vendas(self):
        # Mostra todos os pagamentos
        print("\n=== RELATÓRIO DE VENDAS ===")
        for pag in self.pagamentos:
            print(pag.nome, "-", pag.valor, "-", pag.data_hora)