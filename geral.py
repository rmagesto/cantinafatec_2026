DESABILITADO

# =========================
# ARQUIVO: sistema.py (PRINCIPAL)
# =========================

import pickle
from datetime import datetime
from faker import Faker

# Criando instâncias principais
estoque = Estoque()
vendas = []
fake = Faker('pt_BR')

# =========================
# CADASTRO INICIAL DE PRODUTOS
# =========================

# Criando produtos conforme solicitado
estoque.adicionar_produto(Produto("Água", 1.00, 3.00, "06/2031", 50))
estoque.adicionar_produto(Produto("Água com gás", 1.50, 3.50, "06/2028", 50))
estoque.adicionar_produto(Produto("Refrigerante", 1.20, 3.00, "06/2028", 50))
estoque.adicionar_produto(Produto("Suco", 0.80, 3.00, "06/2027", 50))
estoque.adicionar_produto(Produto("Torcida", 2.10, 3.00, "12/2027", 50))
estoque.adicionar_produto(Produto("Amendoim", 1.30, 3.00, "12/2026", 50))
estoque.adicionar_produto(Produto("Pão de Mel", 1.80, 3.00, "12/2027", 50))
estoque.adicionar_produto(Produto("Bombom", 0.70, 1.50, "01/2029", 50))


# =========================
# FUNÇÃO PARA REALIZAR VENDA
# =========================

def realizar_venda(nome_produto, quantidade):
    # Busca o produto no estoque
    produto = estoque.buscar_produto(nome_produto)

    if produto is None:
        print("Produto não encontrado!")
        return

    # Tenta retirar do estoque
    if not produto.retirar_estoque(quantidade):
        print("Estoque insuficiente!")
        return

    # Gera dados fake para o cliente
    total = 0

    for v in vendas:
        print(f"Produto: {v.produto} | Qtd: {v.quantidade} | Valor: {v.pagamento.valor}")
        total += v.pagamento.valor

    print(f"Total vendido: R$ {total}")


# =========================
# SALVAR DADOS (PICKLE)
# =========================

def salvar_dados():
    with open('dados.pkl', 'wb') as f:
        pickle.dump((estoque, vendas), f)

    print("Dados salvos!")


# =========================
# CARREGAR DADOS (PICKLE)
# =========================

def carregar_dados():
    global estoque, vendas

    try:
        with open('dados.pkl', 'rb') as f:
            estoque, vendas = pickle.load(f)
        print("Dados carregados!")
    except:
        print("Nenhum dado encontrado.")


# =========================
# MENU PRINCIPAL
# =========================

def menu():
    while True:
        print("\n--- SISTEMA CANTINA ---")
        print("1 - Listar produtos")
        print("2 - Realizar venda")
        print("3 - Relatório de vendas")
        print("4 - Salvar dados")
        print("5 - Carregar dados")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == '1':
            estoque.listar_produtos()

        elif opcao == '2':
            nome = input("Nome do produto: ")
            qtd = int(input("Quantidade: "))
            realizar_venda(nome, qtd)

        elif opcao == '3':
            relatorio_vendas()

        elif opcao == '4':
            salvar_dados()

        elif opcao == '5':
            carregar_dados()

        elif opcao == '0':
            break

        else:
            print("Opção inválida!")


# Inicia o sistema
menu()
