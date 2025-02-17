import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def preprocesamiento(df):
    # Variables a elegir
    variables_elegidas = [
    "categoria_alimento",
    "departamento",
    "tipo",
    "ventas_tienda(en millones)",
    "costo_tienda(en millones)",
    'pais',
    "estado_civil",
    "genero",
    "escolaridad",
    "miembro",
    "ocupacion",
    "ingreso_anual",
    "numero_hijos",
    "pies_cuadrados_tienda",
    "costo"]

    # Filtrar el dataset con las variables seleccionadas
    data_selected = df[variables_elegidas]

    # 1. Codificación de escolaridad y miembro (Label Encoding por orden lógico)
    educacion_orden = {
        "Primaria": 1,
        "Secundaria": 2,
        "Técnico": 3,
        "Superior": 4,
        "Maestría": 5
    }

    miembro_orden = {
        "Normal": 1,
        "Bronce": 2,
        "Plata": 3,
        "Oro": 4
    }

    # Usar .loc[:, "columna"] para modificar sin advertencias
    data_selected.loc[:, "escolaridad"] = data_selected["escolaridad"].map(educacion_orden)
    data_selected.loc[:, "miembro"] = data_selected["miembro"].map(miembro_orden)
    
    # One-Hot Encoding a las variables categóricas sin orden específico
    categorical_columns = ["categoria_alimento", "departamento", "tipo", "pais", "estado_civil",
                            "genero","ocupacion"]

    # Aplicar One-Hot Encoding con One-Hot Encoder
    encoder = OneHotEncoder(sparse_output=False, drop="first")
    encoded_data = encoder.fit_transform(data_selected[categorical_columns])
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_columns))

    # Crear un objeto StandardScaler y concatear el dataframe
    scaler = StandardScaler()

    numeric_columns = ["ventas_tienda(en millones)","costo_tienda(en millones)", "ingreso_anual", "numero_hijos","pies_cuadrados_tienda","costo",
                    "escolaridad","miembro"]
    df_final = pd.concat([encoded_df, data_selected[numeric_columns]], axis=1)

    X_std = scaler.fit_transform(df_final)
    df_standarizado = pd.DataFrame(X_std, columns=df_final.columns)
    df_standarizado.head()

    # Guardar el df_standarizado
    df_standarizado.to_csv('./data/media_cost_prediction_standarizado.csv', index=False)

    # Guardar el x_std
    np.save('./models/X_std.npy', X_std)

    print("\nPreprocesamiento finalizado")
    print("Forma de X_std:", X_std.shape)

    return X_std



