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
