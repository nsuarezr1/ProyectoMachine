from flask import Flask, render_template, request
import regex as re 
from datetime import datetime
import RLProyecto

app = Flask(__name__)

modelo_path = "modelo_emisiones.pkl"

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/ingenieria-datos")
def ingenieria_datos():
    return render_template("ingenieria_datos.html")

@app.route("/modelo")
def modelo():
    return render_template("modelo.html")

@app.route("/RegresionLineal/", methods=["GET", "POST"])
def Regresionlineal():
    calculateResult = None
    plot_url = RLProyecto.generar_grafica
    if request.method == "POST":
        temperatura = float(request.form["temperatura"])
        calculateResult = RLProyecto.calcularHelados(temperatura)
    return render_template("RegresionLineal.html", result=calculateResult, plot_url=plot_url)


if __name__ == "__main__":
    app.run(debug=True)