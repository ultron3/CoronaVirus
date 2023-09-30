Questo progetto mette in pratica tutto cio che ho imparato in due anni di Its.
Questo progetto ha lo scopo di analizzare i dati dei pazienti positivi e negativi di covid nei vari stati degli USA.

Come prima cosa creo il database su Mysql Worckbench. 
Scarico la  libreria pretty table, ho a disposizione  6 funzionalità:
- 1 select: stampo i dati in tabella
- 2 insert: inserisco i dati
- 3 delete: cancello i record inserendo il nome dello stato
- 4 plot: stampo il grafico metteendo a confronto positivi e negativi
- 5 linear regression: uguale al punto 4.
- 6 exit
- default opzione non valida.

Ho un file a parte  nominato migration.py dove faccio la migrazione dei dati da worckbench a postgresql version 16.
