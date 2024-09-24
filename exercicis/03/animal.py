from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nom, color, es_manso):
        self.nom = nom
        self.color = color
        self.es_manso = es_manso

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
    
    def description(self):
        # mostro per pantalla el que retorna el mètode __str__
        print(self)
    
    def __str__(self):
        if self.es_manso:
            es_manso_str = "és manso"
        else:
            es_manso_str = "no és manso"
        return f"Soc el/l'animal anomenat {self.nom} de color {self.color} i que {es_manso_str}"

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
    def __init__(self, nom, color, es_manso, pes):
        super().__init__(nom, color, es_manso) # soc un animal
        self.pes = pes                         # amb atributs propis

    def parla(self):
        print("Oink oink")

    def __str__(self):
        desc = super().__str__()
        return desc + f" i soc un porc que peso {self.pes} quilograms"