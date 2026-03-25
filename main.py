# =============================
# ARQUIVO 6 - main.py (EXECUTÁVEL)
# =============================

# Importa todas as classes
from produto import Produto
from estoque import Estoque
from pagamento import Pagamento
from venda import Venda
from sistema import Sistema

# Cria o sistema
sistema = Sistema()

# Carrega dados salvos (se existir)
sistema = sistema.carregar_dados()

# Se for a primeira vez, carrega produtos
if len(sistema.estoque.produtos) == 0:
    sistema.carregar_produtos_iniciais()

# Menu simples
while True:
    print("\n1 - Listar produtos")
    print("2 - Realizar venda")
    print("3 - Relatório de vendas")
    print("4 - Salvar e sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        sistema.estoque.listar_produtos()

    elif opcao == "2":
        nome = input("Nome do produto: ")
        qtd = int(input("Quantidade: "))
        sistema.realizar_venda(nome, qtd)

    elif opcao == "3":
        sistema.relatorio_vendas()

    elif opcao == "4":
        sistema.salvar_dados()
        print("Dados salvos!")
        break

    else:
        print("Opção inválida")
        
