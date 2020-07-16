# 1. impostare qua i tipo di test che si vogliono fare

test1 = False
test2 = False

bilde 	= False		# 3,84 	secondi ad istanza, 220 istanze
chess	= False		# 0.85 	secondi ad istanza, 30  istanze
euclid 	= True		# 0.26 	secondi ad istanza, 30  istanze
fpp11 	= False		# 9		secondi ad istanza, 30  istanze
fpp17 	= False 	# 10	minuti  ad istanza, 30  istanze
gapa 	= False 	# 51	secondi ad istanza, 30  istanze
gapb 	= False		# 140	secondi ad istanza, 30  istanze
gapc 	= False 	# 40  	minuti  ad istanza. stoppato prima

# 2. LANCIARE crea_istanze_benchmark.py per impostare i file per cplex
# 3. eseguire plant_location_problem.mod su cplex



# 4. controllare i risultati lanciando controlla_ottimali_benchmark.py
# IMPOSTARE QUA che cosa mostrare nella stampa
controlla_collegamenti_diversi 				= True
stampa_collegamenti_diversi_costo_uguale 	= False
stampa_collegamenti_diversi_costo_diverso 	= True
controlla_fo_diverse 						= True
