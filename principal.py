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