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
 
 float d[locazioni] = ... ;
 float c[utenti][locazioni] = ... ;
 
 dvar float+ x[utenti][locazioni];
 dvar float+ y[locazioni];
 
 /*
minimize sum(j in alimenti) alimento[j].costo * x[j];
subject to {
	forall(i in valori_nutrizionali)
		vincolo_val_nutr_min:
			sum(j in alimenti) alimento[j].val_nutr_unitari[i] * x[j] >= val_nutr_min[i];
	forall(j in alimenti)
		vincolo_quant_max:
			x[j] <= alimento[j].quant_max;
}*/

minimize sum (j in locazioni) d[j]*y[j] + sum (i in utenti, j in locazioni) c[i][j]*x[i][j];
subject to {
	forall (i in utenti)
	  sum (j in locazioni) x[i][j] == 1;
	forall (i in utenti, j in locazioni)
	  x[i][j] <= y[j];
	// forall (i in users, j in plants)
	//   x[i][j] >= 0;			// vincolo ridondante visto che x è float+
	forall (j in locazioni)
	  y[j] <= 1;				// y[j] >= 0 omesso perché y è float+
}















