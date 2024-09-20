from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def parla(self):
        pass

    def menja(self):
        print(f"{self.nom} està menjant")

    def dorm(self):
        print(f"{self.nom} està dormint")

    def corre(self):
        return f"{self.nom} està corrent"

class Gos(Animal):
    def parla(self):
        print("Guau guau")

class Gat(Animal):
    def parla(self):
        print("Miau miau")

class Cangur(Animal):
    def parla(self):
        print("Cangu cangu")

    def corre(self):
        resposta = super().corre()
        nova_resposta = resposta + " i fa boing boing"
        return nova_resposta

class Porc(Animal):
    def __init__(self, nom, pes):
        super().__init__(nom) # soc un animal
        self.pes = pes        # amb atributs propis

    def parla(self):
        print("Oink oink")

# això dona error
# un_animal = Animal("Epi") 

# un_gos = Gos("Rex")
# un_gos.menja()
# un_gos.parla()

# un_gat = Gat("Fifi")
# un_gat.dorm()
# un_gat.parla()

# un_porc = Porc("Piggy", 40) # el proc pesa 40 quilograms

# un_gat = Gat("Fifi")
# print(un_gat.corre())

un_cangur = Cangur("Popito")
print(un_cangur.corre())


# llista_animals = [un_gos, un_gat, un_porc]

# for a in llista_animals:
#     a.parla()

# herència multi nivell: afegir classe EsserViu amb mètode Respira
# herència múltiple: afegir classe Mascota amb mètode propietari
