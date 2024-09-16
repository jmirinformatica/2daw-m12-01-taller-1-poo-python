class Alumne:
    # compartit entre tots els alumnes
    assignatures = ["Mates", "Física", "Llengua"]

    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
        self.notes = {} # diccionari on guardaré les notes d'aquest alumne
        
    def add_nota(self, assignatura, nota):
        pass

a1 = Alumne("Alfonso", 49)
a1.add_nota("Mates", 7)
a1.add_nota("Patata", 5)   # ha de mostrar un error
a1.add_nota("Física", -78) # ha de mostrar un error







