# Questo script Python utilizza il modulo `mysql.connector` per connettersi a un database MySQL esistente
# e inserire un nuovo record nella tabella "customers".
#
# Funzionamento:
# 1. Stabilisce una connessione con il server MySQL locale specificando host, username, password e il nome del database ("mydatabase").
# 2. Crea un cursore (`mycursor`) per eseguire comandi SQL.
# 3. Definisce una query parametrizzata di tipo INSERT per aggiungere un nuovo record nella tabella "customers", 
#    con i valori per le colonne `name` e `address`.
# 4. Esegue la query passando i valori ("John", "Highway 21") in modo sicuro, prevenendo possibili attacchi di SQL injection.
# 5. Esegue il commit della transazione con `mydb.commit()` per rendere permanente l'inserimento nel database.
# 6. Stampa il numero di record inseriti a conferma dell’operazione.


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
