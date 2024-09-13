class Cotxe:
    def __init__(self, model, any, color, en_venda):
        self.model = model
        self.any = any
        self.color = color
        self.en_venda = en_venda
        self.quilometratge = 0

    def start(self):
        print(f"Cotxe {self.model} en marxa ")

    def stop(self):
        print(f"Cotxe {self.model} aturat")

    def descripcio(self):
        print("----------------------")
        print(f"Model:{self.model}")
        print(f"Any:{self.any}")
        print(f"Color:{self.color}")
        print(f"Quilometratge:{self.quilometratge}")
        # if (self.en_venda):
        #     print("En venda:SI")
        # else:
        #     print("En venda:NO")
        print(f"En venda:{'SI' if self.en_venda else 'NO'}")
        print("----------------------")

    def posa_en_venda(self):
        if (self.en_venda):
            print("Ja hi soc en venda")
        else:
            self.en_venda = True
            print(f"Cotxe {self.model} en venda!!!!")

    def augmenta_quilometratge(self, q):
        if (q < 0):
            print("De que vas estafador!")
        else:
            self.quilometratge = self.quilometratge + q

cotxe1 = Cotxe("Renault Megane", 2012, "verd", True)
cotxe2 = Cotxe("Seat Toledo", 1987, "vermell", False)
cotxe3 = Cotxe("Ford Fiesta", 1965, "groc", False)

cotxe1.descripcio()
cotxe1.augmenta_quilometratge(1000)
cotxe1.descripcio()
cotxe1.augmenta_quilometratge(-500)
cotxe1.descripcio()



# cotxe1.posa_en_venda()
# cotxe1.descripcio()

# cotxe1.descripcio()
# cotxe2.descripcio()
# cotxe3.descripcio()


# print(cotxe1.model)
# crea un segon cotxe i print els atributs
# crea un tercer cotxe i print els atributs
# mou la classe Cotxe a un fitxer cotxe.py
# mètodes start i stop generics i personalitzats
# mètode descriu
# mètode per posar-lo o no en venda

# llista de cotxes i mostro les descripcions de tots els cotxes


