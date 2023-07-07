from account import Account 

class RappiTendero(Account): 
    vehiculo = str

    def __init__(self, nombre, email, documento, vehiculo):
        super().__init__(nombre, email, documento)
        self.vehiculo = vehiculo
           
