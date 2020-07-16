# su windows, quindi python 3
# ATTENZIONE: sovrascrive plant_location_problem.dat

import os
from utils import *

# lista delle cartelli contenenti i file di benchmark 
lista_cartelle = get_folders_list()

# inizializzazione vettore di stringhe contenente i file dei dati
datFiles= "datFiles = [{"

# lista_cartelle = ["BildeKrarup/B"] # per testing

for cartelle in lista_cartelle:
	for cartella in cartelle:
		files = os.listdir(cartella)
		
		# filtro i file che mi servono, scegliendo solo quelli dei dati grezzi:
		# è un modo comodo per prendere il file una sola volta senza avere il
		# disturbo dell'estensione.
		filtered_files = [item for item in files if "opt" not in item \
												and "lst" not in item \
												and "dat" not in item \
												and "new" not in item]
		
		for file in filtered_files:
			
			if file + "_new" not in files:
			# crea il file solo se non esiste
			
				f = open(cartella + "/" + file, 'r') 
				
				# inizializzaione vettori dei dati
				f.readline()
				dimensioni  = f.readline()
				n_utenti    = int(dimensioni.split(" ")[1])
				n_locazioni = int(dimensioni.split(" ")[0])


				# generazione vettore nome utenti, e.g. utenti = {"0", "1", ... };
				utenti = "utenti = {"
				for i in range(0, n_utenti):
					utenti += '"' + str(i) + '", '
				utenti = utenti[:-2]
				utenti += '};\n'
					
					
				# generazione vettore nome locazioni, e.g. locazioni = {"0", "1"};
				locazioni = "locazioni = {"
				for i in range(0, n_locazioni):
					locazioni += '"' + str(i) + '", '
				locazioni = locazioni[:-2]
				locazioni += '};\n\n'

				
				# generazione vettori dei costi di attivazione e dei costi di collegamento
				costi_attivazione  = "costi_attivazione  = ["
				costi_collegamento = "costi_collegamento = "

				matrice_costi_collegamento = []
				for line in f.readlines():
					line = line.strip() # rimuovo i caratteri inutili di inizio e fine stringa
					line_splitted = line.split(" ")
					
					# il costo di attivazione si trova nella seconda posizione della linea
					costi_attivazione += line_splitted[1] + ', '
					
					# nel file ho per ogni locazione il costo di attivazione per ogni utente
					matrice_costi_collegamento += [[int (i) for i in  line_splitted[2:] ]]
				
				# faccio la trasposta della matrice perché mi serve l'ordine contrario,
				# ovvero per ogni utente voglio il costo di attivazione per la locazione
				trasposta = list(map(list, zip(*matrice_costi_collegamento)))
				costi_collegamento += str(trasposta) + ";"

				costi_attivazione = costi_attivazione[:-2]
				costi_attivazione += '];\n'

				
				# scrittura su file
				f = open(cartella + "/" + file + "_new", "w")
				
				f.write(utenti)
				f.write(locazioni)
				f.write(costi_attivazione)
				f.write(costi_collegamento)
				f.close()
				
				print (file + "_new creato ed aggiunto alla lista")
			
			else:
				print (file + "_new già esistente ed aggiunto alla lista")
				
			# aggiungi il file alla lista delle istanze da far analizzare a cplex
			datFiles += '"' + cartella + "/" + file + "_new" + '",'
	datFiles = datFiles[:-1] + '}, {'			
# scrittura file dei dati che serve a cplex
datFiles = datFiles[:-3] + '];'			
f = open("plant_location_problem.dat", "w")

tests= "tests = {"
for test in get_tests_list():
	tests += '"' + test + '",'
tests = tests[:-1] + '};'
f.write(tests)
f.write("\n")

f.write(datFiles)
f.write("\n")

f.close()





'''

# su windows, quindi python 3
# ATTENZIONE: sovrascrive plant_location_problem.dat

import os
from utils import *

# lista delle cartelle contenenti i file di benchmark 
cartelle = get_folders_list()

# inizializzazione vettore di stringhe contenente i file dei dati
datFiles= "datFiles = {"

# cartelle = ["BildeKrarup/B"] # per testing


for cartella in cartelle:
	files = os.listdir(cartella)
	
	# filtro i file che mi servono, scegliendo solo quelli dei dati grezzi:
	# è un modo comodo per prendere il file una sola volta senza avere il
	# disturbo dell'estensione.
	filtered_files = [item for item in files if "opt" not in item \
											and "lst" not in item \
											and "dat" not in item \
											and "new" not in item]
	
	for file in filtered_files:
		
		if file + "_new" not in files:
		# crea il file solo se non esiste
		
			f = open(cartella + "/" + file, 'r') 
			
			# inizializzaione vettori dei dati
			f.readline()
			dimensioni  = f.readline()
			n_utenti    = int(dimensioni.split(" ")[1])
			n_locazioni = int(dimensioni.split(" ")[0])


			# generazione vettore nome utenti, e.g. utenti = {"0", "1", ... };
			utenti = "utenti = {"
			for i in range(0, n_utenti):
				utenti += '"' + str(i) + '", '
			utenti = utenti[:-2]
			utenti += '};\n'
				
				
			# generazione vettore nome locazioni, e.g. locazioni = {"0", "1"};
			locazioni = "locazioni = {"
			for i in range(0, n_locazioni):
				locazioni += '"' + str(i) + '", '
			locazioni = locazioni[:-2]
			locazioni += '};\n\n'

			
			# generazione vettori dei costi di attivazione e dei costi di collegamento
			costi_attivazione  = "costi_attivazione  = ["
			costi_collegamento = "costi_collegamento = "

			matrice_costi_collegamento = []
			for line in f.readlines():
				line = line.strip() # rimuovo i caratteri inutili di inizio e fine stringa
				line_splitted = line.split(" ")
				
				# il costo di attivazione si trova nella seconda posizione della linea
				costi_attivazione += line_splitted[1] + ', '
				
				# nel file ho per ogni locazione il costo di attivazione per ogni utente
				matrice_costi_collegamento += [[int (i) for i in  line_splitted[2:] ]]
			
			# faccio la trasposta della matrice perché mi serve l'ordine contrario,
			# ovvero per ogni utente voglio il costo di attivazione per la locazione
			trasposta = list(map(list, zip(*matrice_costi_collegamento)))
			costi_collegamento += str(trasposta) + ";"

			costi_attivazione = costi_attivazione[:-2]
			costi_attivazione += '];\n'

			
			# scrittura su file
			f = open(cartella + "/" + file + "_new", "w")
			
			f.write(utenti)
			f.write(locazioni)
			f.write(costi_attivazione)
			f.write(costi_collegamento)
			f.close()
			
			print (file + "_new creato ed aggiunto alla lista")
		
		else:
			print (file + "_new già esistente ed aggiunto alla lista")
			
		# aggiungi il file alla lista delle istanze da far analizzare a cplex
		datFiles += '"' + cartella + "/" + file + "_new" + '",'

# scrittura file dei dati che serve a cplex
datFiles = datFiles[:-1] + '};'			
f = open("plant_location_problem.dat", "w")
f.write(datFiles)
f.write("\n")
f.write("tests = " + get_tests_string() + ";")
f.close()
'''


	
	
	
	
	
	
	
	
	
	