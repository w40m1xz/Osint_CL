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


#  Funciones
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
        else:
            print("Error al realizar la solicitud:", response.status_code)
#limpiar pantalla
def limpiar_pantalla():
     sistema_operativo = os.name
     if sistema_operativo == 'nt':  # Windows
        os.system('cls')
     else:  # Unix/Linux/MacOS
        os.system('clear')

# ctrl + c
def def_handler(sig, frame):
    print(colored(f"\n\n[!]Saliendo...\n",'red'))
    sys.exit(0)

# Asociar el manejador de señal a la señal SIGINT (Ctrl + C)
signal.signal(signal.SIGINT, def_handler)

# Repetir
def continuar(funcion_a_escoger):
      while True:
        respuesta = input("¿Quieres generar otro rut? (si/no): ")
        if respuesta.lower() == 'si':
                 limpiar_pantalla() 
                 osint_cl
                 print("Tu número generado al azar es", funcion_a_escoger())
        elif respuesta.lower() == 'no':
          print("¡Hasta luego!")
          break
        else:
            print("Respuesta inválida. Por favor, responde 'si' para continnouar o 'no' para salir.")
            time.sleep(0.8)
            limpiar_pantalla()
def continuar_two(tu_rut):
    while True:
        respuesta = input("¿Quieres buscar otro rut? (si/no): ")
        if respuesta.lower() == 'si':
            limpiar_pantalla() 
            osint_cl()  # Llamar a la función para mostrar el diseño
            tu_rut = input("Ingresa un rut que deseas buscar: ")
            Peticion_De_rut(tu_rut)  # Llamar a la función con el RUT proporcionado
        elif respuesta.lower() == 'no':
            print("¡Hasta luego!")
            break
        else:
            print("Respuesta inválida. Por favor, responde 'si' para continuar o 'no' para salir.")
            time.sleep(0.8)
            limpiar_pantalla()

# Menu Principal

def mostrar_menu():
    print("Menú:")
    print("1.Buscar un rut")
    print("2.Genera tu rut al azar")
    print("3.Generar tu rut con parametros")
    print("4.Generar lotes de rut")
    print("5.Salir")

#-------------------------------------------------------------------------------------------------------------------------
#funciones  para generar rut numero al azar

# generar el primer numero A ejemplo: 19.

def primer_numero_azar():
 return random.randint(1, 25)


# Generar 3 numeros al azar
def generar_tres_numero_azar():
 a = random.randint(0, 9)
 b = random.randint(0, 9)
 c = random.randint(0, 9)
 numero_azar = str(a) + str(b) + str(c) 
 return numero_azar

# el ultimo numero del rut al azar
def ultimo_number():
    aleatorio = random.randint(0, 10)
    # Si el número es 10, seleccionar 'K', de lo contrario, seleccionar un número aleatorio entre 0 y 9
    if aleatorio == 10:
        return 'K'
    else:
        return aleatorio

# generar tu rut al azar
def numero_aleatorio():
    # Definiendo los valores llamándolos desde fuera
    one_number = primer_numero_azar()
    three_number_one = generar_tres_numero_azar()
    three_number_two = generar_tres_numero_azar()
    last_number = ultimo_number()

    # Formateando el RUT con punto y guión
    if last_number == 'K':  # Si el último número es 'K'
        Rut_azar_genetor = "{:02d}{:03d}{:03d}-K".format(int(one_number), int(three_number_one), int(three_number_two))
    else:  # Si el último número es 0 o 1
        Rut_azar_genetor = "{:02d}{:03d}{:03d}-{:01d}".format(int(one_number), int(three_number_one), int(three_number_two), last_number)

    Rut_azar_formateado = Rut_azar_genetor[:2] + '.' + Rut_azar_genetor[2:5] + '.' + Rut_azar_genetor[5:8] + '-' + Rut_azar_genetor[9:]

    return Rut_azar_formateado

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
# elegir tu numero de primer digito 
def numero_opcional_uno():
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
# el ultimo numero opcional
def ultimo_numero_opcional():
    while True:
        try:
            osint_cl()
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
                    limpiar_pantalla()
                    
        except ValueError:
            print("Por favor, ingresa un número válido o 'K'.")
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# tu rut con parametros

