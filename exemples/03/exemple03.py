class Animal:

    def __init__(self, nom):
        self.nom = nom

    def menja(self):
        print(f"{self.nom} està menjant")

    def dorm(self):
        print(f"{self.nom} està dormint")

class Gos(Animal):
    pass

un_gos = Gos("Rex")
un_gos.menja()

# afegir Gat, Lleó
# afegir parla a cada classe
# herència multi nivell: afegir classe EsserViu amb mètode Respira
# herència múltiple: afegir classe Mascota amb mètode propietari
