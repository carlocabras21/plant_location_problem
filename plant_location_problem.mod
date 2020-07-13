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

      for(var datFile in thisOplModel.datFiles){
	      var opl  = new IloOplModel(def,cplex);
	
	      var data = new IloOplDataSource(datFile);
	
	      opl.addDataSource(data);
	      opl.generate();
	
	      if (cplex.solve()) {  
	         opl.postProcess();
	         
	         // stampa il valore ottimale su file:
	         // var o=new IloOplOutputFile("res"+datFile+".txt");
	         // o.writeln("OBJ = " + cplex.getObjValue());
	         // o.close();
	         
	         // stampa il valore ottimale a video:
	         writeln("OBJ = " + cplex.getObjValue());
	      } 
	      else {
	         writeln("No solution");
	      }
	     opl.end();
    }  

    }













