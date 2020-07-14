# su windows, quindi python 3

import os

# lista delle cartelli contenenti i file di benchmark BildeKrarup
cartelle = ["BildeKrarup/B","BildeKrarup/C","BildeKrarup/Dq/1","BildeKrarup/Dq/2", 
			"BildeKrarup/Dq/3","BildeKrarup/Dq/4","BildeKrarup/Dq/5","BildeKrarup/Dq/6", 
			"BildeKrarup/Dq/7","BildeKrarup/Dq/8","BildeKrarup/Dq/9","BildeKrarup/Dq/10", 
			"BildeKrarup/Eq/1","BildeKrarup/Eq/2","BildeKrarup/Eq/3","BildeKrarup/Eq/4", 
			"BildeKrarup/Eq/5","BildeKrarup/Eq/6","BildeKrarup/Eq/7","BildeKrarup/Eq/8", 
			"BildeKrarup/Eq/9","BildeKrarup/Eq/10"]


# cartelle = ["BildeKrarup/B"] # per testing

# file dove salvo i risultati
f = open("confronto_risultati.txt", "w")

# flag per capire se i miei risultati si possono ritenere corretti
errore_grave = False

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
				
		# apro i file relativi alle soluzioni ottimali
		f_orig = open(cartella + "/" + file + ".opt", 'r') 		# soluzioni fornite 
		f_nuov = open(cartella + "/" + file + "_new.opt", 'r') 	# soluzione calcolate da me
		# i file contengono una lista di numeri dove l'i-esimo numero contiene la locazione a cui l'i-esimo
		# utente è collegato. 
		# l'ultimo elemento è il valore obiettivo ottimale
		
		# trasformo la riga in array
		utenti_urig = f_orig.readline().strip().split(" ")
		utenti_nuov = f_nuov.readline().strip().split(" ")
		
		
		# controllo se i risultati ottenuti sono gli stessi
		risultati_uguali = True
		n = len(utenti_nuov)
		
		# scorro l'array fino al penultimo elemento, saltando così il valore ottimale
		for i in range (0, n-1):
		
			# se la locazione i-esima è stata assegnata ad un utente diverso da quello che ho trovato io
			if utenti_urig[i] != utenti_nuov[i]:
			
				# controllo se il costo di collegamento è lo stesso
				
				f_to_check = open(cartella + "/" + file, 'r')
				# per come è costruito il file originale, devo
				# confrontare la colonna numero i+2 delle righe utenti_urig[i]+2 e utenti_nuov[i]+2
				lines = f_to_check.readlines()
				costo_orig = lines[int(utenti_urig[i]) + 2].split(" ")[i+2]
				costo_nuov = lines[int(utenti_nuov[i]) + 2].split(" ")[i+2]
				
				f_to_check.close()
				
				if costo_orig == costo_nuov:
					# se hanno stesso costo, il mio errore è "accettato"
					s = file + ": collegamento DIVERSO ma costo UGUALE, l'utente " + str(i) + \
								" collegato originariamente al " + utenti_urig[i] + \
								", nel mio al " + utenti_nuov[i]
				else:
					# se hanno diverso costo, comunico il valore dei costi
					s = file + ": ERRORE, l'utente " + str(i) + " collegato originariamente al " + utenti_urig[i] + \
								", nel mio al " + utenti_nuov[i] + ". COSTO COLLEGAMENTO DIVERSO: " + \
								"orig: " + costo_orig + ", nuov: " + costo_nuov
					errore_grave = True
				
				# stampo a video e su file
				print (s)
				f.write(s + "\n")
				
				# flag per la stampa
				risultati_uguali = False
				
		if utenti_urig[-1] != utenti_nuov[-1]:
			# stampo a video e su file
			s = file + ": ERRORE diversa f.o. ottimale" + ". orig: " + utenti_urig[-1] + ", nuov: " + utenti_nuov[-1]
			print (s)
			f.write(s + "\n")
			
			# flag per la stampa
			risultati_uguali = False
			
			errore_grave = True
			
		if risultati_uguali:
			# stampo a video e su file
			s = file + ": ok, stessi risultati"
			print (s)
			f.write(s + "\n")
		
f.close()

if not errore_grave:
	print ("\nTutto ok!")
else:
	print ("\nERRORI nel calcolo")
	
	
	
	
	
	
	
	
	