class Fitxer:

    @staticmethod
    def creaFitxer(nom:str):
        if nom.endswith(".xml"): # te l'extensio .xml
            fitxer = FitxerXML(nom)
        elif nom.endswith(".csv"):
            fitxer = FitxerCSV(nom)
        elif nom.endswith(".json"):
            fitxer = FitxerJSON(nom)
        else:
            print("Format no reconegut")
            fitxer = None
        return fitxer

    def __init__(self, nom):
        self.nom = nom

    def write_llista(self, llista_llibre):
        pass

class FitxerCSV(Fitxer):
    def write_llista(self, llista_llibre):
        print("Aquí va el codi que recorre la llista i el fica en un CSV")

class FitxerJSON(Fitxer):
    def write_llista(self, llista_llibre):
        print("Aquí va el codi que recorre la llista i el fica en un JSON")

class FitxerXML(Fitxer):
    def write_llista(self, llista_llibre):
        print("Aquí va el codi que recorre la llista i el fica en un XML")

class Biblioteca:
    def __init__(self, nom):
        self.nom = nom
        self.llista_llibres = []

    # falta el codi per afegir llibres a la llista_llibres

    def write_to_fitxer(self, fitxer:Fitxer):
        fitxer.write_llista(self.llista_llibres)

# CODI DE PROVA
biblio = Biblioteca("Exemple 1")
fitxer = Fitxer.creaFitxer("biblioteca.json") # podia haver triat json o xml
biblio.write_to_fitxer(fitxer)
