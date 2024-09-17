class Alumne:
    materias = ["Catalan", "Castellano", "Inglés", "Mates", "Tecnologia", "Física y Química"]
    alumnes_creats = []
    
    def __init__ (self, nom, edat):
        self.nom = nom
        self.edat = edat
        self.notes = {} # un diccionari buit
        Alumne.alumnes_creats.append(self)

    def descripcio(self):
        print(f"Nom: {self.nom}, Cognom: {self.edat} i Notes: {self.notes}")

    def nota_nova(self, asignatura, nota):
        if type(nota) == int:
            if asignatura in Alumne.materias and nota <= 10 and nota >= 0:
                # self.nota_nova_comprovat(asignatura, nota)
                self.notes[asignatura] = nota
            else:
                print("Assigatura o nota incorrecta")
        else:
            print("No has posat un número!")
    
    def nota_nova_np(self, asignatura, nota):
        if nota == "NP" and asignatura in Alumne.materias:
            # self.nota_nova_comprovat(asignatura, nota)
            self.notes[asignatura] = nota # és NP!
        else:
            print("No has afegit NP!")
        
    def nota_media(self):
        mitjana = -1
        cont = 0
        suma = 0
        for nota in self.notes:
            if self.notes[nota] != "NP":    
                suma = suma + self.notes[nota]
                cont += 1

        if cont == 0:
            print("No hi han notes per fer la mitjana")
        else:
            mitjana = suma / cont
            print(f"La mitjana del alumne {self.nom} es {mitjana}")
        return mitjana

    @classmethod
    def add_assig(cls, assignatura):
        if assignatura in cls.materias:
           print("La assignatura ja hi es")
        else:
            cls.materias.append(assignatura)

    @classmethod
    def del_assig(cls, assignatura):
        if assignatura in cls.materias:
            cls.materias.remove(assignatura)
            
            # Esborro les notes d'aquesta assignatura de tots els alumnes
            # si tenen alguna nota d'aquesta assignatura en concret, clar
            for un_alumne_qualsevol in cls.alumnes_creats:
                if assignatura in un_alumne_qualsevol.notes:
                    del un_alumne_qualsevol.notes[assignatura]

        else:
            print("La assignatura no hi es")
