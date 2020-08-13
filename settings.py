# 1. impostare qua i tipo di test che si vogliono fare

bilde 	= True		
chess	= True		
euclid 	= True		
fpp11 	= True		
fpp17 	= True		
gapa 	= True	 	
gapb 	= True		


# scegliere se lanciare la versione discreta (0) o continua (1)
cont = 0

# 2. LANCIARE crea_istanze_benchmark.py per impostare i file per cplex
# 3. eseguire plant_location_problem.mod su cplex

# 4. controllare i risultati lanciando controlla_ottimali_benchmark.py
# IMPOSTARE QUA che cosa mostrare nella stampa
controlla_collegamenti_diversi 				= True	# ATTENZIONE: stampa molte informazioni
stampa_collegamenti_diversi_costo_uguale 	= True	# eseguito solo se controlla_collegamenti_diversi = True
stampa_collegamenti_diversi_costo_diverso 	= True	# eseguito solo se controlla_collegamenti_diversi = True
controlla_fo_diverse 						= True

# valido nel caso continuo
stampa_valori_x_y = False
