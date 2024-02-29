import requests
import stem
import stem.connection
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup

# Función para cambiar la dirección IP utilizando Tor
def cambiar_direccion_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()  # Autenticar con el controlador de Tor
            controller.signal(Signal.NEWNYM)  # Enviar señal para obtener nueva identidad

        print("Dirección IP cambiada exitosamente a través de Tor.")
    except stem.SocketError as e:
        print(f"Error de conexión con el controlador de Tor: {e}")

# Configuración de la conexión a través de Tor
session = requests.session()
session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}

# URL a la que deseas enviar la solicitud GET para verificar la dirección IP
url = 'https://api.ipify.org/'

# Realizar la solicitud GET para verificar la dirección IP actual
response = session.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    print("Dirección IP actual:", response.text.strip())
else:
    print("Error al obtener la dirección IP:", response.status_code)

# Cambiar la dirección IP utilizando Tor
cambiar_direccion_ip()

# Realizar una nueva solicitud GET para verificar la dirección IP después del cambio
response = session.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    print("Nueva dirección IP:", response.text.strip())
else:
    print("Error al obtener la nueva dirección IP:", response.status_code)
