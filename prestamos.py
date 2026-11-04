# Las posiciones de cada nodo están explicadas en catalogo.py.
# COLAS FIFO: primero en entrar, primero en salir.
# append agrega al final; pop(0) retira al primero.
from catalogo import buscar_codigo
from entradas import leer_texto, leer_entero

def solicitar_prestamo(cabeza):
    codigo = leer_entero("Código del libro: ")
    libro = buscar_codigo(cabeza, codigo)
    if libro is None:
        print("No existe ese libro.")
        return
    if libro[5] != "Préstamo":
        print("Este libro no está publicado para préstamo.")
        return
    nombre = leer_texto("Nombre del solicitante: ")
    universidad = leer_texto("Universidad del solicitante: ")
    if (nombre.lower() == libro[3].lower()
            and universidad.lower() == libro[4].lower()):
        print("El propietario no puede solicitar su propio libro.")
        return
    if (nombre.lower() == libro[7].lower()
            and universidad.lower() == libro[8].lower()):
        print("Esa persona ya tiene prestado el libro.")
        return
    for solicitud in libro[14]:
        if (solicitud[0].lower() == nombre.lower()
                and solicitud[1].lower() == universidad.lower()):
            print("Esa persona ya está en la cola.")
            return
    libro[14].append([nombre, universidad])
    print("Solicitud registrada. Posición en la cola:", len(libro[14]))


def ver_solicitudes(cabeza):
    actual = cabeza
    cantidad = 0
    while actual is not None:
        if len(actual[14]) > 0:
            print("Libro:", actual[1], "| Código:", actual[0])
            posicion = 1
            for solicitud in actual[14]:
                print(posicion, "-", solicitud[0], "|", solicitud[1])
                posicion += 1
                cantidad += 1
        actual = actual[15]
    if cantidad == 0:
        print("No hay solicitudes pendientes.")


def atender_prestamo(cabeza):
    codigo = leer_entero("Código del libro que se va a prestar: ")
    libro = buscar_codigo(cabeza, codigo)
    if libro is None:
        print("No existe ese libro.")
    elif libro[5] != "Préstamo":
        print("Este libro no está publicado para préstamo.")
    elif libro[7] != "":
        print("Primero debe registrarse la devolución del libro.")
    elif len(libro[14]) == 0:
        print("No hay solicitudes para ese libro.")
    else:
        solicitud = libro[14].pop(0)
        libro[7] = solicitud[0]
        libro[8] = solicitud[1]
        print("Libro prestado a:", libro[7])


def devolver_libro(cabeza):
    codigo = leer_entero("Código del libro devuelto: ")
    libro = buscar_codigo(cabeza, codigo)
    if libro is None:
        print("No existe ese libro.")
    elif libro[7] == "":
        print("Ese libro no está prestado.")
    else:
        libro[7] = ""
        libro[8] = ""
        print("Devolución registrada. Ya puede atender la siguiente solicitud.")
