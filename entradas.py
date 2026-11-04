# CADENAS: lectura y validación de los datos escritos por el usuario.

def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        # El símbolo | separa los campos dentro de los archivos.
        if texto != "" and "|" not in texto:
            return texto
        print("Escriba un texto que no esté vacío ni contenga el símbolo |.")


def leer_entero(mensaje):
    while True:
        texto = input(mensaje).strip()
        try:
            numero = int(texto)
            if numero > 0:
                return numero
        except ValueError:
            pass
        print("Escriba un número entero mayor que cero.")

