from flask import Flask, render_template, request
import RegresionProyecto

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
    calculateResult_energia = None
    calculateResult_procesos = None
    plot_url_energia = RegresionProyecto.generar_grafica_energia()   # Obtiene la URL de la primera gráfica
    plot_url_procesos = RegresionProyecto.generar_grafica_procesos() # Obtiene la URL de la segunda gráfica

    if request.method == "POST":
        # Procesar la predicción para la primera gráfica (emisiones de CO2)
        co_energia = float(request.form.get("co_energia", 0)) # Usa .get() con un valor por defecto
        if co_energia:
            calculateResult_energia = RegresionProyecto.calcular_emisiones_energia(co_energia)

        # Procesar la predicción para la segunda gráfica (índice de producción)
        co_procesos = float(request.form.get("co_procesos", 0)) # Usa .get() con un valor por defecto
        if co_procesos:
            calculateResult_procesos = RegresionProyecto.calcular_emisiones_procesos(co_procesos)

    return render_template(
        "RegresionLineal.html",
        result_energia=calculateResult_energia,
        result_procesos=calculateResult_procesos,
        plot_url_energia=plot_url_energia,
        plot_url_procesos=plot_url_procesos
    )

if __name__ == "__main__":
    app.run(debug=True)