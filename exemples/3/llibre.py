class Llibre:

    # Atribut de classe per emmagatzemar la llista de llibres
    llista_llibres = []

    def __init__(self, titol, isbn):
        if not Llibre.is_valid_isbn(isbn):
            raise ValueError("ISBN no vàlid")
        self.titol = titol
        self.isbn = isbn
        Llibre.llista_llibres.append(self)

    @staticmethod
    def is_valid_isbn(isbn):
        return len(isbn) == 13 and isbn.isdigit()

    @classmethod
    def mostrar_llista_llibres(cls):
        for llibre in cls.llista_llibres:
            print(f"Títol: {llibre.titol}, ISBN: {llibre.isbn}")

llibre1 = Llibre("El senyor dels anells", "9780261102385")
llibre2 = Llibre("La casa dels esperits", "9780451524935")
Llibre.mostrar_llista_llibres()

#llibre3 = Llibre("Cien años de soledad", "197803074") # ISBN no vàlid