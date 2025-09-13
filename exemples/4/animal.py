class Animal:
    def __init__(self, nom):
        self.nom = nom

    def menja(self):
        print(f"{self.nom} està menjant")

    def dorm(self):
        print(f"{self.nom} està dormint")

    def corre(self):
        print(f"{self.nom} està corrent")

    def __str__(self):
        return f"Soc el/l'animal anomenat {self.nom}"

class Gos(Animal):
    pass

class Tortuga(Animal):
    def neda(self):
        print(f"{self.nom} està nedant")

    def corre(self):
        print(f"{self.nom} va corrent molt a poc a poc")

class Cavall(Animal):
    def corre(self):
        super().corre()
        print("... i va molt ràpid!")

    def __str__(self):
        desc = super().__str__()
        return desc + " i soc un cavall"
    
un_gos = Gos("Papitu")
un_gos.menja()
un_gos.dorm()
un_gos.corre()
print(un_gos)

una_tortuga = Tortuga("Pepa")
una_tortuga.menja()
una_tortuga.dorm()
una_tortuga.corre()
una_tortuga.neda()
print(una_tortuga)

un_cavall = Cavall("Ferdinand")
un_cavall.menja()
un_cavall.dorm()
un_cavall.corre()
print(un_cavall)

# polimorfisme
print("------------------------------------------------------------")
llista_animals = [un_gos, una_tortuga, un_cavall]
for animal in llista_animals:
    animal.corre()
