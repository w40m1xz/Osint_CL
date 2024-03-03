#!/usr/bin/python3
import random
import time
import os
import signal
import sys
from termcolor import colored
#Progama 2.0
#  Funciones

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
        respuesta = input("¿Quieres generar otro número aleatorio? (s/n): ")
        if respuesta.lower() == 's':
                 limpiar_pantalla()
                 osint_cl()
                 print("Tu número generado al azar es", funcion_a_escoger())
        elif respuesta.lower() == 'n':
          print("¡Hasta luego!")
          break
        else:
            print("Respuesta inválida. Por favor, responde 's' para continnouar o 'n' para salir.")

# Menu Principal

def mostrar_menu():
    print("Menú:")
    print("1. Genera tu rut al azar")
    print("2. Generar tu rut con parametros")
    print("3. Opción 3")
    print("4. Salir")

#-------------------------------------------------------------------------------------------------------------------------
#funciones  para generar rut numero al azar

# generar el primer numero A ejemplo: 19.

def primer_numero_azar():
 return random.randint(1, 25)
one_number=primer_numero_azar()

# Generar 3 numeros al azar
def generar_tres_numero_azar():
 a = random.randint(0, 9)
 b = random.randint(0, 9)
 c = random.randint(0, 9)
 numero_azar = str(a) + str(b) + str(c) 
 return numero_azar
three_number_one= generar_tres_numero_azar
three_number_two = generar_tres_numero_azar

# el ultimo numero del rut al azar
def ultimo_number():
    aleatorio = random.randint(0, 10)
    # Si el número es 10, seleccionar 'K', de lo contrario, seleccionar un número aleatorio entre 0 y 9
    if aleatorio == 10:
        return 'K'
    else:
        return aleatorio
  
last_number = ultimo_number()

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

azar = numero_aleatorio()


azar= numero_aleatorio()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
# elegir tu numero de primer digito 
def numero_opcional_uno():
    while True:
        try:
            numero = int(input("Por favor, ingresa un número: 1 al 25: "))
            if 1 <= numero <= 25:
                break
            else:
                print("El número debe estar entre 1 y 25. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return numero

numero_uno_opcional=numero_opcional_uno

#elegir el ultimo numero o k de tu rut
def ultimo_numero_opcional():
    while True:
        try:
            entrada_final = input("Por favor, ingresa un número del 1 al 9 o 'K': ")
            if entrada_final.upper() == 'K':
                return 'K'
            else:
                numero = int(entrada_final)
                if 1 <= numero <= 9:
                    return numero
                else:
                    print("El número debe estar entre 1 y 9. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido o 'K'.")
    
numero_uno_opcional2=numero_opcional_uno
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

        # Opción 1: Elegir un RUT al azar
        if opcion == "1":
            print("Has seleccionado la Opción 1.")
            limpiar_pantalla()
            time.sleep(0.8)
            osint_cl()
            print("Tu número generado al azar es", numero_aleatorio())
            #time.sleep(7)
            continuar(numero_aleatorio)
            limpiar_pantalla()

        # Opción 2: Elegir un RUT con parámetros
        elif opcion == "2":
            pass  # Implementa la lógica para esta opción aquí

        # Opción 3: Elegir un número telefónico al azar
        elif opcion == "3":
            pass  # Implementa la lógica para esta opción aquí

        # Opción 4: Salir
        elif opcion == "4":
            print("¡Hasta luego!")
            break  # Salir del bucle después de seleccionar la Opción 4

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()