/*********************************************
 * OPL 12.7.0.0 Model
 * Author: carlo
 * Creation Date: 13/lug/2020 at 11:31:19
 *********************************************/

  
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


execute {
  //writeln("x= ",x);
  //writeln("y= ",y);
}