=========================================================================
ISTRUZIONI per il PROGETTO DI RECUPERO PYTHON aa 2023/24
========================================================================
Il progetto prevede la realizzazione di un progetto Scratch e di un progetto Python
che realizzano la gestione di un bancomat, come specificato nel file ProgettoRecupero_aa23_24.pdf.

Come procedere:
(1) realizzare il progetto Scratch seguendo le istruzione ed esportare il bancomat.sb3.
(2) realizzare (nei file bancomat.py e utenti.py) i metodi richiesti seguendo le indicazioni
    dei commenti in corrispondenza di ciascun metodo e testarli opportunamente.
(3) eseguire i test nel file main.py fornito dai docenti (senza modificarlo)
    per effettuare questo test i file main.py, testMy.py, bancomat.py e utenti.py
    si devono trovare nella stessa cartella
(4) realizzare (nel file gui.py) la GUI come specificato nel file di istruzioni (oltre a questo README)
    e testarla opportunamente
(5) assicurarsi che tutti i test vengono superati e viene stampato il messaggio finale 
    che invita alla consegna
(6) scrivere una breve relazione che contiene la spiegazione della struttura logica delle due parti:
    Scratch (spirite,logica,interazione) e Python (file, classi, metodi); le motivazioni delle scelte 
    implementative; e una guida utente che spiega come utilizzare il software.
(7) preparare un archivio zip con i file (bancomat.sb3, bancomat.py, utenti.py, gui.py e relazione in pdf)
    per la consegna inserendo nome cognome e contatti dei componenti del gruppo nell'intestazione.
(8) consegnare su Moodle l'archivio (ed eventuali file aggiuntivi -- vedi istruzioni sotto)
    entro la data dell'appello di cui si vuole svolgere l'orale.

------------------------------------------------
Cosa contiene questa il compito
------------------------------------------------

ProgettoRecupero_aa23_24.pdf	: file contenente la descrizione del progetto

utenti.py 	            	    : file che contiene la definizione della gerarchia di classi per la gestione degli utenti 

bancomat.py 	            	: file che contiene la definizione dei metodi da realizzare

gui.py                          : file in cui inserire il codice della GUI, con gli import necessari per usare il bancomat

main.py, testMy.py              : file per i test finali (NON MODIFICARE)

README			                : questo file


========================================================================
ALCUNI SUGGERIMENTI per la realizzazione dell'assegnamento
========================================================================

Conviene realizzare le funzioni richiest seguendo le specifiche nei commenti e
analizzando la struttura dei test del file main.py che usano un aversione aggiornata 
della testEqual() usata durante il corso e disponibile in testMy.py.
Durante lo sviluppo e' consigliato non usare immediatamente i test in main.py
per non avere risultati complessi e di difficile interpretazione. Consigliamo invece
di ispiraresi a main.py per creare dei test propri che permettano di
verificare il funzionamento delle funzioni passo passo durante la realizzazione
secondo il principio del debug incrementale spesso citato a lezione.

Quando si è ragionevolmente sicuri della correttezza di quanto realizzato, passare a test finali
in main.py.
Questi ultimi test verificano le funzionalità basilari delle funzioni richieste stampando
il risultato a video. Se tutti i test sono superati lo studente viene invitato
a effettuare la consegna altrimenti si stampa il numero di test falliti.

E' possibile aggiungere test, che vanno realizzati in un file di nome "moreTest.py"
da consegnare insieme a archivio.py.

Se lo si desidera è possibile definire funzioni ausiliarie per la realizzazione delle 
funzioni richieste o aggiungere nuove funzioni, tuttavia
le nuove funzioni devono essere fornite specifiche chiare
del funzionamento (nei commenti) e test di funzionamento adeguati
 (nel file "moreTest.py")

 ========================================================================
 GUI - Interfaccia grafica utente
 ========================================================================

 Deve essere realizzata un'interfaccia grafica usando il modulo tkinter che permetta almeno di
    1. deve essere richiesto il login dell’utente;
    2. deve essere richiesta quale operazione vuole essere effettuata fra prelievo,
        deposito e trasferimento ad altro conto corrente;
    3. devono essere richieste le informazioni per svolgere l’operazione;
    4. in caso di errori, a schermo devono essere mostrati i messaggi di errore
        definiti nella classe Bancomat;
    5. in caso di successo, deve essere mostrato un messaggio di riuscita dell’operazione
        e salvare su file il nuovo stato del Bancomat;
    6. dopo alcuni secondi, deve essere richiesto il login per ripartire dal punto (1).
 
    L'aspetto dell'interfaccia viene deciso dallo studente.

 NOTE IMPORTANTI: LEGGERE ATTENTAMENTE
---------------------------------------

1) tutti gli elaborati verranno confrontati fra di loro con tool automatici
   per stabilire eventuali situazioni di PLAGIO. Gli elaborato sono
   ragionevolmente simili verranno scartati.

2) Chi in sede di orale risulta palesemente non essere l'autore del software
   consegnato in uno degli assegnamenti dovra' ripetere l'esame con
   un nuovo progetto

3) Tutti i comportamenti scorretti ai punti 1 e 2 verranno segnalati
   ufficialmente al presidente del corso di laurea

----------------------------
 VALUTAZIONE DELL'ASSEGNAMENTO:
----------------------------

La modalità di valutazione degli assegnamenti è descritta nel file pdf.
