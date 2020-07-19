# su windows, quindi python 3

'''

'''


import os
from utils import *
total_instance_counter = 0
j = 0
f_log = open("log_cont.txt", "w")
for array_cartelle in get_folders_list():
	# la struttura delle liste di array di cartelle è la stessa spiegata in crea_istanze_benchmark
	
	current_test = get_tests_list()[j]
	
	# file dove salvo i risultati
	f = open("risultati/confronto_risultati_" + current_test + "_cont.txt", "w")
	
	# controllo tempi di calcolo totali
	f_times_disc = get_time_disc(current_test, -1)
	f_times_cont = get_time_cont(current_test, -1)
	
	stampa_video_file(current_test, f, f_log, 2)
	
	s = "tempo totale di calcolo nel caso discreto: " + str(f_times_disc) + " s"
	stampa_video_file(s, f, f_log, 1)
	
	s = "tempo totale di calcolo nel caso continuo: " + str(f_times_cont) + " s\n"
	stampa_video_file(s, f, f_log, 1)
	
	for cartella in array_cartelle:
		files = os.listdir(cartella)
		
		# filtro i file che mi servono, scegliendo solo quelli dei dati grezzi
		filtered_files = [item for item in files if "opt" not in item \
												and "lst" not in item \
												and "dat" not in item \
												and "new" not in item]
												
		file_counter = 0
		for file in filtered_files:
			total_instance_counter +=1  
			
			
			stampa_video_file(file, f, f_log, 1)
			
			# apro i file relativi alle soluzioni discrete e continue
			
			f_disc = open(cartella + "/" + file + "_new.opt", 'r') 		# soluzione discreta
			f_cont = open(cartella + "/" + file + "_new_cont.opt", 'r') # soluzione continua
			# i file contengono una lista di numeri dove l'i-esimo numero contiene la locazione a cui l'i-esimo
			# utente e' collegato. 
			# l'ultimo elemento e' il valore obiettivo ottimale
			
			# trasformo la riga in array
			riga_file_opt_disc = f_disc.readline().strip().split(" ")
			riga_file_opt_cont = f_cont.readline().strip().split(" ")
			
			# nelle colonne 0 a n-2 trovo i collegamenti ottimi, in n-1 il valore ottimale
			n = len(riga_file_opt_cont)
			
			'''
			if controlla_collegamenti_diversi:
				# scorro l'array fino al penultimo elemento, saltando cosi' il valore ottimale
				for i in range (0, n-1):
				
					# se la locazione i-esima e' stata assegnata ad un utente diverso da quello che ho trovato io
					if riga_file_opt_disc[i] != riga_file_opt_cont[i]:
					
						# controllo se il costo di collegamento e' lo stesso
						
						f_to_check = open(cartella + "/" + file, 'r')
						# per come e' costruito il file originale, devo
						# confrontare la colonna numero i+2 delle righe riga_file_opt_disc[i]+2 e riga_file_opt_cont[i]+2
						lines = f_to_check.readlines()
						costo_orig = lines[int(riga_file_opt_disc[i]) + 2].split(" ")[i+2]
						costo_nuov = lines[int(riga_file_opt_cont[i]) + 2].split(" ")[i+2]
						
						f_to_check.close()
						
						if costo_orig == costo_nuov:
							# collegamenti diversi ma dallo stesso costo
						
							if stampa_collegamenti_diversi_costo_uguale:
								# se hanno stesso costo, il mio errore e' "accettato"
								s = "    WARNING: l'utente " + str(i) + " collegato originariamente al " + riga_file_opt_disc[i] + \
											", nel mio al " + riga_file_opt_cont[i] + ". Costo collegamento UGUALE "
								# stampo a video e su file
								print (s)
								f.write(s + "\n")
								f_log.write(s + "\n")
						else:
							# collegamenti diversi e dal costo diverso
						
							if stampa_collegamenti_diversi_costo_diverso:
								# se hanno diverso costo, comunico il valore dei costi
								s = "    WARNING: l'utente " + str(i) + " collegato originariamente al " + riga_file_opt_disc[i] + \
											", nel mio al " + riga_file_opt_cont[i] + ". Costo collegamento DIVERSO: " + \
											"orig: " + costo_orig + ", nuov: " + costo_nuov
						
								# stampo a video e su file
								print (s)
								f.write(s + "\n")
								f_log.write(s + "\n")
			'''			
			if controlla_fo_diverse:			
				if riga_file_opt_disc[-1] != riga_file_opt_cont[-1]: # la f.o. si trova alla fine della riga
					# diversa f.o. ottimale
					s = "    DIVERSA f.o. ottimale" + ". disc: " + riga_file_opt_disc[-1] + ", cont: " + riga_file_opt_cont[-1]
					stampa_video_file(s, f, f_log, 1)
					
				else:
					# stessa f.o. ottimale
					s = "    f.o. ottimale uguale"
					stampa_video_file(s, f, f_log, 1)
			
			
			# controllo tempi di calcolo
			f_times_disc = get_time_disc(current_test, file_counter)
			f_times_cont = get_time_cont(current_test, file_counter)
			
			s = "	tempo di calcolo nel caso discreto: " + str(f_times_disc) + " s"
			stampa_video_file(s, f, f_log, 1)
			
			s = "	tempo di calcolo nel caso continuo: " + str(f_times_cont) + " s"
			stampa_video_file(s, f, f_log, 2)
			
			
			file_counter += 1	
	f.close()
	j += 1

s = str(total_instance_counter) + " istanze analizzate"
print (s)
f_log.write(s + "\n")
	
	
	
	
	