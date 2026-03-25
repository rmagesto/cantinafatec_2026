Desabilitado

# ================================
# PROGRAMA PRINCIPAL
# ================================

# Criando a cantina
cantina = Cantina()

# Criando alguns produtos
p1 = Produto("Torcida", 2.1, 3.0, "01/01", "01/06", 40)
p2 = Produto("Refrigerante", 1.5, 3.0, "01/01", "01/08", 60)
p3 = Produto("Agua", 1.0, 3.0, "01/01", "01/12", 24)
p4 = Produto("Agua com gás", 1.2, 3.5, "01/01", "01/12", 24)
p5 = Produto("Amendoim", 1.3, 3.0, "01/01", "01/04", 30)
p6 = Produto("Pão de mel", 1.2, 3.0, "01/01", "01/03", 30)
p7 = Produto("Suco", 0.8, 3.0, "01/01", "01/12", 24)
p8 = Produto("Bombom", 0.5, 1.5, "01/01", "01/12", 50)


# Adicionando produtos na cantina
cantina.adicionar_produto(p1)
cantina.adicionar_produto(p2)
cantina.adicionar_produto(p3)
cantina.adicionar_produto(p4)
cantina.adicionar_produto(p5)
cantina.adicionar_produto(p6)
cantina.adicionar_produto(p7)
cantina.adicionar_produto(p8)

# Mostrando estoque inicial
cantina.mostrar_estoque()

# Simulando uma venda
cantina.vender_produto(
    nome_produto="Torcida",
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
