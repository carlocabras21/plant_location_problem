# su windows, quindi python 3

'''
Crea delle tabelle per ogni classe di istanze, riporta ogni istanza per riga. 
Indica per colonna il numero di utenti, di locazioni, 
i tempi di risoluzione del problema discreto, del rilassamento continuo e il loro gap percentuale.
'''

import os
from utils import *


f_log = open("log_tabelle.txt", "w")
test_index = 0
for array_cartelle in get_folders_list():
	# la struttura delle liste di array di cartelle è la stessa spiegata in crea_istanze_benchmark
	
	current_test = get_tests_list()[test_index]
	
	s = "\\begin{longtable}{|l|l|l|l|l|l|}" + "\n" + \
		"\\multicolumn{6}{c}" + "\n" + \
		"{{ \\tablename \\hspace{1pt} \\thetable{} }} \\\\" + "\n" + \
		"\\hline" + "\n" + \
		"\\multicolumn{6}{|c|}{\\textbf{ " + current_test + "}} \\\\" + "\n" + \
		"\\hline" + "\n" + \
		"\\textbf{Istanza} & \\textbf{n locazioni} & \\textbf{n utenti} & \\textbf{t. discreto} & \\textbf{t. continuo} & \\textbf{gap} \\\\" + "\n" + \
		"\\endfirsthead" + "\n" + \
		"\\multicolumn{6}{c}" + "\n" + \
		"{{ \\tablename \\hspace{1pt} \\thetable{} -- continuo della pagina precedente}} \\\\ \\hline" + "\n" + \
		"\\multicolumn{6}{|c|}{\\textbf{ " + current_test + "}} \\\\" + "\n" + \
		"\\hline" + "\n" + \
		"\\textbf{Istanza} & \\textbf{n locazioni} & \\textbf{n utenti} & \\textbf{t. discreto} & \\textbf{t. continuo} & \\textbf{gap} \\\\" + "\n" + \
		"\\endhead" + "\n" + \
		"\\hline" + "\n"

	stampa_video_file(s, False, f_log, 1)
	
	
	for cartella in array_cartelle:
		files = os.listdir(cartella)
		
		# filtro i file che mi servono, scegliendo solo quelli dei dati grezzi
		filtered_files = [item for item in files if "opt" not in item \
												and "lst" not in item \
												and "dat" not in item \
												and "new" not in item]
												
		file_counter = 0
		for file in filtered_files:
			# da qua estraggo il nome e il numero di utenti e locazioni
			# primo numero: locazioni, secondo numero: utentis
			
			# estraggo nome e dimensioni problema
			with open(cartella + "/" + file, 'r') as f: 
				lines = f.readlines()
			n_locazioni, n_utenti = lines[1].split()[0:2]
			
			# estraggo f.o. ottimale caso discreto
			with open(cartella + "/" + file + "_new.opt", 'r') as f:
				fo_disc = f.readline().split()[-1]
			
			# estraggo f.o. ottimale caso continuo
			with open(cartella + "/" + file + "_new_cont.opt", 'r') as f: 
				fo_cont = f.readline().split()[-1]
			
			# calcolo il gap percentuale
			gap = (float(fo_disc) - float(fo_cont))/float(fo_disc)
			
			# estraggo tempi di calcolo
			time_disc = get_time(current_test, file, is_cont=False)
			time_cont = get_time(current_test, file, is_cont=True)

			
			s = file.replace("_","\_")+" & " +n_locazioni+" & " +n_utenti+" & " +str(time_disc)+" s & " +str(time_cont)+" s & " +"%.6f"%round(gap, 6)+" \\\\ \\hline"
			stampa_video_file(s, False, f_log, 1)
			
			
			
			file_counter += 1
	
	test_index += 1
	
	s = "\\caption{Tabella dei risultati ottenuti dalle istanze " + current_test + ".}" + "\n" + \
		"\\label{tab:" + current_test + "}" + "\n" + \
		"\\end{longtable}" + "\n" 
	stampa_video_file(s, False, f_log, 1)
	
	