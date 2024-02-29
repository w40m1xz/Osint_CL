#!/usr/bin/python3

import random
import time
import os

#--------------------------------------------------------------------------------------------------------------------------
#limpiar pantalla
def limpiar_pantalla():
    os.system('clear')

#--------------------------------------------------------------------------------------------------------------------------
# formateo

def formateo_numero(primero, segundo, tercero, cuatro):
    Rut_formateo = "{:02d}{:03d}{:03d}{:01d}".format(primero, segundo, tercero, cuatro)
    Rut_formateo = list(Rut_formateo)  
    Rut_formateo.insert(2, '.')  # Insertar el primer punto
    Rut_formateo.insert(6, '.')  # Insertar el segundo punto
    Rut_formateo.insert(10, '-') # Insertar el guión
    Rut_formateado_final = ''.join(Rut_formateo)
    return Rut_formateado_final


#--------------------------------------------------------------------------------------------------------------------------

# saliendo 


def Saliendo(valor):
    for i in range(valor, 0, -1):
        mensaje = f"Saliendo {i} "
        puntos = "." * i
        print(mensaje + puntos, end='', flush=True)
        time.sleep(0.8)
        print('\b' * (len(mensaje) + len(puntos)), end='', flush=True)
#--------------------------------------------------------------------------------------------------------------------------

# generar el primer numero A ejemplo: 19.
def primer_numero_azar():
  
  return random.randint(1, 25)
#----------------------------------------------------------------------------------------------------------------------------

#generar el segundo numero B ejemplo 394
#----------------------------------------------------------------------------------------------------------------------------
def numero_tres_digitos_azar():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    numero = str(a) + str(b) + str(c) 
    return numero

#----------------------------------------------------------------------------------------------------------------------------
# generar el tecer ultmo digito C  Ejemplo -K  

def ultimo_digito_azar():
    aleatorio = random.randint(0, 10)
    # Si el número es 10, seleccionar 'K', de lo contrario, seleccionar un número aleatorio entre 0 y 9
    if aleatorio == 10:
        return 'K'
    else:
        return aleatorio


#----------------------------------------------------------------------------------------------------------------------------
# elegir tu numero de primer digito A
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
    

#----------------------------------------------------------------------------------------------------------------------------
# elegir el ultimo digito C  ejemplo -k o un numero de 1 al 9
def ultimo_numero_opcional():
    while True:
        try:
            entrada = input("Por favor, ingresa un número del 1 al 9 o 'K': ")
            if entrada.upper() == 'K':
                return 'K'
            else:
                numero = int(entrada)
                if 1 <= numero <= 9:
                    return numero
                else:
                    print("El número debe estar entre 1 y 9. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido o 'K'.")
            
            
#----------------------------------------------------------------------------------------------------------------------------

#EL PROGAMA ACA EMPIEZA !!



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
print(''' ____                     _           
 |  _ \                   (_)          
 | |_) |_   _   _ __ _   _ _ ___ _   _ 
 |  _ <| | | | | '__| | | | / __| | | |
 | |_) | |_| | | |  | |_| | \__ \ |_| |
 |____/ \__, | |_|   \__,_|_|___/\__,_|
         __/ |                         
        |___/                          
                                     ''')
time.sleep(3)
limpiar_pantalla()

print ("Bievenido al progama")

print("""

 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ██████╗  ██████╗ ██████╗     ██████╗ ███████╗    ██████╗ ██╗   ██╗████████╗
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██╔══██╗██╔════╝    ██╔══██╗██║   ██║╚══██╔══╝
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║██║  ██║██║   ██║██████╔╝    ██║  ██║█████╗      ██████╔╝██║   ██║   ██║   
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║██║  ██║██║   ██║██╔══██╗    ██║  ██║██╔══╝      ██╔══██╗██║   ██║   ██║   
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║██████╔╝╚██████╔╝██║  ██║    ██████╔╝███████╗    ██║  ██║╚██████╔╝   ██║   
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚══════╝    ╚═╝  ╚═╝ ╚═════╝    ╚═╝   
                                                                                                                              
      """)


 # Menu Principal

