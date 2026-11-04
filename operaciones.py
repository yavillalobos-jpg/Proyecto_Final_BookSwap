# COMPRAS E INTERCAMBIOS: funciones que recorren y modifican la lista enlazada.
# El programa registra acuerdos; el pago y la entrega se hacen fuera de él.
from catalogo import buscar_codigo, mostrar_libro
from entradas import leer_texto, leer_entero


def disponible(libro):
    return (libro.estado == "Disponible" and libro.prestado_a == ""
            and len(libro.cola) == 0)


def mostrar_por_modalidad(cabeza, modalidad):
    actual = cabeza
    cantidad = 0
    while actual is not None:
        if actual.modalidad == modalidad and disponible(actual):
            mostrar_libro(actual)
            cantidad += 1
        actual = actual.siguiente
    if cantidad == 0:
        print("No hay libros disponibles para", modalidad.lower())
    return cantidad


def confirmar(mensaje):
    opcion = input(mensaje + " (s/n): ").strip().lower()
    while opcion not in ["s", "n"]:
        opcion = input("Escriba s o n: ").strip().lower()
    return opcion == "s"


def comprar_libro(cabeza):
    if mostrar_por_modalidad(cabeza, "Venta") == 0:
        return
    codigo = leer_entero("Código del libro que desea comprar: ")
    libro = buscar_codigo(cabeza, codigo)
    if libro is None:
        print("No existe ese libro.")
        return
    if libro.modalidad != "Venta" or not disponible(libro):
        print("Ese libro no está disponible para comprar.")
        return
    nombre = leer_texto("Nombre del comprador: ")
    universidad = leer_texto("Universidad del comprador: ")
    if (nombre.lower() == libro.propietario.lower()
            and universidad.lower() == libro.universidad.lower()):
        print("El propietario no puede comprar su propio libro.")
        return
    print("Libro:", libro.titulo, "| Precio: C$", libro.precio)
    if not confirmar("¿Confirma la compra acordada con el vendedor?"):
        print("Compra cancelada. El libro sigue disponible.")
        return
    libro.estado = "Vendido"
    libro.destinatario = nombre
    libro.universidad_destinatario = universidad
    print("Compra registrada. Libro vendido a:", nombre)
    print("El pago y la entrega se realizan fuera del programa.")


def intercambiar_libros(cabeza):
    if mostrar_por_modalidad(cabeza, "Intercambio") < 2:
        print("Se necesitan dos publicaciones disponibles para intercambio.")
        return
    codigo_deseado = leer_entero("Código del libro que desea recibir: ")
    codigo_ofrecido = leer_entero("Código del libro que ofrece a cambio: ")
    if codigo_deseado == codigo_ofrecido:
        print("Debe seleccionar dos libros distintos.")
        return
    deseado = buscar_codigo(cabeza, codigo_deseado)
    ofrecido = buscar_codigo(cabeza, codigo_ofrecido)
    if deseado is None or ofrecido is None:
        print("Uno de los códigos no existe.")
        return
    if (deseado.modalidad != "Intercambio" or ofrecido.modalidad != "Intercambio"
            or not disponible(deseado) or not disponible(ofrecido)):
        print("Ambos libros deben estar disponibles para intercambio.")
        return
    if (deseado.propietario.lower() == ofrecido.propietario.lower()
            and deseado.universidad.lower() == ofrecido.universidad.lower()):
        print("Los libros deben pertenecer a personas distintas.")
        return
    print(deseado.propietario, "recibirá:", ofrecido.titulo)
    print(ofrecido.propietario, "recibirá:", deseado.titulo)
    if not confirmar("¿Ambos propietarios aceptaron el intercambio?"):
        print("Intercambio cancelado. Los libros siguen disponibles.")
        return
    # Conservamos quién publicó cada libro y registramos quién lo recibe.
    deseado.estado = "Intercambiado"
    deseado.destinatario = ofrecido.propietario
    deseado.universidad_destinatario = ofrecido.universidad
    deseado.codigo_intercambio = ofrecido.codigo
    ofrecido.estado = "Intercambiado"
    ofrecido.destinatario = deseado.propietario
    ofrecido.universidad_destinatario = deseado.universidad
    ofrecido.codigo_intercambio = deseado.codigo
    print("Intercambio registrado. Ambas publicaciones quedan cerradas.")
