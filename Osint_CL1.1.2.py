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

#Bylucho

# Clase que proporciona funciones útiles para realizar operaciones de OSINT
class Osint:    
    class Funciones: 
      def continuar_buscando_rut(self):
        self.dibujo = Osint.Dibujos()
        self.limpiar_pantalla()
        self.dibujo.osint_cl()
        while True:
            respuesta = input("¿Quieres buscar otro RUT? (si/no): ")
            if respuesta == 'si':
              self.limpiar_pantalla()
              self.dibujo.osint_cl()
              rut_verificado= self.validar_rut()
              self.buscador_de_rut(rut_verificado)
              input("Presiona Enter para continuar...")
            elif respuesta.lower() == 'no':
              print("¡Hasta luego!")
              time.sleep(1)
              self.limpiar_pantalla()
              break
            else:
              print("Por favor, ingresa 'si' o 'no'.")
              time.sleep(1)
              self.limpiar_pantalla()      
      def buscador_de_rut(self,rut):
        url = 'https://www.nombrerutyfirma.com/rut'
        headers = {
            'Host': 'www.nombrerutyfirma.com',
            'Cookie': 'cf_clearance=DuWwsI1Jk_E5A0UBh_tPzpwyCANkrz.mbNv9NzE286E-1709514440-1.0.1.1-Gofv6W1hJ17Hop9dIpvsVSBJFRvJorbhCHQ64v3jiS7q_2CeQbJYKWnu0uJKdT_qfKFdcQi7M6.yBpgafdI1Ow',
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
      def validar_rut(self):
        self.dibujo= Osint.Dibujos()
        while True:
            self.dibujo.osint_cl
            rut = input("Ingresa un RUT en el formato xx.xxx.xxx-k (Solo números y último dígito 0-9 o K): ")
            patron_rut = r'^(25|[1-9]|[1][0-9]|2[0-5])\.\d{3}\.\d{3}-[\dkK0-9]$'
            if re.match(patron_rut, rut):
                break
            else:
                print("El RUT ingresado no tiene el formato correcto. Inténtalo nuevamente.")
                time.sleep(1)
                self.limpiar_pantalla()
                self.dibujo.osint_cl()
        return rut
      def limpiar_pantalla(self):
            sistema_operativo = os.name
            if sistema_operativo == 'nt':  # Windows
               os.system('cls')
            else:  # Unix/Linux/MacOS
             os.system('clear')
      def control_De_salida(self, sig, frame):
          print(colored(f"\n\n[!]Saliendo...\n",'red'))
          sys.exit(0)
      def continuar(self,funcion_a_escoger):
           self.dibujo = Osint.Dibujos()
           self.limpiar_pantalla()
           self.dibujo.osint_cl()
           while True:
             respuesta = input("¿Quieres generar otro rut? (si/no): ")
             if respuesta.lower() == 'si':
                 self.limpiar_pantalla()
                 self.dibujo.osint_cl()
                 print("Tu Rut generado  es", funcion_a_escoger())
                 time.sleep(1)
                 True
             elif respuesta.lower() == 'no':
                  print("¡Hasta luego!")
                  time.sleep(0.8)
                  self.limpiar_pantalla()
                  break
             else:
                 print("Respuesta inválida. Por favor, responde 'si' para continuar o 'no' para salir.")
      def mostrar_menu(self):
            print("Menú:")
            print("1. Buscar un rut")
            print("2. Genera tu rut al azar")
            print("3. Generar tu rut con parametros")
            print("4. Generar lotes de rut")
            print("5. Salir")
    class Numeros:
       def primer_numerorut_azar(self):
         return random.randint(1, 25)
       def generar_tres_numero_azar(self):
           a = random.randint(0, 9)
           b = random.randint(0, 9)
           c = random.randint(0, 9)
           numero_azar = str(a) + str(b) + str(c) 
           return numero_azar
       def ultimo_numerorut_azar(self):
        aleatorio = random.randint(0, 10)
        # Si el número es 10, seleccionar 'K', de lo contrario, seleccionar un número aleatorio entre 0 y 9
        if aleatorio == 10:
         return 'K'
        else:
         return aleatorio
       def primer_numerorut_opcional(self):
        while True:
            try:
              numero = int(input("Por favor, ingresa un número: 1 al 25 para tu primer numero de tu rut: "))
              if 1 <= numero <= 25:
                 break
              else:
                print("El número debe estar entre 1 y 25. Inténtalo de nuevo.")
            except ValueError:
               print("Por favor, ingresa un número válido.")
        return numero
       def ultimo_numerorut_opcional(self):
            while True:
                try:
                   entrada_final = input("Por favor, ingresa un número del 0 al 9 o 'K': ")
                   if entrada_final.upper() == 'K':
                      return 'K'
                   else:
                      entrada_final = int(entrada_final)
                      if 0 <= entrada_final <= 9:
                       return entrada_final
                      else:
                       print("El número debe estar entre 0 y 9. Inténtalo de nuevo.")
                       time.sleep(0.8)
                    
                    
                except ValueError:
                  print("Por favor, ingresa un número válido o 'K'.")      
    class Crear: 
        def __init__(self):
         self.numeros_Intancia = Osint.Numeros()       
        def crear_rut_aleatorio(self):
        # Definiendo los valores llamándolos desde fuera
         one_number = self.numeros_Intancia.primer_numerorut_azar()
         three_number_one = self.numeros_Intancia.generar_tres_numero_azar()
         three_number_two = self.numeros_Intancia.generar_tres_numero_azar()
         last_number = self.numeros_Intancia.ultimo_numerorut_azar()

         # Formateando el RUT con punto y guión
         if last_number == 'K':  # Si el último número es 'K'
             Rut_azar_genetor = "{:02d}{:03d}{:03d}-K".format(int(one_number), int(three_number_one), int(three_number_two))
         else:  # Si el último número es 0 o 1
             Rut_azar_genetor = "{:02d}{:03d}{:03d}-{:01d}".format(int(one_number), int(three_number_one), int(three_number_two), last_number)
        
         Rut_azar_formateado = Rut_azar_genetor[:2] + '.' + Rut_azar_genetor[2:5] + '.' + Rut_azar_genetor[5:8] + '-' + Rut_azar_genetor[9:]
        
         return Rut_azar_formateado
        def crear_numero_con_parametros(self): 
         # se Defines la variable
         azar_two = self.numeros_Intancia.generar_tres_numero_azar()
         azar_three = self.numeros_Intancia.generar_tres_numero_azar()
         #Definiendo la la funciones de la otras clases
         self.dibujo = Osint.Dibujos()
         self.funcion = Osint.Funciones()
         # limpiamos y dibujamos osint
         self.funcion.limpiar_pantalla()
         self.dibujo.osint_cl()
         while True:
            try: 
                # elegir tu primer dígito del rut
                opc_answer_one = input("¿Desea elegir el primer número de tu rut? (si/no): ").lower()
                time.sleep(0.8)
                if opc_answer_one == "si":
                    print("Has elegido 'si'.")
                    time.sleep(0.8)
                    self.funcion.limpiar_pantalla()
                    self.dibujo.osint_cl()
                    respuesta_primer_numero = self.numeros_Intancia.primer_numerorut_opcional()
                    time.sleep(1.3)
                    self.funcion.limpiar_pantalla()
                elif opc_answer_one == "no":
                    print("Has elegido 'no'.")
                    time.sleep(0.8)
                    self.funcion.limpiar_pantalla()
                    respuesta_primer_numero = self.numeros_Intancia.primer_numerorut_azar()
                else:
                    print("Respuesta inválida. Por favor, ingresa 'si' o 'no'.")
                    continue
                 
                # elegir tu último dígito del rut
                self.dibujo.osint_cl()
                opc_answer_two = input("¿Desea elegir el último número de tu rut (si/no): ").lower()
                time.sleep(0.8)
                if opc_answer_two == "si":
                    print("Has elegido 'si'.")
                    time.sleep(0.8)
                    self.funcion.limpiar_pantalla()
                    self.dibujo.osint_cl()
                    respuesta_ultimo_numero = self.numeros_Intancia.ultimo_numerorut_opcional()
                    time.sleep(1.3)
                    self.funcion.limpiar_pantalla()
                elif opc_answer_two == "no":
                    print("Has elegido 'no'.")
                    time.sleep(0.8)
                    self.funcion.limpiar_pantalla()
                    self.dibujo.osint_cl
                    respuesta_ultimo_numero = self.numeros_Intancia.ultimo_numerorut_azar()
                else:
                    print("Respuesta inválida. Por favor, ingresa 'si' o 'no'.")
                    continue
                rut_con_parametro_final = "{:02d}{:03d}{:03d}-{}".format(int(respuesta_primer_numero), int(azar_two), int(azar_three), respuesta_ultimo_numero if isinstance(respuesta_ultimo_numero, int) else 'K')
                rut_con_parametro_final_formateado = "{}.{}.{}-{}".format(rut_con_parametro_final[:2], rut_con_parametro_final[2:5], rut_con_parametro_final[5:8], rut_con_parametro_final[9:])
                return rut_con_parametro_final_formateado

            except ValueError:
                print("Respuesta inválida. Por favor, ingresa un número válido.")
    class Dibujos:
        def dibujo_calavera(self):
         print('''
                ███████████████████████████
                ███████▀▀▀░░░░░░░▀▀▀███████
                ████▀░░░░░░░░░░░░░░░░░▀████  
                ███│░░░░░░░░░░░░░░░░░░░│███
                ██▌│░░░░░░░░░░░░░░░░░░░│▐██
                ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
                ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
                ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
                ██▌░│██████▌░░░▐██████│░▐██
                ███░│▐███▀▀░░▄░░▀▀███▌│░███
                ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
                ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
                ████▄─┘██▌░░░░░░░▐██└─▄████ 
                █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
                ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
                █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
                ███████▄░░░░░░░░░░░▄███████
                ██████████▄▄▄▄▄▄▄██████████
                ███████████████████████████
                         ''')
        def by_ruisu(self):
         print(r'''           
          ____                     _           
         |  _ \                   (_)          
         | |_) |_   _   _ __ _   _ _ ___ _   _ 
         |  _ <| | | | | '__| | | | / __| | | |
         | |_) | |_| | | |  | |_| | \__ \ |_| |
         |____/ \__, | |_|   \__,_|_|___/\__,_|
                 __/ |                         
                |___/                          
                                     ''')
        def osint_cl(self):
            print("""
            ██████  ███████ ██ ███    ██ ████████       ██████ ██      
           ██    ██ ██      ██ ████   ██    ██         ██      ██      
           ██    ██ ███████ ██ ██ ██  ██    ██         ██      ██      
           ██    ██      ██ ██ ██  ██ ██    ██         ██      ██      
            ██████  ███████ ██ ██   ████    ██ ███████  ██████ ███████ 
                                                                       
                                       """)                     
# El Progama inicia aca 
def main():
    # Creando una instancia de las clases
    mifunciones = Osint.Funciones()
    crear = Osint.Crear()
    dibujo = Osint.Dibujos()
    signal.signal(signal.SIGINT, mifunciones.control_De_salida)
    
    while True:  # Bucle principal para mantener el menú en ejecución
        # Inicio del menú
        dibujo.dibujo_calavera()
        time.sleep(0.4)
        dibujo.by_ruisu()
        time.sleep(2)
        mifunciones.limpiar_pantalla()
        dibujo.osint_cl()
        mifunciones.mostrar_menu()

        # Selección de opción
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            time.sleep(0.8)
            mifunciones.limpiar_pantalla()
            dibujo.osint_cl()
            rut_validado = mifunciones.validar_rut()
            mifunciones.buscador_de_rut(rut_validado)
            input("Presiona Enter para continuar...")
            time.sleep(0.8)
            mifunciones.continuar_buscando_rut()

        elif opcion == "2":
            mifunciones.limpiar_pantalla()
            time.sleep(0.8)
            dibujo.osint_cl()
            print("Tu Rut generado al azar es", crear.crear_rut_aleatorio())
            time.sleep(0.8)
            mifunciones.continuar(crear.crear_rut_aleatorio)

        elif opcion == "3":
            mifunciones.limpiar_pantalla()
            time.sleep(0.8)
            dibujo.osint_cl()   
            rut_generado = crear.crear_numero_con_parametros()
            print("Tu número generado con parámetros es", rut_generado)
            input("Presiona Enter para continuar...")
            dibujo.osint_cl()
            mifunciones.continuar(crear.crear_numero_con_parametros)

        elif opcion == "4":
            pass  # Implementa la lógica para esta opción aquí

        elif opcion == "5":
            print("¡Hasta luego!")
            break  # Salir del bucle principal y terminar el programa

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
            mifunciones.limpiar_pantalla()
if __name__ == "__main__":
    main()
