from animal import Gos, Gat, Cangur, Porc

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
            return True

    def description(self):
        # mostro per pantalla el que retorna el mètode __str__
        print(self)

    def write_to_csv(self, csv_file_path):
        output = open(csv_file_path, "w")
        output.write("Tipus,Nom,Color,Es manso,Pes\n")
        for animal in self.llista_animals:
            es_manso_str = "si" if animal.es_manso else "no"
            pes_str = animal.pes if animal.__class__.__name__ == "Porc" else ""
            output.write(f"{animal.__class__.__name__},{animal.nom},{animal.color},{es_manso_str},{pes_str}\n")
        output.close()

    def read_from_csv(self, csv_file_path):
        input = open(csv_file_path, "r")
        input.readline() # descarto la primera línia
        for line in input:
            parts = line.strip().split(",")

            tipus = parts[0]
            nom = parts[1]
            color = parts[2]
            es_manso = parts[3] == "si"

            if tipus == "Gos":
                animal = Gos(nom, color, es_manso)
            elif tipus == "Gat":
                animal = Gat(nom, color, es_manso)
            elif tipus == "Cangur":
                animal = Cangur(nom, color, es_manso)
            elif tipus == "Porc":
                pes = int(parts[4])
                animal = Porc(nom, color, es_manso, pes)
      
            self.add_animal(animal)

    def __str__(self):
        granja_str = f"Granja {self.nom}"
        if self.llista_animals:
            granja_str = granja_str + " té els animals següents:"
            for a in self.llista_animals:
                granja_str += "\n\t" + str(a) # str(a) és com crida al mètode __str__ de la classe Animal
        else:
            granja_str = granja_str + " no té cap animal"

        return granja_str