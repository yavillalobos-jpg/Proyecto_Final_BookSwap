# BOOKSWAP: ejecutar este archivo con python main.py.
# MÓDULOS: importamos funciones de los otros archivos del proyecto.
from catalogo import publicar_libro, mostrar_catalogo, buscar_libros, eliminar_publicacion
from prestamos import solicitar_prestamo, ver_solicitudes, atender_prestamo, devolver_libro
from archivos import guardar_datos, cargar_datos
from operaciones import comprar_libro, intercambiar_libros

def main():
    try:
        cabeza = cargar_datos()
    except (OSError, ValueError, IndexError):
        print("No se pudieron leer los archivos. Revise su contenido y permisos.")
        return
    while True:
        print("\n========== BOOKSWAP ==========")
        print("1. Vender: publicar un libro en venta")
        print("2. Publicar un libro para intercambio")
        print("3. Publicar un libro para préstamo")
        print("4. Mostrar catálogo")
        print("5. Buscar libros")
        print("6. Comprar un libro")
        print("7. Intercambiar libros")
        print("8. Solicitar préstamo")
        print("9. Ver solicitudes de préstamo pendientes")
        print("10. Atender siguiente solicitud de préstamo")
        print("11. Registrar devolución")
        print("12. Eliminar publicación")
        print("13. Guardar y salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            cabeza = publicar_libro(cabeza, "Venta")
        elif opcion == "2":
            cabeza = publicar_libro(cabeza, "Intercambio")
        elif opcion == "3":
            cabeza = publicar_libro(cabeza, "Préstamo")
        elif opcion == "4":
            mostrar_catalogo(cabeza)
        elif opcion == "5":
            buscar_libros(cabeza)
        elif opcion == "6":
            comprar_libro(cabeza)
        elif opcion == "7":
            intercambiar_libros(cabeza)
        elif opcion == "8":
            solicitar_prestamo(cabeza)
        elif opcion == "9":
            ver_solicitudes(cabeza)
        elif opcion == "10":
            atender_prestamo(cabeza)
        elif opcion == "11":
            devolver_libro(cabeza)
        elif opcion == "12":
            cabeza = eliminar_publicacion(cabeza)
        elif opcion != "13":
            print("Opción incorrecta.")
            continue
        # Guardamos después de cada cambio y antes de salir.
        if opcion in ["1", "2", "3", "6", "7", "8", "10", "11", "12", "13"]:
            try:
                guardar_datos(cabeza)
            except OSError:
                print("No se pudo guardar. Revise los permisos e intente la opción 13.")
                continue
        if opcion == "13":
            print("Datos guardados. Hasta pronto.")
            break


if __name__ == "__main__":
    main()
