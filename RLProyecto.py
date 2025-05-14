import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import io
import base64
from sklearn.linear_model import LinearRegression

df = pd.read_excel("DatosMachine.xlsx")

X = df[["Año"]]
y = df[["CO2 -Emisiones en Gg"]]

modelo = LinearRegression()
modelo.fit(X, y)

def calcularHelados(temperatura):  #Esta función debería ser renombrada
    resultado = modelo.predict(pd.DataFrame({"Año": [temperatura]}))[0]
    return resultado

def generar_grafica():
    plt.figure(figsize=(6, 4))
    plt.scatter(X, y, color='blue', label='Emisiones de CO2 Reales')  #Actualizado
    x_range = np.linspace(min(X["Año"]), max(X["Año"]), 100).reshape(-1, 1)
    x_range_df = pd.DataFrame(x_range, columns=["Año"])
    y_pred = modelo.predict(x_range_df)
    plt.plot(x_range, y_pred, color='red', linewidth=2, label='Línea de Regresión') #Actualizado
    plt.xlabel('Año')
    plt.ylabel('CO2 - Emisiones en Gg')  #Actualizado
    plt.title('Regresión Lineal de Emisiones de CO2')  #Actualizado
    plt.legend()
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    grafica_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return grafica_url
