import requests
from bs4 import BeautifulSoup
import os

def enviar_solicitud_get():
    url = 'https://www.nombrerutyfirma.com/rut'
    params = {'term': '19.084.309-2'}
    headers = {
        'Host': 'www.nombrerutyfirma.com',
        'Cookie': 'cf_clearance=DuWwsI1Jk_E5A0UBh_tPzpwyCANkrz.mbNv9NzE286E-1709514440-1.0.1.1-Gofv6W1hJ17Hop9dIpvsVSBJFRvJorbhCHQ64v3jiS7q_2CeQbJYKWnu0uJKdT_qfKFdcQi7M6.yBpgafdI1Ow',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-CL,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.nombrerutyfirma.com',
        'Dnt': '1',
        'Sec-Gpc': '1',
        'Referer': 'https://www.nombrerutyfirma.com/',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Te': 'trailers'
    }
  
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        print("Solicitud exitosa!")
        # Guardar la respuesta en un archivo
        with open('respuesta.html', 'w', encoding='utf-8') as file:
            file.write(response.text)

        # Analizar la respuesta HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        nombres = soup.find_all('td', {'style': 'white-space: nowrap;'})
        direcciones = soup.find_all('td', {'style': 'white-space: nowrap;'})
        # Retornar la respuesta para poder acceder a ella fuera de la función
        return response

    else:
        print("Error al realizar la solicitud:", response.status_code)
        # Retornar None en caso de error
        return None

def analizar_y_borrar_html():
    # Llamando a la función para enviar la solicitud GET y obtener la respuesta
    response = enviar_solicitud_get()

    if response:
        # Analizar la respuesta HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar el div con la clase "container"
        container_div = soup.find('div', class_='container')

        # Extraer los datos necesarios dentro del div
        if container_div:
            nombre = container_div.find('td').text
            rut = container_div.find('td', style='white-space: nowrap;').text
            direccion = container_div.find_all('td')[3].text
            ciudad_comuna = container_div.find_all('td')[4].text
            #limpiar_pantalla()
            # Mostrar los datos de manera elegante
            print(f"Nombre: {nombre}")
            print(f"RUT: {rut}")
            print(f"Dirección: {direccion}")
            print(f"Ciudad/Comuna: {ciudad_comuna}")

            # Borrar el archivo HTML después de haber extraído los datos
            os.remove('respuesta.html')

# Llamando a la función para analizar y borrar el archivo HTML
analizar_y_borrar_html()