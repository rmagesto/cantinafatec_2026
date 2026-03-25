import pickle
from estoque import Estoque
from produto import Produto
from pagamento import Pagamento
from venda import Venda
from datetime import datetime
from faker import Faker

fake = Faker()

class Sistema:

    def __init__(self):
        self.estoque = Estoque()
        self.vendas = []
        self.pagamentos = []

    def carregar_produtos_iniciais(self):
        self.estoque.adicionar_produto(Produto("Água", "06/2031", 1.00, 3.00, 12))
        self.estoque.adicionar_produto(Produto("Água com gás", "06/2028", 1.50, 3.50, 12))
        self.estoque.adicionar_produto(Produto("Refrigerante", "06/2028", 1.20, 3.00, 36))
        self.estoque.adicionar_produto(Produto("Suco", "06/2027", 0.80, 3.00, 24))
        self.estoque.adicionar_produto(Produto("Torcida", "12/2027", 2.10, 3.00, 60))
        self.estoque.adicionar_produto(Produto("Amendoim", "12/2026", 1.30, 3.00, 40))
        self.estoque.adicionar_produto(Produto("Pão de Mel", "12/2027", 1.80, 3.00, 30))
        self.estoque.adicionar_produto(Produto("Bombom", "01/2029", 0.70, 1.50, 50))

    def simular_venda_automatica(self):

        if len(self.estoque.produtos) == 0:
            return

        produto = fake.random_element(elements=self.estoque.produtos)
        quantidade = fake.random_int(min=1, max=3)

        if produto.reduzir_estoque(quantidade):

            valor_total = produto.preco_venda * quantidade

            pagamento = Pagamento(
                fake.name(),
                fake.random_element(elements=("Aluno", "Professor", "Servidor")),
                fake.random_element(elements=("IA", "ESG")),
                valor_total,
                datetime.now()
            )

            venda = Venda(produto, quantidade, pagamento)

            self.vendas.append(venda)
            self.pagamentos.append(pagamento)

            print("\n--- VENDA AUTOMÁTICA REALIZADA ---")
            print(f"Produto: {produto.nome}")
            print(f"Quantidade: {quantidade}")
            print(f"Valor total: R$ {valor_total:.2f}")

    def realizar_venda(self, nome_produto, quantidade):

        produto = self.estoque.buscar_produto(nome_produto)

        if produto is None:
            print("Produto não encontrado")
            return

        if produto.reduzir_estoque(quantidade):

            valor_total = produto.preco_venda * quantidade

            pagamento = Pagamento(
                fake.name(),
                fake.random_element(elements=("Aluno", "Professor", "Servidor")),
                fake.random_element(elements=("IA", "ESG")),
                valor_total,
                datetime.now()
            )

            venda = Venda(produto, quantidade, pagamento)

            self.vendas.append(venda)
            self.pagamentos.append(pagamento)

            print("Venda realizada com sucesso!")
        else:
            print("Estoque insuficiente")

    def salvar_dados(self):
        with open("dados.pkl", "wb") as f:
            pickle.dump(self, f)

    def carregar_dados(self):
        try:
            with open("dados.pkl", "rb") as f:
                return pickle.load(f)
        except:
            return self

    def relatorio_vendas(self):
        for v in self.vendas:
            print(f"Produto: {v.produto.nome} | Quantidade: {v.quantidade} | Valor: {v.pagamento.valor}")
