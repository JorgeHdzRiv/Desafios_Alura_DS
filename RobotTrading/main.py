from scripts.importar_datos import importar_base_bitcoin
from scripts.extraer_tendencias import extraer_tendencias
from scripts.limpieza_datos import limpieza_datos
from scripts.tomar_decisiones import tomar_decisiones
from scripts.visualizacion import visualizacion
from scripts.automatizacion import automatizacion

def main():
    """
    Ejecuta todo el flujo del bot de trading de Bitcoin una vez.
    """
    print("🚀 Iniciando el bot de trading de Bitcoin...")

    # 1️⃣ Obtener datos de Bitcoin
    df_bitcoin = importar_base_bitcoin()
    if df_bitcoin is None:
        print("⚠️ No se pudieron obtener los datos de Bitcoin.")
        return

    # 2️⃣ Extraer tendencias del mercado
    precio_actual, tendencia = extraer_tendencias()
    if precio_actual is None or tendencia is None:
        print("⚠️ No se pudieron obtener las tendencias del mercado.")
        return

    # 3️⃣ Limpiar los datos
    df_bitcoin_limpio, media_bitcoin = limpieza_datos(df_bitcoin)
    if df_bitcoin_limpio is None:
        print("⚠️ Error en la limpieza de datos.")
        return

    # 4️⃣ Tomar decisiones de compra/venta
    decision, color_flecha = tomar_decisiones(df_bitcoin_limpio, precio_actual, tendencia, media_bitcoin)

    # 5️⃣ Visualizar los datos y la decisión
    visualizacion(df_bitcoin_limpio, media_bitcoin, decision, color_flecha)

    print("✅ Ejecución del bot completada. Se ha generado el gráfico con la decisión.")

if __name__ == "__main__":
    # Ejecuta el bot una sola vez, para interrumplirlo presiona Ctrl + C
    #main()

    # 🔄 Si quieres ejecutarlo en intervalos de tiempo, descomenta la siguiente línea:
    automatizacion(n_iteraciones=3, intervalo_minutos=1)
