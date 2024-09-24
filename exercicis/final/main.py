llibre1 = Llibre("99348977", "El mecanoscrit del 2n origen", "Manuel de Pedrolo", 340, False)
llibre2 = Llibre("78668734", "La Biblia", "San Pedro", 500, True)

# mostro el llibre1 per pantalla
llibre1.descripcio() 

biblioteca = Biblioteca("Armand Cardona", "Carrer Major 10")
biblioteca.add_llibre(llibre1)
biblioteca.add_llibre(llibre2)

# mostra el cataleg per pantalla, dos llibres
biblioteca.mostra_cataleg()

# Prova CSV
csv_file = FitxerCSV("./biblio.csv")
biblioteca.write_to_fitxer(csv_file)

nova_biblioteca1 = Biblioteca("Prova", "Sense adreça")
nova_biblioteca1.read_from_fitxer(csv_file)

# Prova JSON
json_file = FitxerJSON("./biblio.json")
biblioteca.write_to_fitxer(json_file)

nova_biblioteca2 = Biblioteca("Prova", "Sense adreça")
nova_biblioteca2.read_from_fitxer(json_file)

# Prova XML... igual
