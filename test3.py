#!/usr/bin/python3
import random
import time
import os
import signal
import sys
from termcolor import colored
import re
import requests
from bs4 import BeautifulSoup
import os
#Progama 2.0



def Peticion_De_rut(tu_rut):
    url = 'https://www.nombrerutyfirma.com/rut'
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
    # Función para validar el formato del RUT
    def validar_rut(rut):
        patron_rut = r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK0-9]$'

        return re.match(patron_rut, rut) is not None

    if not validar_rut(tu_rut):
        print("El RUT ingresado no tiene el formato correcto. Debe ser en formato x.xxx.xxx-x.")
        return
    
    # Enviar la solicitud GET con el RUT válido
    params = {'term': tu_rut}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        # Guardar la respuesta en un archivo
        with open('respuesta.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
        
        # Analizar la respuesta HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar el div con la clase "container"
        container_div = soup.find('div', class_='container')

        # Extraer los datos necesarios dentro del div
        if container_div:
            rut_element = container_div.find('td', style='white-space: nowrap;')
            if rut_element:
                rut = rut_element.text.strip() 
                nombre = container_div.find_all('td')[0].text.strip()
                sexo = container_div.find_all('td')[2].text.strip()  
                Dirección = container_div.find_all('td')[3].text.strip()
                ciudad = container_div.find_all('td')[4].text.strip()
                
                # Ordenar el nombre 
                nombres_separados = nombre.split()
                nombres_reordenados = " ".join(nombres_separados[2:] + nombres_separados[:2])
                
                # Ordenando el tipo de sexo
                sexo_element = sexo
                if sexo_element == "VAR":
                    sexo_element = "Hombre"
                elif sexo_element == "MUJ":
                    sexo_element = "Mujer"
                else:
                    sexo_element = 'No encontrado'

                # Mostrar los datos 
                print(f"Nombre: {nombres_reordenados}")
                print(f"RUT: {rut}")
                print(f"Sexo: {sexo_element}")
                print(f"Dirección: {Dirección}")
                print(f"Ciudad/Comuna: {ciudad}")
                
                os.remove('respuesta.html')
            else:
                print("El RUT ingresado no se encontró en la base de datos.")
                os.remove('respuesta.html')
       
tu_rut=input(":")
Peticion_De_rut(tu_rut)