def mostrar_menu():
    print("Menú:")
    print("1. Genera tu rut al azar")
    print("2. Generar tu rut con parametros")
    print("3. Opción 3")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        # Opcion 1 elegir un rut totalmente al azar
        if opcion == "1":
            print("Has seleccionado la Opción 1.")
            limpiar_pantalla()
            azar_primero = primer_numero_azar()
            azar_segundo = numero_tres_digitos_azar()
            azar_tercero = numero_tres_digitos_azar()
            azar_cuarto = ultimo_digito_azar()
            Rut_azar_genetor = "{:02d}{:03d}{:03d}{:01d}".format(azar_primero, int(azar_segundo), int(azar_tercero), azar_cuarto)
            Rut_azar_genetor = list(Rut_azar_genetor)  
            Rut_azar_genetor.insert(2, '.')  # Insertar el primer punto
            Rut_azar_genetor.insert(6, '.')  # Insertar el segundo punto
            Rut_azar_genetor.insert(10, '-') # Insertar el guión
            Rut_azar_formateado = ''.join(Rut_azar_genetor)
            print("Tu rut al azar es:", Rut_azar_formateado)
            Saliendo(7)
            limpiar_pantalla()


        # Opcion 2 elegir un rut totalmente Con parametros  
        elif opcion == "2":
              while True:
                respuesta_opcional = input("¿Deseas elegir el primer parámetro de tu rut? (Sí/No): ").strip().lower()

                if respuesta_opcional == "si":
                  print("Has elegido Sí. Realizando acciones para el primer parámetro...")
                  save_opcional_one= numero_opcional_uno()
                  break
                elif respuesta_opcional == "no":
                   print("Has elegido No. Realizando otras acciones...")
                   save_opcional_one= primer_numero_azar()
                   break
                else:
                    print("Respuesta no válida. Por favor, responde 'Sí' o 'No'.")
                    break
              while True: 
                respuesta_opcional_dos = input("¿Deseas elegir el último parámetro de tu rut? (Sí/No): ").strip().lower()

                if respuesta_opcional_dos == "si":
                   print("Has elegido Sí. Realizando acciones para el último parámetro...")
                   save_opcional_two = ultimo_numero_opcional()
                   break
                elif respuesta_opcional_dos == "no":
                     print("Has elegido No. Realizando otras acciones...")
                     save_opcional_two = ultimo_digito_azar()
                     break
              else:
                    print("Respuesta no válida. Por favor, responde 'Sí' o 'No'.")
                    break
                    azar_segundo = numero_tres_digitos_azar()
                    azar_tercero = numero_tres_digitos_azar()
                    break
               # Rut_azar_genetor = "{:02d}{:03d}{:03d}{:01d}".format(save_opcional_one, int(azar_segundo), int(azar_tercero), save_opcional_two)
              #Rut_azar_formateado = formateo_numero(Rut_azar_genetor)
            

        # Opcion 3
        elif opcion == "3":
            # Código para la Opción 3
            pass

        # Opcion 4: Salir
        elif opcion == "4":
          print("¡Hasta luego!")
         # Sale del bucle while y termina el programa
        pass 
      #----------------------------------------------------------------------------------------------------------------------------      
        #azar_segundo = numero_tres_digitos_azar()
        #azar_tercero = numero_tres_digitos_azar()
       # Rut_azar_genetor = "{:02d}{:03d}{:03d}{:01d}".format(respuesta_opcional, int(azar_segundo), int(azar_tercero), save_opcional_two)
    
    #----------------------------------------------------------------------------------------------------------------------------
     
 #----------------------------------------------------------------------------------------------------------------------------           
# Continua al salir del bucle
if __name__ == "__main__": 
    main()
