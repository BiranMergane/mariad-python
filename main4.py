# Questo script Python utilizza il modulo `mysql.connector` per connettersi a un database MySQL esistente
# e recuperare tutti i record dalla tabella "customers".
#
# Funzionamento:
# 1. Stabilisce una connessione con il server MySQL locale specificando host, username, password e il nome del database ("mydatabase").
# 2. Crea un cursore (`mycursor`) per eseguire comandi SQL.
# 3. Esegue una query SQL di tipo SELECT per ottenere tutti i dati dalla tabella "customers".
# 4. Recupera tutti i risultati della query tramite `fetchall()`, che ritorna una lista di tuple, ognuna rappresentante una riga.
# 5. Itera attraverso la lista dei risultati e stampa ogni singola riga.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
