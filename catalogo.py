# LISTA ENLAZADA SIMPLE: cada nodo representa un libro.
# Los nodos son listas de Python; las operaciones son funciones.
from entradas import leer_texto, leer_entero

# Cada nodo es una lista con estas posiciones:
# 0 código, 1 título, 2 autor, 3 propietario, 4 universidad,
# 5 modalidad, 6 precio, 7 prestatario, 8 universidad del prestatario,
# 9 carrera, 10 estado, 11 destinatario, 12 universidad del destinatario,
# 13 código del libro intercambiado, 14 cola, 15 enlace al siguiente nodo.
# La cabeza apunta al primer nodo; None indica el final.
# IMPORTANTE: nodo[15] guarda el siguiente nodo, no su código.
def crear_nodo(codigo, titulo, autor, propietario, universidad,
               modalidad, precio, carrera="Sin especificar"):
    return [codigo, titulo, autor, propietario, universidad,
            modalidad, precio, "", "", carrera, "Disponible", "", "", 0, [], None]


def agregar_libro(cabeza, nuevo):
    if cabeza is None:
        return nuevo
    actual = cabeza
    while actual[15] is not None:
        actual = actual[15]
    actual[15] = nuevo
    return cabeza


def buscar_codigo(cabeza, codigo):
    actual = cabeza
    while actual is not None:
        if actual[0] == codigo:
            return actual
        actual = actual[15]
    return None


def quitar_libro(cabeza, codigo):
    anterior = None
    actual = cabeza
    while actual is not None:
        if actual[0] == codigo:
            if anterior is None:
                return actual[15]
            anterior[15] = actual[15]
            return cabeza
        anterior = actual
        actual = actual[15]
    return cabeza


def publicar_libro(cabeza, modalidad):
    codigo = leer_entero("Código del libro: ")
    if buscar_codigo(cabeza, codigo) is not None:
        print("Ese código ya existe.")
        return cabeza
    titulo = leer_texto("Título: ")
    autor = leer_texto("Autor: ")
    propietario = leer_texto("Nombre del propietario: ")
    universidad = leer_texto("Universidad del propietario: ")
    carrera = leer_texto("Carrera o área del libro: ")
    precio = 0
    if modalidad == "Venta":
        precio = leer_entero("Precio en córdobas enteros: ")
    nuevo = crear_nodo(codigo, titulo, autor, propietario, universidad,
                      modalidad, precio, carrera)
    cabeza = agregar_libro(cabeza, nuevo)
    print("Libro publicado.")
    return cabeza


def mostrar_libro(libro):
    print("----------------------------------------")
    print("Código:", libro[0], "| Título:", libro[1])
    print("Autor:", libro[2])
    print("Publicado por:", libro[3])
    print("Universidad:", libro[4])
    print("Carrera:", libro[9])
    print("Modalidad:", libro[5])
    if libro[5] == "Venta":
        print("Precio: C$", libro[6])
    if libro[10] == "Vendido":
        print("Estado: Vendido")
        print("Comprador:", libro[11], "| Universidad:", libro[12])
    elif libro[10] == "Intercambiado":
        print("Estado: Intercambiado por el libro", libro[13])
        print("Entregado a:", libro[11], "| Universidad:", libro[12])
    elif libro[7] == "":
        print("Estado: Disponible")
    else:
        print("Prestado a:", libro[7],
              "| Universidad:", libro[8])


def mostrar_catalogo(cabeza):
    if cabeza is None:
        print("No hay libros publicados.")
    actual = cabeza
    while actual is not None:
        mostrar_libro(actual)
        actual = actual[15]


def buscar_libros(cabeza):
    texto = leer_texto("Título, autor, universidad o carrera que desea buscar: ").lower()
    actual = cabeza
    encontrados = 0
    while actual is not None:
        if (texto in actual[1].lower() or texto in actual[2].lower()
                or texto in actual[4].lower()
                or texto in actual[9].lower()):
            mostrar_libro(actual)
            encontrados += 1
        actual = actual[15]
    if encontrados == 0:
        print("No se encontraron libros.")


def eliminar_publicacion(cabeza):
    codigo = leer_entero("Código del libro que desea eliminar: ")
    libro = buscar_codigo(cabeza, codigo)
    if libro is None:
        print("No existe ese libro.")
    elif libro[7] != "" or len(libro[14]) > 0:
        print("No puede eliminar un libro prestado o con solicitudes pendientes.")
    else:
        cabeza = quitar_libro(cabeza, codigo)
        print("Publicación eliminada.")
    return cabeza
