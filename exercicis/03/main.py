from animal import Gos, Gat, Cangur, Porc
from granja import Granja

un_gos = Gos("Papitu", "marró", True)
print(un_gos)

un_gat = Gat("Marramiau", "blanc", False)
print(un_gat)

un_cangur = Cangur("Jumpy", "gris", False)
print(un_cangur)

un_porc = Porc("Porki", "blau", True, 40)
print(un_porc)

granja = Granja("Felicitat")
granja.add_animal(un_gos)
granja.add_animal(un_gat)
granja.add_animal(un_cangur)
granja.add_animal(un_porc)

print(granja)

granja.write_to_csv("animals.csv")

granja2 = Granja("Tristessa")
print(granja2)

granja2.read_from_csv("animals.csv")
print(granja2)