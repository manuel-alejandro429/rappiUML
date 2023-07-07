
from account import Account

class Comprador(Account):
    pedido = []

    def __init__(self, nombre, email, documento):
        super().__init__(nombre, email, documento)



