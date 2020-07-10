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
 */
 
{string} utenti  = ... ;
{string} locazioni = ... ;
 
float costi_attivazione[locazioni] = ... ;
float costi_collegamento[utenti][locazioni] = ... ;
 
dvar int+ x[utenti][locazioni];
dvar int+ y[locazioni];
 


minimize sum (j in locazioni) costi_attivazione[j]*y[j] + sum (i in utenti, j in locazioni) costi_collegamento[i][j]*x[i][j];

subject to {

	forall (i in utenti)
	  sum (j in locazioni) x[i][j] == 1;
	  
	forall (i in utenti, j in locazioni)
	  x[i][j] <= y[j];
	  
	// forall (i in users, j in plants)
	//   x[i][j] >= 0;			// vincolo ridondante visto che x è int+
	
	forall (j in locazioni)
	  y[j] <= 1;				// y[j] >= 0 omesso perché y è int+
}















