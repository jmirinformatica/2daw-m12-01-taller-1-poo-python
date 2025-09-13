from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def nom(self):
        pass

    def start(self):
        print(f"El vehicle {self.nom()} està en marxa")

    def stop(self):
        print(f"El vehicle {self.nom()} s'ha aturat")

class Coche(Vehicle):
    def nom(self):
        return "Coche"
    
class Moto(Vehicle):
    def nom(self):
        return "Moto"

coche = Coche()
coche.start()
coche.stop()

moto = Moto()
moto.start()
moto.stop()

# error pq no es pot instanciar una classe abstracta
# vehicle = Vehicle()

