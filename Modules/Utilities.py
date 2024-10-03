#!/usr/bin/python3
from Modules.Drawings import Dibujos
import re
import time
import os
from termcolor import colored
import sys
import requests
from bs4 import BeautifulSoup
import pygame
# Mis funciones del progamas

class Helpers: 
      @staticmethod
      def limpiar_pantalla():
            sistema_operativo = os.name
            if sistema_operativo == 'nt':  # Windows
               os.system('cls')
            else:  # Unix/Linux/MacOS
             os.system('clear')
      @staticmethod
      def control_De_salida(self, sig, frame=None):
          print(colored(f"\n\n[!]Saliendo...\n",'red'))
          pygame.mixer.music.stop()
          sys.exit(0)
      @staticmethod
      def get_music_file_path(file_name):
          current_dir = os.path.dirname(__file__)
          data_dir = os.path.join(current_dir, '..', 'Data')
          music_file_path = os.path.join(data_dir, file_name)
          return music_file_path
      @staticmethod
      def play_music(file_path):
          pygame.init()
          pygame.mixer.music.load(file_path)
          pygame.mixer.music.play(-1)
          while pygame.mixer.music.get_busy():
           pygame.time.Clock().tick(10)
class Functions:
      def validar_rut(): 
        while True:
            Dibujos.osint_cl
            rut = input("Ingresa un RUT en el formato xx.xxx.xxx-k (Solo números y último dígito 0-9 o K): ")
            patron_rut = r'^(25|[1-9]|[1][0-9]|2[0-5])\.\d{3}\.\d{3}-[\dkK0-9]$'
            if re.match(patron_rut, rut):
                break
            else:
                print("El RUT ingresado no tiene el formato correcto. Inténtalo nuevamente.")
                time.sleep(1)
                Helpers.limpiar_pantalla
                Dibujos.osint_cl     
        return rut
      def buscador_de_rut(rut):
        url = 'https://www.nombrerutyfirma.com/rut'
        headers = {
            'Host': 'www.nombrerutyfirma.com',
            #'Cookie': 'cf_clearance=DuWwsI1Jk_E5A0UBh_tPzpwyCANkrz.mbNv9NzE286E-1709514440-1.0.1.1-Gofv6W1hJ17Hop9dIpvsVSBJFRvJorbhCHQ64v3jiS7q_2CeQbJYKWnu0uJKdT_qfKFdcQi7M6.yBpgafdI1Ow',
            'User-Agent': 'Mozilla/5.0 (compatible; Konqueror/4.0; Linux) KHTML/4.0.5 (like Gecko)',
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
        # Enviar la solicitud GET con el RUT válido
        params = {'term': rut}
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
            else:
                print("Error al realizar la solicitud:", response.status_code)
      def continuar_buscando_rut(self):
        Dibujos.osint_cl
        Helpers.limpiar_pantalla
        Dibujos.osint_cl
        while True:
            respuesta = input("¿Quieres buscar otro RUT? (si/no): ")
            if respuesta == 'si':
              Helpers.limpiar_pantalla
              Dibujos.osint_cl()
              rut_verificado= self.validar_rut()
              self.buscador_de_rut(rut_verificado)
              input("Presiona Enter para continuar...")
            elif respuesta.lower() == 'no':
              print("¡Hasta luego!")
              time.sleep(1)
              Helpers.limpiar_pantalla
              break
            else:
              print("Por favor, ingresa 'si' o 'no'.")
              time.sleep(1)
              Helpers.limpiar_pantalla
      def continuar(funcion_a_escoger):
           Dibujos.osint_cl
           Helpers.limpiar_pantalla
           Dibujos.osint_cl
           while True:
             respuesta = input("¿Quieres generar otro rut? (si/no): ")
             if respuesta.lower() == 'si':
                 Helpers.limpiar_pantalla
                 Dibujos.osint_cl
                 print("Tu Rut generado  es", funcion_a_escoger())
                 time.sleep(1)
                 True
             elif respuesta.lower() == 'no':
                  print("¡Hasta luego!")
                  time.sleep(0.8)
                  Helpers.limpiar_pantalla
                  break
             else:
                 print("Respuesta inválida. Por favor, responde 'si' para continuar o 'no' para salir.")