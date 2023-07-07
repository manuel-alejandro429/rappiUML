from payment import Payment

class Transaccion (Payment):

    number= int
    cvv = int 
    date = []

    def __init__(self, ide, number, cvv, date):
        super().__init__(id)
        self.number = number
        self.cvv = cvv
        self.date = date
        

