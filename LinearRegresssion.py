
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

MODELO_PATH = "modelo_emisiones.pkl"
DATOS_PATH = "DatosMachine.xlsx"

# Función para entrenar y guardar el modelo
def entrenar_modelo():
    df = pd.read_excel(DATOS_PATH, sheet_name="Reporte_emisiones_y_absorciones")
    data = df[["Año", "Categorías IPCC 2006", "CO2 -Emisiones en Gg"]].copy()
    data = data.dropna(subset=["CO2 -Emisiones en Gg"])

    # Limpiar números
    data["CO2 -Emisiones en Gg"] = data["CO2 -Emisiones en Gg"].str.replace(",", "")
    data["CO2 -Emisiones en Gg"] = pd.to_numeric(data["CO2 -Emisiones en Gg"], errors="coerce")
    data = data.dropna()

    X = data[["Año", "Categorías IPCC 2006"]]
    y = data["CO2 -Emisiones en Gg"]

    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["Categorías IPCC 2006"])
    ], remainder="passthrough")

    modelo = Pipeline([
        ("preprocessor", preprocessor),
        ("regresion", LinearRegression())
    ])

    modelo.fit(X, y)
    joblib.dump(modelo, MODELO_PATH)

# Función para predecir emisiones
def predecir_emision(anio, categoria):
    if not os.path.exists(MODELO_PATH):
        entrenar_modelo()
    modelo = joblib.load(MODELO_PATH)
    entrada = pd.DataFrame([[anio, categoria]], columns=["Año", "Categorías IPCC 2006"])
    prediccion = modelo.predict(entrada)
    return round(prediccion[0], 2)