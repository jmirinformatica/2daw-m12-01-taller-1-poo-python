from animal import Gos, Gat, Cangur, Porc
from granja import Granja

un_gos = Gos("Papitu")
print(un_gos)

un_gat = Gat("Marramiau")
print(un_gat)

un_cangur = Cangur("Jumpy")
print(un_cangur)

un_porc = Porc("Porki", 40)
print(un_porc)

granja = Granja("Felicitat")
granja.add_animal(un_gos)
granja.add_animal(un_gat)
granja.add_animal(un_cangur)
granja.add_animal(un_porc)

print(granja)


granja2 = Granja("Tristessa")
print(granja2)