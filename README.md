# Plant Location Problem
In questo elaborato presento il lavoro svolto per il corso di Decision Science, dove studio il cosiddetto Plant Location Problem, un problema appartente alla classe dei problemi NP-difficili.
Dopo aver scritto il modello matematico su CPLEX, l’ho prima testato su alcune istanze casuali create da me per poi testarlo su istanze di benchmark [3]. 

Le soluzioni ottimali ottenute su queste ultime istanze sono pressoché uguali a quelle riportate nei benchmark, tranne per un caso che differisce leggermente rispetto all’originale e per alcune soluzioni che nonostante avessero stesso valore ottimale, riportavano soluzioni diverse. Confronto poi i risultati con il corrispettivo rilassamento continuo, rimuovendo il vincolo di interezza delle variabili x e y, ottenendo (come ci si aspettava) tempi di risoluzione e f.o. inferiori. 

## Passi per eseguire il lavoro
1. impostare il lavoro su `settings.py`, scegliendo quali classi di istanze eseguire e quali confronti si vogliono effettuare tra i risultati ottenuti. Impostare `True`/`False` per quanto riguarda le classi dei benchmark da analizzare e che messaggi stampare a video;

2. lanciare `crea_istanze_benchmark.py` che provvederà a convertire le istanze di benchmark in istanze leggibili dal programma, impostando inoltre i vettori dei dati nel file `plant_location_problem.dat`;

3. lanciare da CPLEX il file `plant_location_problem.mod` che salverà i risultati su file di testo;

4. studiare i risultati lanciando `controlla_ottimali_benchmark.py` se vogliamo studiare i risultati discreti ottenuti da me confrontandoli con quelli forniti, o `controlla_continui.py` se vogliamo studiare i miei risultati nel caso discreto con il corrispettivo rilassamento continuo.
