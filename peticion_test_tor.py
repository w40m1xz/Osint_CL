import socks
import socket
import requests
from bs4 import BeautifulSoup
import stem.process
from stem import Signal
from stem.control import Controller
import os
import sys
import tempfile

def cambiar_nodo_tor():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="your_password")
        controller.signal(Signal.NEWNYM)

def iniciar_tor():
    try:
        SOCKS_PORT = 9050
        print("Iniciando Tor...")

        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout = open(tempfile.mkstemp()[1], 'w')
        sys.stderr = sys.stdout

        tor_process = stem.process.launch_tor_with_config(
            config={
                'SocksPort': str(SOCKS_PORT),
                'ControlPort': '9051',
                'HashedControlPassword': '16:10382C861ECE2BA66079454359C7F11C5E5CFF72D60BDDA6E7FB3854A5',
                'Log': [],
            },
            init_msg_handler=None,
            close_output=False,
        )
        print("Tor ha iniciado.")

        sys.stdout.close()
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        os.system('cls' if os.name == 'nt' else 'clear')

        return tor_process
    except Exception as e:
        print("Error al iniciar Tor:", e)
        return None

def obtener_datos_via_tor(url, tor_process):
    with requests.Session() as session:
        session.proxies = {'http': 'socks5://localhost:9050',
                           'https': 'socks5://localhost:9050'}
        input_save = input("Ingresa el RUT que quieres: ")
        data = {'term': input_save}
        response = session.post(url, data=data)
        if response.status_code == 200:
            print("Solicitud exitosa!")
            soup = BeautifulSoup(response.text, 'html.parser')
            tabla_resultados = soup.find('table', class_='table table-hover')
            if tabla_resultados:
                fila_resultado = tabla_resultados.find('tr', tabindex='1')
                if fila_resultado:
                    celdas_resultado = fila_resultado.find_all('td')
                    nombre = celdas_resultado[0].text.strip()
                    rut = celdas_resultado[1].text.strip()
                    sexo = celdas_resultado[2].text.strip()
                    direccion = celdas_resultado[3].text.strip()
                    ciudad_comuna = celdas_resultado[4].text.strip()
                    print("Nombre:", nombre)
                    print("RUT:", rut)
                    print("Sexo:", sexo)
                    print("Dirección:", direccion)
                    print("Ciudad/Comuna:", ciudad_comuna)
                else:
                    print("No se encontró la fila del resultado.")
            else:
                print("No se encontró la tabla de resultados.")
        else:
            print("Error al realizar la solicitud:", response.status_code)

url = 'https://www.nombrerutyfirma.com/rut'
tor_process = iniciar_tor()
if tor_process:
    obtener_datos_via_tor(url, tor_process)
    tor_process.terminate()