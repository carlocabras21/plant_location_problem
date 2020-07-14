# su windows, quindi python 3
# ATTENZIONE: sovrascrive plant_location_problem.dat

import os

# lista delle cartelli contenenti i file di benchmark BildeKrarup
cartelle = ["BildeKrarup/B","BildeKrarup/C","BildeKrarup/Dq/1","BildeKrarup/Dq/2", 
			"BildeKrarup/Dq/3","BildeKrarup/Dq/4","BildeKrarup/Dq/5","BildeKrarup/Dq/6", 
			"BildeKrarup/Dq/7","BildeKrarup/Dq/8","BildeKrarup/Dq/9","BildeKrarup/Dq/10", 
			"BildeKrarup/Eq/1","BildeKrarup/Eq/2","BildeKrarup/Eq/3","BildeKrarup/Eq/4", 
			"BildeKrarup/Eq/5","BildeKrarup/Eq/6","BildeKrarup/Eq/7","BildeKrarup/Eq/8", 
			"BildeKrarup/Eq/9","BildeKrarup/Eq/10"]

# inizializzazione vettore di stringhe contenente i file dei dati

# cartelle = ["BildeKrarup/B"] # per testing
		
for cartella in cartelle:
	files = os.listdir(cartella)
	
	# filtro i file che mi servono, scegliendo solo quelli dei dati grezzi
	filtered_files = [item for item in files if "opt" not in item \
											and "lst" not in item \
											and "dat" not in item \
											and "new" not in item]
	
	# ordino i dati in modo da avere i file ordinati come B1.1, B1.2, B1.3 [...] anziché B1.1, B1.10, B1.2
	sorted_files = sorted(filtered_files, key = lambda x: int(x.split(".")[1]))
	for file in sorted_files:
	
		print (file)
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
	
	
	
	
	
	
	
	
	
	