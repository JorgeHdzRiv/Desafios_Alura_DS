import pandas_ta as ta

def tomar_decisiones(df_bitcoin, precio_actual, tendencia, media_bitcoin):
    """
    Calcula los indicadores técnicos y toma decisiones de compra/venta.

    Parámetros:
        df_bitcoin (pd.DataFrame): DataFrame con datos de Bitcoin.
        precio_actual (float): Precio actual del Bitcoin.
        tendencia (str): Tendencia del mercado ('baja' o 'alta').
        media_bitcoin (float): Media del precio de Bitcoin después de limpieza.

    Retorna:
        (str, str): Decisión de compra/venta ('Comprar', 'Vender', 'Esperar') y color de la flecha ('green', 'red', 'orange').
    """
    # 📌 Eliminar MultiIndex en columnas si existe
    if isinstance(df_bitcoin.columns[0], tuple):
        df_bitcoin.columns = [col[0] for col in df_bitcoin.columns]

    # Verificar si 'Close' está presente después de la conversión
    if 'Close' not in df_bitcoin.columns:
        print("⚠️ La columna 'Close' no se encontró después de procesar el DataFrame. Revisando estructura...")
        print(df_bitcoin.head())  # Muestra las primeras filas para depuración
        return None, None

    # Calcular el RSI con un periodo de 14 días
    df_bitcoin['RSI'] = ta.rsi(df_bitcoin['Close'], length=14)

    # Calcular la SMA de 50 días
    df_bitcoin['SMA_50'] = ta.sma(df_bitcoin['Close'], length=50)

    # Obtener los valores más recientes
    rsi_actual = df_bitcoin['RSI'].iloc[-1]  # Último valor del RSI
    sma_50_actual = df_bitcoin['SMA_50'].iloc[-1]  # Último valor de la SMA de 50 días

    # Criterios de decisión
    if rsi_actual < 30 and precio_actual < sma_50_actual:
        decision = 'Comprar'
        color_flecha = 'green'
    elif precio_actual >= media_bitcoin and tendencia == 'baja':
        decision = 'Vender'
        color_flecha = 'red'
    else:
        decision = 'Esperar'
        color_flecha = 'orange'

    # Imprimir resultados para depuración
    print(f"📊 RSI actual: {rsi_actual:.2f}")
    print(f"📉 SMA 50 días actual: {sma_50_actual:.2f}")
    print(f"⚡ Decisión del algoritmo: {decision}")

    return decision, color_flecha
