#!/usr/bin/python3

import requests

import requests

# URL a la que deseas enviar la solicitud POST
url = 'https://www.nombrerutyfirma.com/rut'

# Datos a enviar en la solicitud POST
data = {
    'term': 'xx.xxx.xxx-k'  # Puedes cambiar este rut por cualquier otro que desees buscar
}

# Cabeceras de la solicitud POST


# Realizar la solicitud POST
response = requests.post(url, data=data,)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    print("Solicitud exitosa!")
    
    # Mostrar el contenido de la respuesta
    print("Contenido de la respuesta:")
    print(response.text)  # Opcionalmente, puedes usar response.content para obtener los bytes de la respuesta
else:
    print("Error al realizar la solicitud:", response.status_code)
