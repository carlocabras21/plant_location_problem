/*********************************************
 * OPL 12.7.0.0 Model
 * Author: carlo
 * Creation Date: 10/lug/2020 at 11:16:54
 *********************************************/

 /*
 Plant Location Problem
 n utenti, m locazioni ciascuno con un costo d_j di attivazione.
 Ogni utente i deve sostenere un costo c_ij per raggiungare la locazione j attivata a lui più vicina
 
 Obiettivo: minimizzare la somma dei costi fissi e di collegamento
 
 x_ij = {1 se l'utente j si collega alla locazione j; 0 altrimenti}
 y_j  = {1 se la locazione j viene attivata; 		  0 altrimenti}
 
 min { sum d_j*y_j + sum sum c_ij * x_ij }
 s.t. 
 	sum x_ij = 1, i in {1, ... , n}
 	x_ij <= y_j			// congruenza logica delle variabili x_ij e y_j
 	x_ij >= 0 intero
 	0 <= y_j <= 1
 	
 
 benchmark:
 http://resources.mpi-inf.mpg.de/departments/d1/projects/benchmarks/UflLib/packages.html
 */

/*
La cartella dei benchmark BildeKrarup è strutturata così:
BildeKrarup
|__ B
|__ B
|__ Dq
	|__ 1
	|__
	...
	|__ 10
|__ Eq
	|__ 1
	|__
	...
	|__ 10
|__ B

BildeKrarup/B
BildeKrarup/C
BildeKrarup/Dq/1
BildeKrarup/Dq/2
BildeKrarup/Dq/3
BildeKrarup/Dq/4
BildeKrarup/Dq/5
BildeKrarup/Dq/6
BildeKrarup/Dq/7
BildeKrarup/Dq/8
BildeKrarup/Dq/9
BildeKrarup/Dq/10
BildeKrarup/Eq/1
BildeKrarup/Eq/2
BildeKrarup/Eq/3
BildeKrarup/Eq/4
BildeKrarup/Eq/5
BildeKrarup/Eq/6
BildeKrarup/Eq/7
BildeKrarup/Eq/8
BildeKrarup/Eq/9
BildeKrarup/Eq/10
dove ogni cartella contiene 10 file con i costi e 1 con la soluzione ottimale

*/

{string} datFiles=...;

	
main {
	var source = new IloOplModelSource("plant_location_problem_sub.mod");
	var cplex = new IloCplex();
	var def = new IloOplModelDefinition(source);
	
	var f_times = new IloOplOutputFile("times_BildeKrarup.txt");
	var total_time = 0;
	
	for(var datFile in thisOplModel.datFiles){
			
		var opl  = new IloOplModel(def,cplex);
		
		var data = new IloOplDataSource(datFile);
			
		opl.addDataSource(data);
		opl.generate();
		
		if (cplex.solve()) {  
			opl.postProcess();
	     
			var f = new IloOplOutputFile(datFile + ".opt");
			
			// metodo estremamente inefficiente per recuperare il numero di
			// utenti e locazioni ma al momento è l'unica soluzione
			for (var i in opl.utenti);
			var n_utenti = parseInt(i) + 1;
			for (var j in opl.utenti);
			var n_locazioni = parseInt(j) + 1;
			
			// stampa a video di nome file e sue dimensioni
			writeln(datFile + ", " + n_utenti + " utenti e " + n_locazioni + " locazioni");
			
			// stampa a video dei risulati formattati come nei file originali:
			for (var i in opl.utenti){
				for (var j in opl.locazioni){
					if (opl.x[i][j] == 1){
						write(j + " ");		
						f.write(j + " ");
					}						
				}	
			}
			
			// stampa del valore obiettivo ottimale
			writeln(cplex.getObjValue());
			f.write(cplex.getObjValue());
			
			// stampa del tempo risolutivo
			var solvedTime = cplex.getSolvedTime();
			total_time += solvedTime;
			writeln(solvedTime);
			f_times.writeln(datFile + ", " + n_utenti + " utenti e " + n_locazioni + " locazioni" + 
							". Tempo di risoluzione: " + solvedTime + " s");
			
			writeln("");
			
			} 
		else 
			writeln("No solution");
		
		opl.end();
	}  

	f.close()
	
	f_times.writeln("\nTempo complessivo: " + total_time + " s");
	f_times.close();
}













