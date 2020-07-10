import random

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# modificare questi dati per cambiare le dimensioni del problema
N_UTENTI = 5
N_LOCAZIONI = 2
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *



# generazione vettore nome utenti, e.g. utenti = {"u0", "u1", ... };
utenti = "utenti = {"

for i in range(0, N_UTENTI):
	utenti += '"u' + str(i) + '", '
utenti = utenti[:-2]
utenti += '};\n'

print (utenti)
	
	
# generazione vettore nome locazioni, e.g. locazioni = {"l0", "l1"};
locazioni = "locazioni = {"

for i in range(0, N_LOCAZIONI):
	locazioni += '"l' + str(i) + '", '
locazioni = locazioni[:-2]
locazioni += '};\n\n'

print (locazioni)
	
	
# generazione vettore costo attivazione locazioni, e.g. costi_attivazione = [39, 41];
costi_attivazione = "costi_attivazione = ["

for i in range(0, N_LOCAZIONI):
	costi_attivazione += str(random.randint(1,50)) + ', '
costi_attivazione = costi_attivazione[:-2]
costi_attivazione += '];\n'

print (costi_attivazione)
	
	
# generazione vettore costo collegamento utenti - locazioni, e.g. costi_collegamento = [[22, 18], [11, 21] ... ];
costi_collegamento = "costi_collegamento = ["

for i in range(0, N_UTENTI):
	costi_collegamento += '['
	for i in range(0, N_LOCAZIONI):
		costi_collegamento += str(random.randint(1,50)) + ', '
	costi_collegamento = costi_collegamento[:-2]
	costi_collegamento += '], '
costi_collegamento = costi_collegamento[:-2]
costi_collegamento += '];\n'

print (costi_collegamento)

# scrittura su file
f = open("plant_location_problem.dat", "w")
f.write(utenti)
f.write(locazioni)
f.write(costi_attivazione)
f.write(costi_collegamento)
f.close()

	
