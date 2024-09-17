class Animal:
    def __init__(self, nom):
        self.nom = nom

    def menja(self):
        print(f"{self.nom} està menjant")

    def dorm(self):
        print(f"{self.nom} està dormint")

class Gos(Animal):
    def parla(self):
        print("Guau guau")

class Gat(Animal):
    def parla(self):
        print("Miau miau")

un_gos = Gos("Rex")
un_gos.menja()
un_gos.parla()

un_gat = Gat("Fifi")
un_gat.dorm()
un_gat.parla()

llista_animals = [un_gos, un_gat]

for a in llista_animals:
    a.parla()

# herència multi nivell: afegir classe EsserViu amb mètode Respira
# herència múltiple: afegir classe Mascota amb mètode propietari
