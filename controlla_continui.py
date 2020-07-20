# su windows, quindi python 3

'''
Questo script confronta i risultati continui con i risultati discreti ottenuti da me
'''


import os
from utils import *
total_instance_counter = 0
test_index = 0
f_log = open("log_cont.txt", "w")
for array_cartelle in get_folders_list():
	# la struttura delle liste di array di cartelle è la stessa spiegata in crea_istanze_benchmark
	
	current_test = get_tests_list()[test_index]
	
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
			total_instance_counter += 1  
			
			
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
			
			if controlla_fo_diverse:			
				if riga_file_opt_disc[-1] != riga_file_opt_cont[-1]: # la f.o. si trova alla fine della riga
					# diversa f.o. ottimale
					s = "    DIVERSA f.o. ottimale" + ". disc: " + riga_file_opt_disc[-1] + ", cont: " + riga_file_opt_cont[-1]
					stampa_video_file(s, f, f_log, 1)
				else:
					# stessa f.o. ottimale
					s = "    f.o. ottimale uguale: " + str(riga_file_opt_cont[-1])
					stampa_video_file(s, f, f_log, 1)
					
			if controlla_collegamenti_diversi:
				# nelle colonne 0 a n-2 trovo i collegamenti ottimi, in n-1 il valore ottimale
				n1 = len(riga_file_opt_disc)
				n2 = len(riga_file_opt_cont)
				
				soluzioni_diverse = False
				
				if n1 != n2:
					soluzioni_diverse = True
				else:
					for i in range(0, n1):
						if riga_file_opt_disc[i] != riga_file_opt_cont[i]:
							soluzioni_diverse = False
				
				if soluzioni_diverse:
					s = "    DIVERSA soluzione"
					stampa_video_file(s, f, f_log, 1)
				else:
					s = "    soluzione discreta UGUALE alla soluzione continua"
					stampa_video_file(s, f, f_log, 1)
						
			
			if stampa_valori_x_y:
			
				with open(cartella + "/" + file, 'r') as f_to_check:
					# per estrarre dopo il costo del collegamento utente-locazione
					lines = f_to_check.readlines()
				
			
				# recupero i vettori soluzione x e y dal file delle soluzioni continue
				x,y = get_x_y_from_cont_opt(cartella + "/" + file + "_new_cont.opt")
				
				# estraggo le dimensioni di x
				m = len(x)
				n = len(x[0])
				
				for i in range(0,m):
					for j in range (0,n):
						# per come e' costruito il file originale, per ottenere il costo del collegamento
						# utente-locazione devo estrarre la colonna numero i+2 dalla riga j+2 
						costo_colleg = int(lines[j+2].split(" ")[i+2])
						costo_attiva = int(lines[j+2].split(" ")[1])
						
						if x[i][j] > 0: # and x[i][j] < 1:
							# stampa info sul collegamento
							s = "	ut. " + str(i) + " -> loc. " + str(j) + " \t" + \
								"x[" + str(i) + "][" + str(j) + "] = " + '%.4f' % x[i][j] + "\t" + \
								"y[" + str(j) + "] = " + '%.4f' % y[j] + "\t\t" + \
								"costo_colleg = " + str(costo_colleg) + "\t" + \
								"costo_attiva = " + str(costo_attiva)
							stampa_video_file(s, f, f_log, 1)

			# controllo tempi di calcolo
			f_times_disc = get_time_disc(current_test, file_counter)
			f_times_cont = get_time_cont(current_test, file_counter)
			
			s = " tempo di calcolo nel caso discreto: " + str(f_times_disc) + " s"
			stampa_video_file(s, f, f_log, 1)
			
			s = " tempo di calcolo nel caso continuo: " + str(f_times_cont) + " s"
			stampa_video_file(s, f, f_log, 2)
			
			file_counter += 1	
			
	f.close()
	test_index += 1

s = str(total_instance_counter) + " istanze analizzate"
print (s)
f_log.write(s + "\n")
	
	
	
	
	