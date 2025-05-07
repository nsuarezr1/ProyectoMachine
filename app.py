from flask import Flask, render_template, request
import regex as re # pip install regex
from datetime import datetime
import LinearRegresssion

app = Flask(__name__)

modelo_path = "modelo_emisiones.pkl"

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/predecir", methods=["POST"])
def predecir():
    anio = int(request.form["anio"])
    categoria = request.form["categoria"]
    resultado = LinearRegresssion(modelo_path, anio, categoria)
    return render_template("index.html", resultado=f"Predicción de CO₂: {resultado} Gg")

if __name__ == "__main__":
    app.run(debug=True)