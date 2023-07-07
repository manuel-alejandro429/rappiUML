from account import Account

class Tiendas(Account) :
    stock = []

    def __init__(self, nombre, email, documeto):
        super().__init__(nombre, email, documeto)
