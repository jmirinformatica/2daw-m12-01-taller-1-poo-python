from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def parla(self):
        pass

    def __eq__(self, other):
        # si son de la mateixa classe i tenen el mateix nom, són iguals
        if self.__class__.__name__ == other.__class__.__name__ and self.nom == other.nom:
            return True
        else:
            return False

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
        
    def __str__(self):
        desc = super().__str__()
        return desc + " i soc un gos"

class Gat(Animal):
    def parla(self):
        print("Miau miau")

    def __str__(self):
        desc = super().__str__()
        return desc + " i soc un gat"
    
class Cangur(Animal):
    def parla(self):
        print("Cangu cangu")

    def corre(self):
        resposta = super().corre()
        nova_resposta = resposta + " i fa boing boing"
        return nova_resposta
    
    def __str__(self):
        desc = super().__str__()
        return desc + " i soc un cangur"

class Porc(Animal):
    def __init__(self, nom, pes):
        super().__init__(nom) # soc un animal
        self.pes = pes        # amb atributs propis

    def parla(self):
        print("Oink oink")

    def __str__(self):
        desc = super().__str__()
        return desc + f" i soc un porc que peso {self.pes} quilograms"