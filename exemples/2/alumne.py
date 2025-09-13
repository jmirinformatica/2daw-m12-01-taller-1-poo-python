class Alumne:
    
    # Nombre d'alumnes com a variable de classe
    nombre_alumnes = 0

    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
        Alumne.nombre_alumnes += 1

a1 = Alumne("Alfonso", 49)
a2 = Alumne("Marta", 24)

print(Alumne.nombre_alumnes)
