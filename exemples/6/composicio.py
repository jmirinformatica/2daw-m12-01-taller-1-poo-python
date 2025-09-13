class Direccio:
    def __init__(self, carrer, ciutat, pais):
        self.carrer = carrer
        self.ciutat = ciutat
        self.pais = pais

    def __str__(self):
        return f"{self.carrer}, {self.ciutat}, {self.pais}"

class Persona:
    def __init__(self, nom, edat, carrer, ciutat, pais):
        self.nom = nom
        self.edat = edat
        self.direccio = Direccio(carrer, ciutat, pais)

    def __str__(self):
        return f"Nom: {self.nom}, Edat: {self.edat}, Direcció: {self.direccio}"

persona1 = Persona("Anna", 30, "Carrer Major, 1", "Barcelona", "Espanya")
persona2 = Persona("Joan", 25, "Avinguda Llibertat, 5", "Madrid", "Espanya")

print("-----")
print(persona1)
print("-----")
print(persona2)
