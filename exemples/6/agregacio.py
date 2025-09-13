class Asssignatura:
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return self.nom

class Alumne:
    def __init__(self, nom):
        self.nom = nom
        self.assignatures = []

    def afegeix_assignatura(self, assignatura):
        self.assignatures.append(assignatura)

    def llista_assignatures(self):
        for assignatura in self.assignatures:
            print(assignatura)

alumne1 = Alumne("Marta")
alumne2 = Alumne("Pere")

assignatura1 = Asssignatura("Matemàtiques")
assignatura2 = Asssignatura("Física")
assignatura3 = Asssignatura("Química")

alumne1.afegeix_assignatura(assignatura1)
alumne1.afegeix_assignatura(assignatura2)

alumne2.afegeix_assignatura(assignatura1)
alumne2.afegeix_assignatura(assignatura3)

print("-----")
alumne1.llista_assignatures()
print("-----")
alumne2.llista_assignatures()   
