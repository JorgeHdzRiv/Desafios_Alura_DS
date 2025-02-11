from urllib.request import urlopen
from bs4 import BeautifulSoup

def extraer_tendencias():
    """
    Obtiene el precio actual del Bitcoin y su tendencia desde CoinMarketCap.
    
    Retorna:
        - precio_actual (float): Precio actual del Bitcoin en USD.
        - tendencia (str): 'baja' o 'alta' según el cambio en la última hora.
    """
    try:
        # Obtener los datos de CoinMarketCap con BeautifulSoup
        url = 'https://coinmarketcap.com/es/'
        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        # Extraer el precio actual del Bitcoin
        precio_element = soup.find('td', style="text-align:end")
        precio_actual = float(precio_element.div.span.getText().replace('$', '').replace(',', ''))

        # Extraer el porcentaje de variación en la última hora
        tendencia_element = soup.find('td', style="text-align:end").find_next_sibling()
        porcentaje = tendencia_element.span.getText()

        # Determinar la tendencia (sube o baja)
        if tendencia_element.span.span['class'][0] == 'icon-Caret-down':
            tendencia = 'baja'
        else:
            tendencia = 'alta'

        # Imprimir los resultados para verificar
        print(f"📊 Precio Actual del Bitcoin: {precio_actual} USD")
        print(f"📉 Variación en la última hora: {porcentaje}")
        print(f"📈 Tendencia: {tendencia}")

        return precio_actual, tendencia

    except Exception as e:
        print(f"⚠️ Error al extraer tendencias: {e}")
        return None, None
