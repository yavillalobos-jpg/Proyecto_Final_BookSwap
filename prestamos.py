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
    if libro.modalidad != "Préstamo":
        print("Este libro no está publicado para préstamo.")
        return
    nombre = leer_texto("Nombre del solicitante: ")
    universidad = leer_texto("Universidad del solicitante: ")
    if (nombre.lower() == libro.propietario.lower()
            and universidad.lower() == libro.universidad.lower()):
        print("El propietario no puede solicitar su propio libro.")
        return
    if (nombre.lower() == libro.prestado_a.lower()
            and universidad.lower() == libro.universidad_prestatario.lower()):
        print("Esa persona ya tiene prestado el libro.")
        return
    for solicitud in libro.cola:
        if (solicitud[0].lower() == nombre.lower()
                and solicitud[1].lower() == universidad.lower()):
            print("Esa persona ya está en la cola.")
            return
    libro.cola.append([nombre, universidad])
    print("Solicitud registrada. Posición en la cola:", len(libro.cola))


def ver_solicitudes(cabeza):
    actual = cabeza
    cantidad = 0
    while actual is not None:
        if len(actual.cola) > 0:
            print("Libro:", actual.titulo, "| Código:", actual.codigo)
            posicion = 1
            for solicitud in actual.cola:
                print(posicion, "-", solicitud[0], "|", solicitud[1])
                posicion += 1
                cantidad += 1
        actual = actual.siguiente
    if cantidad == 0:
        print("No hay solicitudes pendientes.")


def atender_prestamo(cabeza):
    codigo = leer_entero("Código del libro que se va a prestar: ")
    libro = buscar_codigo(cabeza, codigo)
    if libro is None:
        print("No existe ese libro.")
    elif libro.modalidad != "Préstamo":
        print("Este libro no está publicado para préstamo.")
    elif libro.prestado_a != "":
        print("Primero debe registrarse la devolución del libro.")
    elif len(libro.cola) == 0:
        print("No hay solicitudes para ese libro.")
    else:
        solicitud = libro.cola.pop(0)
        libro.prestado_a = solicitud[0]
        libro.universidad_prestatario = solicitud[1]
        print("Libro prestado a:", libro.prestado_a)


def devolver_libro(cabeza):
    codigo = leer_entero("Código del libro devuelto: ")
    libro = buscar_codigo(cabeza, codigo)
    if libro is None:
        print("No existe ese libro.")
    elif libro.prestado_a == "":
        print("Ese libro no está prestado.")
    else:
        libro.prestado_a = ""
        libro.universidad_prestatario = ""
        print("Devolución registrada. Ya puede atender la siguiente solicitud.")
