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

cotxe1 = Cotxe("Renault Megane", 2012, "verd", True)
cotxe2 = Cotxe("Seat Toledo", 1987, "vermell", False)

cotxe1.start()
cotxe2.start()

cotxe2.stop()
cotxe1.stop()
