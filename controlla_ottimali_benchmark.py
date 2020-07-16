# su windows, quindi python 3

import os
from utils import *

# lista delle cartelli contenenti i file di benchmark 
cartelle = get_folders_list()


# cartelle = ["BildeKrarup/B"] # per testing

# file dove salvo i risultati
# f = open("risultati/confronto_risultati_" + get_tests_list() + ".txt", "w")

# lista delle cartelli contenenti i file di benchmark 
lista_cartelle = get_folders_list()

lista_test = get_tests_list()

# flag per capire se i miei risultati si possono ritenere corretti
errore_grave = False

j = 0
for cartelle in lista_cartelle:

	# file dove salvo i risultati
	f = open("risultati/confronto_risultati_" + lista_test[j] + ".txt", "w")
	print("risultati/confronto_risultati_" + lista_test[j] + ".txt")
	for cartella in cartelle:
		files = os.listdir(cartella)
		
		# filtro i file che mi servono, scegliendo solo quelli dei dati grezzi
		filtered_files = [item for item in files if "opt" not in item \
												and "lst" not in item \
												and "dat" not in item \
												and "new" not in item]
		
		for file in filtered_files:
			print (file)
			f.write(file + "\n")
			
			# apro i file relativi alle soluzioni ottimali
			f_orig = open(cartella + "/" + file + ".opt", 'r') 		# soluzioni fornite 
			f_nuov = open(cartella + "/" + file + "_new.opt", 'r') 	# soluzione calcolate da me
			# i file contengono una lista di numeri dove l'i-esimo numero contiene la locazione a cui l'i-esimo
			# utente e' collegato. 
			# l'ultimo elemento e' il valore obiettivo ottimale
			
			# trasformo la riga in array
			utenti_urig = f_orig.readline().strip().split(" ")
			utenti_nuov = f_nuov.readline().strip().split(" ")
			
			
			# controllo se i risultati ottenuti sono gli stessi
			risultati_uguali = True
			n = len(utenti_nuov)
			
			if controlla_collegamenti_diversi:
				# scorro l'array fino al penultimo elemento, saltando cosi' il valore ottimale
				for i in range (0, n-1):
				
					# se la locazione i-esima e' stata assegnata ad un utente diverso da quello che ho trovato io
					if utenti_urig[i] != utenti_nuov[i]:
					
						# controllo se il costo di collegamento e' lo stesso
						
						f_to_check = open(cartella + "/" + file, 'r')
						# per come e' costruito il file originale, devo
						# confrontare la colonna numero i+2 delle righe utenti_urig[i]+2 e utenti_nuov[i]+2
						lines = f_to_check.readlines()
						costo_orig = lines[int(utenti_urig[i]) + 2].split(" ")[i+2]
						costo_nuov = lines[int(utenti_nuov[i]) + 2].split(" ")[i+2]
						
						f_to_check.close()
						
						if costo_orig == costo_nuov:
							if stampa_collegamenti_diversi_costo_uguale:
								# se hanno stesso costo, il mio errore e' "accettato"
								s = "    WARNING: l'utente " + str(i) + " collegato originariamente al " + utenti_urig[i] + \
											", nel mio al " + utenti_nuov[i] + ". Costo collegamento UGUALE "
								# stampo a video e su file
								print (s)
								f.write(s + "\n")
						else:
							if stampa_collegamenti_diversi_costo_diverso:
								# se hanno diverso costo, comunico il valore dei costi
								s = "    WARNING: l'utente " + str(i) + " collegato originariamente al " + utenti_urig[i] + \
											", nel mio al " + utenti_nuov[i] + ". Costo collegamento DIVERSO: " + \
											"orig: " + costo_orig + ", nuov: " + costo_nuov
						
								# stampo a video e su file
								print (s)
								f.write(s + "\n")
						
						# flag per la stampa
						risultati_uguali = False
			if controlla_fo_diverse:			
				if utenti_urig[-1] != utenti_nuov[-1]:
					# stampo a video e su file
					s = "    ERRORE diversa f.o. ottimale" + ". orig: " + utenti_urig[-1] + ", nuov: " + utenti_nuov[-1]
					print (s)
					f.write(s + "\n\n")
					
					# flag per la stampa
					risultati_uguali = False
				else:
					s = "    f.o. ottimale uguale"
					print (s)
					f.write(s + "\n\n")
					
			# if risultati_uguali:
				# stampo a video e su file
				# s = file + ": ok"
				# print (s)
				# f.write(s + "\n")
			print("")
	f.close()
	j += 1
	
	
	
	
	
	
	