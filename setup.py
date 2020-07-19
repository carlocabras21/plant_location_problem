# 1. impostare qua i tipo di test che si vogliono fare

bilde 	= False		# 3,84 	secondi ad istanza, 220 istanze. tot: 14 minuti
chess	= False		# 0.85 	secondi ad istanza, 30  istanze. tot: 25 secondi
euclid 	= True		# 0.26 	secondi ad istanza, 30  istanze. tot: 9 secondi
fpp11 	= False		# 9		secondi ad istanza, 30  istanze. tot: 4 minuti 20 secondi
fpp17 	= False		# 10	minuti  ad istanza, 30  istanze. tot: 4 ore 45 minuti
gapa 	= False	 	# 51	secondi ad istanza, 30  istanze. tot: 26 minuti
gapb 	= False		# 140	secondi ad istanza, 30  istanze. tot: 70 minuti

# 2. LANCIARE crea_istanze_benchmark.py per impostare i file per cplex
# 3. eseguire plant_location_problem.mod su cplex

# 4. controllare i risultati lanciando controlla_ottimali_benchmark.py
# IMPOSTARE QUA che cosa mostrare nella stampa
controlla_collegamenti_diversi 				= True
stampa_collegamenti_diversi_costo_uguale 	= True # eseguito solo se controlla_collegamenti_diversi = True
stampa_collegamenti_diversi_costo_diverso 	= True # eseguito solo se controlla_collegamenti_diversi = True
controlla_fo_diverse 						= True
