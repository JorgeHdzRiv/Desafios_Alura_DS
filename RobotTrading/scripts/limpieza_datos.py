import os
import pandas as pd
import matplotlib.pyplot as plt

def limpieza_datos(df_bitcoin):
    """
    Limpia los datos de Bitcoin, elimina outliers y calcula la media del precio.

    Parámetros:
        df_bitcoin (pd.DataFrame): DataFrame con los datos de Bitcoin.

    Retorna:
        df_bitcoin_limpio (pd.DataFrame): DataFrame limpio sin valores nulos ni outliers.
        media_bitcoin (float): Precio promedio del Bitcoin después de la limpieza.
    """
    if df_bitcoin is None or df_bitcoin.empty:
        print("⚠️ No hay datos para limpiar.")
        return None, None

    # 📌 Eliminar MultiIndex en columnas
    df_bitcoin.columns = [col[0] for col in df_bitcoin.columns]

    # Crear la carpeta 'results' si no existe
    os.makedirs("results", exist_ok=True)

    print(f"🔍 Registros antes de la limpieza: {df_bitcoin.shape[0]}")

    # 1. Boxplot antes de la limpieza
    plt.figure(figsize=(8, 6))
    plt.boxplot(df_bitcoin['Close'])
    plt.title('Boxplot del Precio de Bitcoin (Close) antes de la limpieza')
    plt.ylabel('Precio (USD)')
    plt.savefig("results/boxplot_before.png")

    # 2. Buscar valores nulos en la columna 'Close' y eliminarlos
    df_bitcoin.dropna(subset=['Close'], inplace=True)

    # 3. Eliminar registros donde el Volume sea menor o igual a 0
    df_bitcoin = df_bitcoin[df_bitcoin['Volume'] > 0]

    # 4. Identificar outliers en la columna 'Close' utilizando un boxplot
    plt.figure(figsize=(8, 6))
    plt.boxplot(df_bitcoin['Close'])
    plt.title('Boxplot del Precio de Bitcoin (Close) después de la limpieza')
    plt.ylabel('Precio (USD)')
    plt.savefig("results/boxplot_after.png")

    # 5. Calcular los cuartiles para identificar los outliers
    Q1 = df_bitcoin['Close'].quantile(0.25)
    Q3 = df_bitcoin['Close'].quantile(0.75)
    IQR = Q3 - Q1  # Rango intercuartil

    # 6. Filtrar los registros cuyo precio (Close) esté entre el Q1 y el Q3
    df_bitcoin = df_bitcoin[(df_bitcoin['Close'] >= Q1) &
                            (df_bitcoin['Close'] <= Q3)]

    # 7. Calcular el precio promedio (media) de la columna 'Close'
    media_bitcoin = df_bitcoin['Close'].mean()

    # Imprimir resultados para verificar
    print(f"📉 Precio promedio de Bitcoin (media): {media_bitcoin:.2f} USD")
    print(f"📊 Registros después de la limpieza: {df_bitcoin.shape[0]}")

    return df_bitcoin, media_bitcoin

