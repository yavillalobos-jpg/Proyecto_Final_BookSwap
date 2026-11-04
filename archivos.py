# Las posiciones de cada nodo están explicadas en catalogo.py.
# ARCHIVOS: guardar y recuperar libros y solicitudes.
# Los .txt se guardan en la carpeta desde la que se ejecuta el programa.
from catalogo import crear_nodo, agregar_libro, buscar_codigo

def guardar_datos(cabeza):
    with open("libros.txt", "w", encoding="utf-8") as archivo:
        actual = cabeza
        while actual is not None:
            campos = [str(actual[0]), actual[1], actual[2],
                      actual[3], actual[4], actual[5],
                      str(actual[6]), actual[7],
                      actual[8], actual[9], actual[10],
                      actual[11], actual[12],
                      str(actual[13])]
            archivo.write("|".join(campos) + "\n")
            actual = actual[15]
    with open("solicitudes.txt", "w", encoding="utf-8") as archivo:
        actual = cabeza
        while actual is not None:
            for solicitud in actual[14]:
                archivo.write(str(actual[0]) + "|" + solicitud[0]
                              + "|" + solicitud[1] + "\n")
            actual = actual[15]


def cargar_datos():
    cabeza = None
    try:
        # Solo usamos los ejemplos si aún no existe un catálogo guardado.
        # Un catálogo guardado vacío debe permanecer vacío.
        try:
            archivo_libros = open("libros.txt", "r", encoding="utf-8")
        except FileNotFoundError:
            archivo_libros = open("libros_ejemplo.txt", "r", encoding="utf-8")
        with archivo_libros as archivo:
            for linea in archivo:
                campos = linea.rstrip("\n").split("|")
                nuevo = crear_nodo(int(campos[0]), campos[1], campos[2],
                                  campos[3], campos[4], campos[5], int(campos[6]))
                nuevo[7] = campos[7]
                nuevo[8] = campos[8]
                # También podemos leer los archivos de la versión anterior.
                if len(campos) > 9:
                    nuevo[9] = campos[9]
                if len(campos) > 10:
                    nuevo[10] = campos[10]
                    nuevo[11] = campos[11]
                    nuevo[12] = campos[12]
                    nuevo[13] = int(campos[13])
                cabeza = agregar_libro(cabeza, nuevo)
    except FileNotFoundError:
        # Si no existen datos guardados ni ejemplos, iniciamos sin libros.
        pass
    try:
        with open("solicitudes.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                campos = linea.rstrip("\n").split("|")
                libro = buscar_codigo(cabeza, int(campos[0]))
                if libro is not None:
                    libro[14].append([campos[1], campos[2]])
    except FileNotFoundError:
        pass
    return cabeza

