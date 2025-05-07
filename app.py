from flask import Flask, render_template, request
import regex as re 
from datetime import datetime
import LinearRegresssion

app = Flask(__name__)

modelo_path = "modelo_emisiones.pkl"

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/ingenieria-datos")
def ingenieria_datos():
    return render_template("ingenieria_datos.html")

@app.route("/ingenieria-modelo")
def ingenieria_modelo():
    return render_template("ingenieria_modelo.html")


@app.route("/predecir", methods=["POST"])
def predecir():
    anio = int(request.form["anio"])
    categoria = request.form["categoria"]
    resultado = LinearRegresssion(modelo_path, anio, categoria)
    return render_template("index.html", resultado=f"Predicción de CO₂: {resultado} Gg")

if __name__ == "__main__":
    app.run(debug=True)