import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import io
import base64
from sklearn.linear_model import LinearRegression

# Cargar los datos de la primera hoja
df_energia = pd.read_excel("DatosMachine.xlsx", sheet_name="Energia")
X_energia = df_energia[["Año"]]
y_energia = df_energia[["CO2 -Emisiones en Gg"]]

# Entrenar el modelo para la primera hoja
modelo_energia = LinearRegression()
modelo_energia.fit(X_energia, y_energia)

def calcular_emisiones_energia(año): # Renombramos la función para mayor claridad
    resultado = modelo_energia.predict(pd.DataFrame({"Año": [año]}))[0]
    return resultado

def generar_grafica_energia():
    plt.figure(figsize=(6, 4))
    plt.scatter(X_energia, y_energia, color='blue', label='Emisiones de CO2 Reales')
    x_range_energia = np.linspace(min(X_energia["Año"]), max(X_energia["Año"]), 100).reshape(-1, 1)
    x_range_energia_df = pd.DataFrame(x_range_energia, columns=["Año"])
    y_pred_energia = modelo_energia.predict(x_range_energia_df)
    plt.plot(x_range_energia, y_pred_energia, color='red', linewidth=2, label='Línea de Regresión')
    plt.xlabel('Año')
    plt.ylabel('CO2 - Emisiones en Gg')
    plt.title('Regresión Lineal de Emisiones de CO2 (Energía)')
    plt.legend()
    img_energia = io.BytesIO()
    plt.savefig(img_energia, format='png')
    img_energia.seek(0)
    grafica_energia_url = base64.b64encode(img_energia.getvalue()).decode()
    plt.close()
    return grafica_energia_url



# Cargar los datos de la segunda hoja
df_procesos= pd.read_excel("DatosMachine.xlsx", sheet_name="Procesos") # Reemplaza "procesos" con el nombre de tu segunda hoja
X_procesos = df_procesos[["Año"]] # Ajusta las columnas si son diferentes
y_procesos = df_procesos[["CO2 -Emisiones en Gg"]] # Ajusta las columnas si son diferentes

# Entrenar el modelo para la segunda hoja
modelo_procesos = LinearRegression()
modelo_procesos.fit(X_procesos, y_procesos)

def calcular_emisiones_procesos(año): # Nueva función para la segunda hoja
    resultado = modelo_procesos.predict(pd.DataFrame({"Año": [año]}))[0]
    return resultado

def generar_grafica_procesos():
    plt.figure(figsize=(6, 4))
    plt.scatter(X_procesos, y_procesos, color='green', label='CO2 -Emisiones en Gg Real') # Ajusta la etiqueta
    x_range_procesos = np.linspace(min(X_procesos["Año"]), max(X_procesos["Año"]), 100).reshape(-1, 1)
    x_range_procesos_df = pd.DataFrame(x_range_procesos, columns=["Año"])
    y_pred_procesos = modelo_procesos.predict(x_range_procesos_df)
    plt.plot(x_range_procesos, y_pred_procesos, color='orange', linewidth=2, label='Línea de Regresión') # Ajusta la etiqueta
    plt.xlabel('Año')
    plt.ylabel('CO2 -Emisiones en Gg') # Ajusta la etiqueta
    plt.title('Regresión Lineal del CO2') # Ajusta el título
    plt.legend()
    img_procesos = io.BytesIO()
    plt.savefig(img_procesos, format='png')
    img_procesos.seek(0)
    grafica_procesos_url = base64.b64encode(img_procesos.getvalue()).decode()
    plt.close()
    return grafica_procesos_url
