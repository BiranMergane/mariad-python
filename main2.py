# Questo script Python utilizza il modulo `mysql.connector` per connettersi a un database MySQL esistente.
#
# Funzionamento:
# 1. Stabilisce una connessione con il server MySQL locale specificando host, username, password e il nome del database ("mydatabase").
# 2. Crea un cursore (`mycursor`) che permette di eseguire comandi SQL sul database connesso.
# 3. Esegue una query SQL per creare una nuova tabella chiamata "customers" con due colonne:
#    - `name`: campo di tipo VARCHAR con lunghezza massima di 255 caratteri, per memorizzare il nome del cliente.
#    - `address`: campo di tipo VARCHAR con lunghezza massima di 255 caratteri, per memorizzare l'indirizzo del cliente.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
