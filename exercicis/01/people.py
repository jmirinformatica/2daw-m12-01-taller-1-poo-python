class People:
    def __init__(self, name, surname, age, favoritColor):
        self.name = name
        self.surname = surname
        self.age = age
        self.favoritColor = favoritColor
        self.malnoms = []

    #chanche the favotite color
    def set_favoritColor(self, favoritColor):
        self.favoritColor = favoritColor

    #append malnoms
    def add_malnom(self, malnom):
        afegit = True
        if malnom in self.malnoms:
            print(f"Ja té aquest malnom: {malnom}")
            afegit = False
        else:
            self.malnoms.append(malnom)
        return afegit

    #description
    def description(self):
        malnoms_str = ', '.join(self.malnoms) if self.malnoms else 'No té malnoms'
        return f"Nom: {self.name}, Cognoms: {self.surname}, Edat: {self.age}, Color preferit: {self.favoritColor}, Malnoms: {malnoms_str}"

p1 = People("Alfonso", "da Silva", 49, "verd")
print(p1.description())

p1.set_favoritColor("groc")
p1.add_malnom("El màquina")
p1.add_malnom("El màquina")
p1.add_malnom("Assamblador")

print(p1.description())