def crear_numero_con_parametros():
    # Llamando a las funciones
    opc_answer_one = ""
    opc_answer_two = ""
    respuesta_primer_numero = ""    
    respuesta_ultimo_numero = ""

    while True:
        try: 
            osint_cl
            opc_answer_one = input("¿Desea elegir el primer número de tu rut? (si/no): ").lower()
            time.sleep(0.8)
            limpiar_pantalla()
            osint_cl()
            if opc_answer_one == "si":
                print("Has elegido 'si'.")
                limpiar_pantalla()
                osint_cl()
                respuesta_primer_numero = numero_opcional_uno()
                time.sleep(1.3)
                limpiar_pantalla()
            elif opc_answer_one == "no":
                print("Has elegido 'no'.")
                limpiar_pantalla()
                respuesta_primer_numero = primer_numero_azar()
            else:
                osint_cl
                print("Respuesta inválida. Por favor, ingresa 'si' o 'no'.")
                limpiar_pantalla()
                continue
            osint_cl()
            opc_answer_two = input("¿Desea elegir el último número de tu rut (si/no): ").lower()
            time.sleep(0.8)
            limpiar_pantalla()
            if opc_answer_two == "si":
                print("Has elegido 'si'.")
                limpiar_pantalla()
                respuesta_ultimo_numero = ultimo_numero_opcional()
                time.sleep(1.3)
                limpiar_pantalla()
            elif opc_answer_two == "no":
                print("Has elegido 'no'.")
                respuesta_ultimo_numero = ultimo_number()
                limpiar_pantalla()
            else:
                limpiar_pantalla()
                osint_cl()
                print("Respuesta inválida. Por favor, ingresa 'si' o 'no'.")
                continue

            break  # Salir del bucle while cuando se han ingresado las respuestas correctas
        
        except ValueError:
            print("Respuesta inválida. Por favor, ingresa un número válido.")

    azar_two = generar_tres_numero_azar()
    azar_three = generar_tres_numero_azar()

    if respuesta_ultimo_numero == 'K':
        respuesta_ultimo_numero = 'K'
    else:
        respuesta_ultimo_numero = str(respuesta_ultimo_numero)

    rut_con_parametro_final = "{:02d}{:03d}{:03d}-{}".format(int(respuesta_primer_numero), int(azar_two), int(azar_three), respuesta_ultimo_numero)
    rut_con_parametro_final_formateado = "{}.{}.{}-{}".format(rut_con_parametro_final[:2], rut_con_parametro_final[2:5], rut_con_parametro_final[5:8], rut_con_parametro_final[9:12])
    return rut_con_parametro_final_formateado
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#dibujos
def dibujo_calavera():
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


def by_ruisu():
 print(r''' ____                     _           
 |  _ \                   (_)          
 | |_) |_   _   _ __ _   _ _ ___ _   _ 
 |  _ <| | | | | '__| | | | / __| | | |
 | |_) | |_| | | |  | |_| | \__ \ |_| |
 |____/ \__, | |_|   \__,_|_|___/\__,_|
         __/ |                         
        |___/                          
                                     ''')

def osint_cl():
    print("""

 ██████  ███████ ██ ███    ██ ████████       ██████ ██      
██    ██ ██      ██ ████   ██    ██         ██      ██      
██    ██ ███████ ██ ██ ██  ██    ██         ██      ██      
██    ██      ██ ██ ██  ██ ██    ██         ██      ██      
 ██████  ███████ ██ ██   ████    ██ ███████  ██████ ███████ 
                                                            
                                       """)                     

#--------------------------------------------------------------------------------------------------------------
# ACA EMPIEZA EL PROGAMA
    
def main():
    while True:
        dibujo_calavera()
        by_ruisu()
        time.sleep(1)
        limpiar_pantalla()
        osint_cl()
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
       
         # Opción 1: Buscar un rut
        if opcion == "1":
          limpiar_pantalla()
          time.sleep(0.8)
          osint_cl()
          tu_rut = input("Ingresa un rut que deseas buscar: ")
          Peticion_De_rut(tu_rut)
          continuar_two(tu_rut)
        # Opción 2: Elegir un RUT al azar
        elif opcion == "2":
            print("Has seleccionado la Opción 2.")
            limpiar_pantalla()
            time.sleep(0.8)
            print("Tu número generado al azar es", numero_aleatorio())
            continuar(numero_aleatorio)
            limpiar_pantalla()

        # Opción 3: Elegir un RUT con parámetros
        elif opcion == "3":
            print("Has seleccionado la Opción 3.")
            limpiar_pantalla()
            time.sleep(0.8)
            osint_cl()  # Llamar a osint_cl() después de limpiar la pantalla
            print("Tu número generado con parametros es", crear_numero_con_parametros())
            continuar(crear_numero_con_parametros)
            osint_cl
            limpiar_pantalla()  # Llamar a limpiar_pantalla() con paréntesis

            pass  # Implementa la lógica para esta opción aquí

        # Opción 4: Elegir un número telefónico al azar
        elif opcion == "4":
            pass  # Implementa la lógica para esta opción aquí

        # Opción 5: Salir
        elif opcion == "5":
            print("¡Hasta luego!")
            break  # Salir del bucle después de seleccionar la Opción 4

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()