class Granja:
    def __init__(self, nom):
        self.nom = nom
        self.llista_animals = []

    def add_animal(self, animal):
        if animal in self.llista_animals:
            print("L'animal ja hi és a la llista")
            return False
        else:
            self.llista_animals.append(animal)

    def description(self):
        print(self)

    def __str__(self):
        granja_str = f"Granja {self.nom}"
        if self.llista_animals:
            granja_str = granja_str + " té els animals següents:"
            for a in self.llista_animals:
                granja_str += "\n\t" + str(a)
        else:
            granja_str = granja_str + " no té cap animal"

        return granja_str