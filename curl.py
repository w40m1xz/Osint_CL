import requests

# Configurar el proxy SOCKS5 para las solicitudes HTTP

proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}


# URL a la que deseas enviar la solicitud POST
url = 'https://www.nombrerutyfirma.com/rut'

input_save = input("Ingresa el RUT que quieres: ")

# Datos a enviar en la solicitud POST
data = {
    'term': input_save
}

# Realizar la solicitud POST a través de Tor
response = requests.post(url, data=data, proxies=proxies)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    print("Solicitud exitosa!")
    # Aquí puedes procesar la respuesta como desees
    print(response.text)
else:
    print("Error al realizar la solicitud:", response.status_code)
