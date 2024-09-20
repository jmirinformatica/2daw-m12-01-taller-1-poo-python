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
    
    def __str__(self):
        return f"Soc el/l'animal anomenat {self.nom}"

class Gos(Animal):
    def parla(self):
        print("Guau guau")

    def __eq__(self, other):
        if isinstance(other, Gos) and self.nom == other.nom:
            return True
        else:
            return False
        
    def __str__(self):
        desc = super().__str__()
        return desc + " i soc un gos"

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


un_gos = Gos("Papitu")
print(un_gos)

un_altre_gos = Gos("Papitu")

un_altre_gat = Gat("Papitu")
print(un_altre_gat)

if un_gos == un_altre_gat:
    print("Son el mateix gos!")
else:
    print("Son gossos diferents")






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

# un_cangur = Cangur("Popito")
# print(un_cangur.corre())


# llista_animals = [un_gos, un_gat, un_porc]

# for a in llista_animals:
#     a.parla()

# herència multi nivell: afegir classe EsserViu amb mètode Respira
# herència múltiple: afegir classe Mascota amb mètode propietari
