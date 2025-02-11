import yfinance as yf
import pandas as pd
import os
from datetime import datetime, timedelta

def importar_base_bitcoin():
    """
    Obtiene los datos históricos de Bitcoin (BTC-USD) de los últimos 7 días con intervalos de 5 minutos y los guarda en 'data/'.
    """
    hoy = datetime.now()
    inicio = hoy - timedelta(days=7)

    print(f"Importando datos desde {inicio} hasta {hoy}")

    df_bitcoin = yf.download('BTC-USD', start=inicio, end=hoy, interval='5m')

    if df_bitcoin.empty:
        print("⚠️ No se pudieron obtener datos.")
        return None

    os.makedirs(r"data", exist_ok=True)
    df_bitcoin.to_csv("data/bitcoin_data.csv", index=True)
    print("✅ Datos guardados en 'data/bitcoin_data.csv'")

    return df_bitcoin
