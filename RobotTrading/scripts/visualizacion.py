import os
import matplotlib.pyplot as plt
import pandas as pd

def visualizacion(df_bitcoin, media_bitcoin, decision, color_flecha):
    """
    Genera un gráfico de la evolución del precio de Bitcoin y su promedio con una línea suavizada.

    Parámetros:
        df_bitcoin (pd.DataFrame): DataFrame con los datos de Bitcoin.
        media_bitcoin (float): Precio promedio de Bitcoin después de limpieza.
        decision (str): Decisión del algoritmo ('Comprar', 'Vender', 'Esperar').
        color_flecha (str): Color de la flecha ('green', 'red', 'orange').
    """
    # 📌 Verificar y eliminar MultiIndex en columnas
    if isinstance(df_bitcoin.columns[0], tuple):
        df_bitcoin.columns = [col[0] for col in df_bitcoin.columns]

    # 📌 Verificar si 'Close' está en las columnas después de la conversión
    if 'Close' not in df_bitcoin.columns:
        print("⚠️ La columna 'Close' no se encontró. Verificando estructura del DataFrame...")
        print("Columnas actuales:", df_bitcoin.columns)
        print(df_bitcoin.head())  # Muestra las primeras filas para depuración
        return

    # Aplicar media móvil de 20 períodos para suavizar la línea
    df_bitcoin['SMA_20'] = df_bitcoin['Close'].rolling(window=20, min_periods=1).mean()

    # 1. Adicionar una nueva columna "Promedio" con el valor de media_bitcoin
    df_bitcoin['Promedio'] = media_bitcoin

    # Crear la carpeta 'results' si no existe
    os.makedirs("results", exist_ok=True)

    # 2. Configurar el tamaño del gráfico en una proporción de 16x5
    plt.figure(figsize=(16, 5))

    # 3. Adicionar un título al gráfico
    plt.title("Evolución del Precio de Bitcoin y Promedio (Suavizado con SMA 20)")

    # 4. Dibujar la línea del precio "Close" en el gráfico
    plt.plot(df_bitcoin.index, df_bitcoin['SMA_20'], label="Precio Suavizado (SMA 20)", color='blue')

    # 5. Dibujar la línea del "Promedio" en el gráfico
    plt.plot(df_bitcoin.index, df_bitcoin['Promedio'], label="Promedio (media)", color='orange', linestyle='--')

    # 6. Colocar la flecha en el último valor de 'Close'
    plt.annotate("",
                 xy=(df_bitcoin.index[-1], df_bitcoin['Close'].iloc[-1]),  # Último valor de 'Close'
                 xytext=(df_bitcoin.index[-1], df_bitcoin['Close'].iloc[-1] + 500),  # Flecha ajustada arriba
                 arrowprops=dict(facecolor=color_flecha, shrink=0.05))

    # 7. Colocar el texto de la decisión en el centro superior del gráfico
    plt.annotate(f"Decisión: {decision}",
                 xy=(0.5, 0.95), xycoords='axes fraction',  # Posición en el centro superior
                 fontsize=16, color=color_flecha, ha='center', va='top',
                 bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1'))

    # 8. Configurar las etiquetas de los ejes
    plt.xlabel("Fecha")
    plt.ylabel("Precio (USD)")

    # 9. Mostrar la leyenda en la parte superior izquierda
    plt.legend(loc="upper left")

    # 10. Mostrar y guardar el gráfico
    plt.savefig("results/decision.png")
    plt.show()
