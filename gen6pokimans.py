import mysql.connector
from flask import Flask, jsonify, abort

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="pokemon_db"
)
mycursor = mydb.cursor()

app = Flask(__name__)

@app.route("/")
def home():
    return "Benvenuto al database Pokémon!"

@app.route("/pokemon")
def get_all_pokemon():
    mycursor.execute("SELECT id, Name, Type1, Type2 FROM pokemon LIMIT 50")
    columns = [desc[0] for desc in mycursor.description]
    myresult = mycursor.fetchall()
    result = [dict(zip(columns, row)) for row in myresult]
    return jsonify(result)

@app.route("/pokemon/<int:pokemon_id>")
def get_pokemon_detail(pokemon_id):
    mycursor.execute("SELECT * FROM pokemon WHERE id = %s", (pokemon_id,))
    columns = [desc[0] for desc in mycursor.description]
    row = mycursor.fetchone()
    if row is None:
        abort(404, description="Pokémon non trovato")
    result = dict(zip(columns, row))
    return jsonify(result)

@app.route("/type/<type_name>")
def get_pokemon_by_type(type_name):
    query = """
    SELECT id, Name, Type1, Type2 FROM pokemon
    WHERE Type1 = %s OR Type2 = %s
    """
    mycursor.execute(query, (type_name.capitalize(), type_name.capitalize()))
    columns = [desc[0] for desc in mycursor.description]
    myresult = mycursor.fetchall()
    result = [dict(zip(columns, row)) for row in myresult]
    return jsonify(result)

# Route per Pokémon leggendari
@app.route("/legendary")
def get_legendary_pokemon():
    mycursor.execute("SELECT id, Name, Type1, Type2 FROM pokemon WHERE Legendary = TRUE")
    columns = [desc[0] for desc in mycursor.description]
    myresult = mycursor.fetchall()
    result = [dict(zip(columns, row)) for row in myresult]
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
