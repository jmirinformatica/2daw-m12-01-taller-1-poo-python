class Alumne:
    numero_alumnes = 0
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
        Alumne.numero_alumnes+=1;

a1 = Alumne("Alfonso", 49)
a2 = Alumne("Marta", 24)

print(Alumne.numero_alumnes)

# Nombre d'alumnes com a variable de classe

