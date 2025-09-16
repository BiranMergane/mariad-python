# Questo script Python utilizza il modulo `mysql.connector` per connettersi a un server MySQL locale.
# Funzionamento:
# 1. Stabilisce una connessione con il server MySQL tramite la funzione `mysql.connector.connect()`, 
#    specificando host, username e password per l'autenticazione.
# 2. Crea un cursore (`mycursor`) per eseguire comandi SQL sul database.
# 3. Esegue una query SQL per creare un nuovo database chiamato "mydatabase".

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
