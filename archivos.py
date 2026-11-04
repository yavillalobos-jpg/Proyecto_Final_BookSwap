# ARCHIVOS: guardar y recuperar libros y solicitudes.
# Los .txt se guardan en la carpeta desde la que se ejecuta el programa.
from catalogo import NodoLibro, agregar_libro, buscar_codigo

def guardar_datos(cabeza):
    with open("libros.txt", "w", encoding="utf-8") as archivo:
        actual = cabeza
        while actual is not None:
            campos = [str(actual.codigo), actual.titulo, actual.autor,
                      actual.propietario, actual.universidad, actual.modalidad,
                      str(actual.precio), actual.prestado_a,
                      actual.universidad_prestatario, actual.carrera, actual.estado,
                      actual.destinatario, actual.universidad_destinatario,
                      str(actual.codigo_intercambio)]
            archivo.write("|".join(campos) + "\n")
            actual = actual.siguiente
    with open("solicitudes.txt", "w", encoding="utf-8") as archivo:
        actual = cabeza
        while actual is not None:
            for solicitud in actual.cola:
                archivo.write(str(actual.codigo) + "|" + solicitud[0]
                              + "|" + solicitud[1] + "\n")
            actual = actual.siguiente


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
                nuevo = NodoLibro(int(campos[0]), campos[1], campos[2],
                                  campos[3], campos[4], campos[5], int(campos[6]))
                nuevo.prestado_a = campos[7]
                nuevo.universidad_prestatario = campos[8]
                # También podemos leer los archivos de la versión anterior.
                if len(campos) > 9:
                    nuevo.carrera = campos[9]
                if len(campos) > 10:
                    nuevo.estado = campos[10]
                    nuevo.destinatario = campos[11]
                    nuevo.universidad_destinatario = campos[12]
                    nuevo.codigo_intercambio = int(campos[13])
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
                    libro.cola.append([campos[1], campos[2]])
    except FileNotFoundError:
        pass
    return cabeza
