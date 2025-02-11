from IPython.display import clear_output
import time
from scripts.importar_datos import importar_base_bitcoin
from scripts.extraer_tendencias import extraer_tendencias
from scripts.limpieza_datos import limpieza_datos
from scripts.tomar_decisiones import tomar_decisiones
from scripts.visualizacion import visualizacion

def automatizacion(n_iteraciones=None, intervalo_minutos=5):
    """
    Ejecuta el bot de trading en intervalos de minutos definidos por el usuario.
    """
    iteracion = 0
    intervalo_segundos = intervalo_minutos * 60  # Convertir minutos a segundos

    try:
        while n_iteraciones is None or iteracion < n_iteraciones:
            iteracion += 1
            print(f"🔄 Ejecución {iteracion}...")

            clear_output(wait=True)  # Limpia la pantalla antes de cada iteración

            # Ejecutar las funciones en secuencia
            df_bitcoin = importar_base_bitcoin()
            precio_actual, tendencia = extraer_tendencias()
            df_bitcoin_limpio, media_bitcoin = limpieza_datos(df_bitcoin)
            decision, color_flecha = tomar_decisiones(df_bitcoin_limpio, precio_actual, tendencia, media_bitcoin)
            visualizacion(df_bitcoin_limpio, media_bitcoin, decision, color_flecha)

            print(f"⏳ Esperando {intervalo_minutos} minutos antes de la siguiente ejecución...")
            time.sleep(intervalo_segundos)  # Esperar el tiempo definido por el usuario

    except KeyboardInterrupt:
        print("⏹️ Ejecución detenida manualmente.")
