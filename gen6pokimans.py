import mysql.connector
from flask import Flask, jsonify, abort

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="PokemonDB"
)
mycursor = mydb.cursor(dictionary=True)  # dictionary=True per avere dict e non tuple

app = Flask(__name__)

@app.route("/")
def home():
    return "Benvenuto al database Pokémon!"

@app.route("/pokemon")
def get_all_pokemon():
    mycursor.execute("SELECT * FROM Pokemon")
    results = mycursor.fetchall()
    return jsonify(results)

@app.route("/count")
def get_pokemon_count():
    mycursor.execute("SELECT COUNT(*) AS total FROM Pokemon")
    count = mycursor.fetchone()['total']
    return jsonify({"total_pokemon": count})

@app.route("/types")
def get_all_types():
    mycursor.execute("SELECT DISTINCT type1 FROM Pokemon")
    types1 = {row['type1'] for row in mycursor.fetchall()}
    mycursor.execute("SELECT DISTINCT type2 FROM Pokemon WHERE type2 IS NOT NULL")
    types2 = {row['type2'] for row in mycursor.fetchall()}
    all_types = sorted(types1.union(types2))
    return jsonify({"types": all_types})

@app.route("/fast")
def get_fast_pokemon():
    mycursor.execute("SELECT * FROM Pokemon WHERE speed > 100")
    results = mycursor.fetchall()
    return jsonify(results)

@app.route("/pokemon/legendary")
def get_legendary_pokemon():
    mycursor.execute("SELECT * FROM Pokemon WHERE legendary = TRUE")
    results = mycursor.fetchall()
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)

