from alumne import Alumne

alumne1 = Alumne("Said", 20)

alumne1.descripcio()

alumne1.nota_nova("Mates", 8)

alumne1.descripcio()

alumne1.nota_nova_np("Catalan", "NP")

alumne1.descripcio()

alumne1.nota_nova("Inglés", 5)

alumne1.nota_nova("Plastica", 10)

alumne1.nota_nova_np("Catalan", "NP")

alumne1.descripcio()

alumne1.nota_media()

alumne1.nota_nova_np("Mates", "8")
alumne1.nota_nova_np("Inglés", "NP")
alumne1.descripcio()
alumne1.nota_media()


Alumne.del_assig("Mates")
print(Alumne.materias)
alumne1.descripcio()


Alumne.del_assig("Tecnologia")
alumne1.descripcio()



# Alumne.canviar_assig("Programacion")

# Alumne.canviar_assig("Mates")

# print(Alumne.materias)

# alumne1.nota_media()