class Cotxe:
    def __init__(self, model, any, color, en_venda):
        self.model = model
        self.any = any
        self.color = color
        self.en_venda = en_venda

    def start(self):
        print(f"Cotxe {self.model} en marxa ")

    def stop(self):
        print(f"Cotxe {self.model} aturat")

cotxe1 = Cotxe("Renault Megane", 2012, "verd", True)
cotxe2 = Cotxe("Seat Toledo", 1987, "vermell", False)

cotxe1.start()
cotxe2.start()

cotxe2.stop()
cotxe1.stop()

# print(cotxe1.model)
# crea un segon cotxe i print els atributs
# crea un tercer cotxe i print els atributs
# mou la classe Cotxe a un fitxer cotxe.py
# mètodes start i stop generics i personalitzats
# mètode descriu
# mètode per posar-lo o no en venda

# llista de cotxes i mostro les descripcions de tots els cotxes


