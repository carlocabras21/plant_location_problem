# su windows, quindi python 3

'''
Questo script confronta i risultati ottimali ottenuti da me con quelli forniti dal benchmark.
I file ottimali contengono una lista di numeri dove dal primo al penultimo indicano a quale locazione è collegato 
l'i-esimo utente; l'ultimo numero contiene il valore ottimale della funzione obiettivo.
Nel caso l'i-esimo utente sia collegato ad una locazione diversa, cerco nel file originale di benchmark il costo 
di collegamento e stampo a video se i collegamenti hanno costo uguale o diverso.
'''


import os
from utils import *
count = 0
j = 0
f_log = open("log.txt", "w")
for array_cartelle in get_folders_list():
	# la struttura delle liste di array di cartelle è la stessa spiegata in crea_istanze_benchmark
	
	# file dove salvo i risultati
	f = open("risultati/confronto_risultati_" + get_tests_list()[j] + ".txt", "w")
	
	for cartella in array_cartelle:
		files = os.listdir(cartella)
		
		# filtro i file che mi servono, scegliendo solo quelli dei dati grezzi
		filtered_files = [item for item in files if "opt" not in item \
												and "lst" not in item \
												and "dat" not in item \
												and "new" not in item]
		
		for file in filtered_files:
			count +=1 
			print (file)
			f.write(file + "\n")
			f_log.write(file + "\n")
			
			# apro i file relativi alle soluzioni ottimali
			f_orig = open(cartella + "/" + file + ".opt", 'r') 		# soluzioni fornite 
			f_nuov = open(cartella + "/" + file + "_new.opt", 'r') 	# soluzione calcolate da me
			# i file contengono una lista di numeri dove l'i-esimo numero contiene la locazione a cui l'i-esimo
			# utente e' collegato. 
			# l'ultimo elemento e' il valore obiettivo ottimale
			
			# trasformo la riga in array
			riga_file_opt_orig = f_orig.readline().strip().split(" ")
			riga_file_opt_nuov = f_nuov.readline().strip().split(" ")
			
			# nelle colonne 0 a n-2 trovo i collegamenti ottimi, in n-1 il valore ottimale
			n = len(riga_file_opt_nuov)
			
			if controlla_collegamenti_diversi:
				# scorro l'array fino al penultimo elemento, saltando cosi' il valore ottimale
				for i in range (0, n-1):
				
					# se la locazione i-esima e' stata assegnata ad un utente diverso da quello che ho trovato io
					if riga_file_opt_orig[i] != riga_file_opt_nuov[i]:
					
						# controllo se il costo di collegamento e' lo stesso
						
						f_to_check = open(cartella + "/" + file, 'r')
						# per come e' costruito il file originale, devo
						# confrontare la colonna numero i+2 delle righe riga_file_opt_orig[i]+2 e riga_file_opt_nuov[i]+2
						lines = f_to_check.readlines()
						costo_orig = lines[int(riga_file_opt_orig[i]) + 2].split(" ")[i+2]
						costo_nuov = lines[int(riga_file_opt_nuov[i]) + 2].split(" ")[i+2]
						
						f_to_check.close()
						
						if costo_orig == costo_nuov:
							# collegamenti diversi ma dallo stesso costo
						
							if stampa_collegamenti_diversi_costo_uguale:
								# se hanno stesso costo, il mio errore e' "accettato"
								s = "    WARNING: l'utente " + str(i) + " collegato originariamente al " + riga_file_opt_orig[i] + \
											", nel mio al " + riga_file_opt_nuov[i] + ". Costo collegamento UGUALE "
								# stampo a video e su file
								print (s)
								f.write(s + "\n")
								f_log.write(s + "\n")
						else:
							# collegamenti diversi e dal costo diverso
						
							if stampa_collegamenti_diversi_costo_diverso:
								# se hanno diverso costo, comunico il valore dei costi
								s = "    WARNING: l'utente " + str(i) + " collegato originariamente al " + riga_file_opt_orig[i] + \
											", nel mio al " + riga_file_opt_nuov[i] + ". Costo collegamento DIVERSO: " + \
											"orig: " + costo_orig + ", nuov: " + costo_nuov
						
								# stampo a video e su file
								print (s)
								f.write(s + "\n")
								f_log.write(s + "\n")
						
			if controlla_fo_diverse:			
				if riga_file_opt_orig[-1] != riga_file_opt_nuov[-1]: # la f.o. si trova alla fine della riga
					# diversa f.o. ottimale
					s = "    ERRORE diversa f.o. ottimale" + ". orig: " + riga_file_opt_orig[-1] + ", nuov: " + riga_file_opt_nuov[-1]
					print (s)
					f.write(s + "\n\n")
					f_log.write(s + "\n\n")
					
				else:
					# stessa f.o. ottimale
					s = "    f.o. ottimale uguale"
					print (s)
					f.write(s + "\n\n")
					f_log.write(s + "\n\n")

			print("")
	f.close()
	j += 1

s = str(count) + " istanze analizzate"
print (s)
f_log.write(s + "\n")
	
	
	
	
	