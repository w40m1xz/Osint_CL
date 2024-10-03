import signal
from threading import Thread
from Modules.Osint_Menu import *
from Modules.Utilities import Helpers


def main_menu():
    while True:
        print("\nMenú Principal")
        print("1.Buscar a una persona")
        print("2. SUB MENU 2")
        print("3. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            Search_Person()
        elif choice == "2":
            submenu_2()
        elif choice == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

def Search_Person():
    while True:
        print("\nSubmenú 1")
        print("1. Buscar a una persona por su Rut")
        print("2. Opción 1.2")
        print("3. Regresar al Menú Principal")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            print("Has seleccionado la Opción 1.1")
            # Lógica para la Opción 1.1
        elif choice == "2":
            print("Has seleccionado la Opción 1.2")
            # Lógica para la Opción 1.2
        elif choice == "3":
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

def submenu_2():
    while True:
        print("\nSubmenú 2")
        print("1. Opción 2.1")
        print("2. Opción 2.2")
        print("3. Regresar al Menú Principal")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            print("Has seleccionado la Opción 2.1")
            # Lógica para la Opción 2.1
        elif choice == "2":
            print("Has seleccionado la Opción 2.2")
            # Lógica para la Opción 2.2
        elif choice == "3":
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

