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


# ================================
# CLASSE PAGAMENTO
# ================================

class Pagamento:
    def __init__(self, nome, categoria, curso, valor, data_hora):
        # Dados de quem pagou
        self.nome = nome
        self.categoria = categoria
        self.curso = curso
        self.valor = valor
        self.data_hora = data_hora


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


# ================================
# PROGRAMA PRINCIPAL
# ================================

# Criando a cantina
cantina = Cantina()

# Criando alguns produtos
p1 = Produto("Coxinha", 2.0, 5.0, "20/03", "25/03", 10)
p2 = Produto("Refrigerante", 3.0, 6.0, "20/03", "30/03", 5)

# Adicionando produtos na cantina
cantina.adicionar_produto(p1)
cantina.adicionar_produto(p2)

# Mostrando estoque inicial
cantina.mostrar_estoque()

# Simulando uma venda
cantina.vender_produto(
    nome_produto="Coxinha",
    quantidade=2,
    nome_cliente="João",
    categoria="Aluno",
    curso="IA",
    data_hora="24/03 10:00"
)

# Mostrando estoque depois da venda
cantina.mostrar_estoque()

# Mostrando relatório
cantina.relatorio_vendas()

