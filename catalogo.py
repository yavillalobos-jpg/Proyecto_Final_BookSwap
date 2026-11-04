# LISTA ENLAZADA SIMPLE: cada nodo representa un libro.
# NodoLibro solamente construye los nodos; las operaciones son funciones.
from entradas import leer_texto, leer_entero

class NodoLibro:
    def __init__(self, codigo, titulo, autor, propietario, universidad,
                 modalidad, precio, carrera="Sin especificar"):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.propietario = propietario
        self.universidad = universidad
        self.carrera = carrera
        self.modalidad = modalidad
        self.precio = precio
        self.prestado_a = ""
        self.universidad_prestatario = ""
        self.cola = []
        self.siguiente = None


def agregar_libro(cabeza, nuevo):
    if cabeza is None:
        return nuevo
    actual = cabeza
    while actual.siguiente is not None:
        actual = actual.siguiente
    actual.siguiente = nuevo
    return cabeza


def buscar_codigo(cabeza, codigo):
    actual = cabeza
    while actual is not None:
        if actual.codigo == codigo:
            return actual
        actual = actual.siguiente
    return None


def quitar_libro(cabeza, codigo):
    anterior = None
    actual = cabeza
    while actual is not None:
        if actual.codigo == codigo:
            if anterior is None:
                return actual.siguiente
            anterior.siguiente = actual.siguiente
            return cabeza
        anterior = actual
        actual = actual.siguiente
    return cabeza


def publicar_libro(cabeza):
    codigo = leer_entero("Código del libro: ")
    if buscar_codigo(cabeza, codigo) is not None:
        print("Ese código ya existe.")
        return cabeza
    titulo = leer_texto("Título: ")
    autor = leer_texto("Autor: ")
    propietario = leer_texto("Nombre del propietario: ")
    universidad = leer_texto("Universidad del propietario: ")
    carrera = leer_texto("Carrera o área del libro: ")
    print("1. Venta   2. Intercambio   3. Préstamo")
    opcion = input("Modalidad: ").strip()
    while opcion not in ["1", "2", "3"]:
        opcion = input("Seleccione 1, 2 o 3: ").strip()
    precio = 0
    if opcion == "1":
        modalidad = "Venta"
        precio = leer_entero("Precio en córdobas enteros: ")
    elif opcion == "2":
        modalidad = "Intercambio"
    else:
        modalidad = "Préstamo"
    nuevo = NodoLibro(codigo, titulo, autor, propietario, universidad,
                      modalidad, precio, carrera)
    cabeza = agregar_libro(cabeza, nuevo)
    print("Libro publicado.")
    return cabeza


def mostrar_libro(libro):
    print("----------------------------------------")
    print("Código:", libro.codigo, "| Título:", libro.titulo)
    print("Autor:", libro.autor)
    print("Propietario:", libro.propietario)
    print("Universidad:", libro.universidad)
    print("Carrera:", libro.carrera)
    print("Modalidad:", libro.modalidad)
    if libro.modalidad == "Venta":
        print("Precio: C$", libro.precio)
    if libro.prestado_a == "":
        print("Estado: Disponible")
    else:
        print("Prestado a:", libro.prestado_a,
              "| Universidad:", libro.universidad_prestatario)


def mostrar_catalogo(cabeza):
    if cabeza is None:
        print("No hay libros publicados.")
    actual = cabeza
    while actual is not None:
        mostrar_libro(actual)
        actual = actual.siguiente


def buscar_libros(cabeza):
    texto = leer_texto("Título, autor, universidad o carrera que desea buscar: ").lower()
    actual = cabeza
    encontrados = 0
    while actual is not None:
        if (texto in actual.titulo.lower() or texto in actual.autor.lower()
                or texto in actual.universidad.lower()
                or texto in actual.carrera.lower()):
            mostrar_libro(actual)
            encontrados += 1
        actual = actual.siguiente
    if encontrados == 0:
        print("No se encontraron libros.")


def eliminar_publicacion(cabeza):
    codigo = leer_entero("Código del libro que desea eliminar: ")
    libro = buscar_codigo(cabeza, codigo)
    if libro is None:
        print("No existe ese libro.")
    elif libro.prestado_a != "" or len(libro.cola) > 0:
        print("No puede eliminar un libro prestado o con solicitudes pendientes.")
    else:
        cabeza = quitar_libro(cabeza, codigo)
        print("Publicación eliminada.")
    return cabeza