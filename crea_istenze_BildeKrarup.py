# su windows, quindi python 3

import os

cartelle = ["BildeKrarup/B","BildeKrarup/C","BildeKrarup/Dq/1","BildeKrarup/Dq/2", 
			"BildeKrarup/Dq/3","BildeKrarup/Dq/4","BildeKrarup/Dq/5","BildeKrarup/Dq/6", 
			"BildeKrarup/Dq/7","BildeKrarup/Dq/8","BildeKrarup/Dq/9","BildeKrarup/Dq/10", 
			"BildeKrarup/Eq/1","BildeKrarup/Eq/2","BildeKrarup/Eq/3","BildeKrarup/Eq/4", 
			"BildeKrarup/Eq/5","BildeKrarup/Eq/6","BildeKrarup/Eq/7","BildeKrarup/Eq/8", 
			"BildeKrarup/Eq/9","BildeKrarup/Eq/10"]
			
datFiles= "datFiles = {"

#cartelle = ["BildeKrarup/B","BildeKrarup/C"]
		
for cartella in cartelle:
	for file in os.listdir(cartella):
		if "opt" not in file and "lst" not in file and "dat" not in file:
			print (file)
			
			f = open(cartella+"/"+file, 'r') 
		
			#f = open("test.txt", 'r') 
					
			dimensioni  = f.readlines()[1]
			n_utenti    = int(dimensioni.split(" ")[1])
			n_locazioni = int(dimensioni.split(" ")[0])


			# generazione vettore nome utenti, e.g. utenti = {"u0", "u1", ... };
			utenti = "utenti = {"

			for i in range(0, n_utenti):
				utenti += '"u' + str(i) + '", '
			utenti = utenti[:-2]
			utenti += '};\n'

			# print (utenti)
				
				
			# generazione vettore nome locazioni, e.g. locazioni = {"l0", "l1"};
			locazioni = "locazioni = {"

			for i in range(0, n_locazioni):
				locazioni += '"l' + str(i) + '", '
			locazioni = locazioni[:-2]
			locazioni += '};\n\n'

			# print (locazioni)

			costi_attivazione = "costi_attivazione = ["
			costi_collegamento = "costi_collegamento = "

			matrice_costi_collegamento = []
			f.seek(0)
			for line in f.readlines()[2:]:
				line = line.strip()
				#print (line)
				line_splitted = line.split(" ")
				#print (line_splitted)
				
				costi_attivazione += line_splitted[1] + ', '
					
				#costi_collegamento +=  str([int (i) for i in  line_splitted[2:] ]) + ','
				matrice_costi_collegamento += [[int (i.strip()) for i in  line_splitted[2:] ]]

			trasposta = list(map(list, zip(*matrice_costi_collegamento)))
			costi_collegamento += str(trasposta) + ";"

			costi_attivazione = costi_attivazione[:-2]
			costi_attivazione += '];\n'

			# print (costi_attivazione)
			# print (costi_collegamento)
				
			# scrittura su file
			f = open(cartella + "/" + file + ".dat", "w")
			#f = open("test.dat", "w")
			
			f.write(utenti)
			f.write(locazioni)
			f.write(costi_attivazione)
			f.write(costi_collegamento)
			f.close()
			
			datFiles += '"' + cartella + "/" + file + ".dat" + '",'

datFiles = datFiles[:-1] + '}'			
f = open("datFiles.txt", "w")
f.write(datFiles)
f.close()
	
	
	
	
	
	
	
	
	
	
	
	