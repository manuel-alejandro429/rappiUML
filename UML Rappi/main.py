from account import Account
from rappiTendero import RappiTendero
from comprador import Comprador
from tiendas import Tiendas
from cash import Cash
from transaccion import Transaccion


if __name__ =="__main__":

    #rappiTendero

    rapi1 = RappiTendero("moto","Duford","duford@gmail.com0","136317")
    rapi1.ubicacion = "CALLE 48 #5-134"

    print(vars(rapi1))
    print("\n")

    #comprador

    comprador1 = Comprador("ManuelGaston", "gaton.com", "1324462556674")
    print(vars(comprador1))
    print("\n")

    #tienda

    falabellaTienda = Tiendas("falabella", "falabella.outlook", "8603")
    print(vars(falabellaTienda))
    print("\n")

    #Metodos de pago

    #Cash

    pagoEfectivo1 = Cash(55)
    print(vars(pagoEfectivo1))
    print("\n")

    #transacción

    pagoTarjeta1 = Transaccion(55, 123, 55, [34,23,23,2,53])
    print(vars(pagoTarjeta1))
    print("\n")    







  
