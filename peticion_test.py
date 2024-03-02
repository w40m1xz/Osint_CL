import requests
from bs4 import BeautifulSoup


# con el sitio rutificador 
# URL a la que deseas enviar la solicitud POST
url = 'https://www.nombrerutyfirma.com/rut'

input_save = input("Ingresa el RUT que quieres: ")

# Datos a enviar en la solicitud POST
data = {
    'term': input_save  # Puedes cambiar este rut por cualquier otro que desees buscar
}

# Realizar la solicitud POST
response = requests.post(url, data=data)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    print("Solicitud exitosa!")

    # Crear un objeto BeautifulSoup para analizar el HTML de la respuesta
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar la tabla que contiene los resultados
    tabla_resultados = soup.find('table', class_='table table-hover')

    # Verificar si se encontró la tabla
    if tabla_resultados:
        # Encontrar la fila que contiene los datos del primer resultado
        fila_resultado = tabla_resultados.find('tr', tabindex='1')

        # Verificar si se encontró la fila del resultado
        if fila_resultado:
            # Encontrar todas las celdas de la fila
            celdas_resultado = fila_resultado.find_all('td')

            # Obtener el nombre, RUT, Sexo, Dirección y Ciudad/Comuna del primer resultado
            nombre = celdas_resultado[0].text.strip()
            rut = celdas_resultado[1].text.strip()
            sexo = celdas_resultado[2].text.strip()
            direccion = celdas_resultado[3].text.strip()
            ciudad_comuna = celdas_resultado[4].text.strip()

            # Imprimir los detalles
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
