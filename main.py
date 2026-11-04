# BOOKSWAP: ejecutar este archivo con python main.py.
# MÓDULOS: importamos funciones de los otros archivos del proyecto.
from catalogo import publicar_libro, mostrar_catalogo, buscar_libros, eliminar_publicacion
from prestamos import solicitar_prestamo, ver_solicitudes, atender_prestamo, devolver_libro
from archivos import guardar_datos, cargar_datos

def main():
    try:
        cabeza = cargar_datos()
    except (OSError, ValueError, IndexError):
        print("No se pudieron leer los archivos. Revise su contenido y permisos.")
        return
    while True:
        print("\n========== BOOKSWAP ==========")
        print("1. Publicar un libro")
        print("2. Mostrar catálogo")
        print("3. Buscar libros")
        print("4. Solicitar préstamo")
        print("5. Ver solicitudes pendientes")
        print("6. Atender siguiente solicitud de préstamo")
        print("7. Registrar devolución")
        print("8. Eliminar publicación")
        print("9. Guardar y salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            cabeza = publicar_libro(cabeza)
        elif opcion == "2":
            mostrar_catalogo(cabeza)
        elif opcion == "3":
            buscar_libros(cabeza)
        elif opcion == "4":
            solicitar_prestamo(cabeza)
        elif opcion == "5":
            ver_solicitudes(cabeza)
        elif opcion == "6":
            atender_prestamo(cabeza)
        elif opcion == "7":
            devolver_libro(cabeza)
        elif opcion == "8":
            cabeza = eliminar_publicacion(cabeza)
        elif opcion != "9":
            print("Opción incorrecta.")
            continue
        # Guardamos después de cada cambio y antes de salir.
        if opcion in ["1", "4", "6", "7", "8", "9"]:
            try:
                guardar_datos(cabeza)
            except OSError:
                print("No se pudo guardar. Revise los permisos e intente la opción 9.")
                continue
        if opcion == "9":
            print("Datos guardados. Hasta pronto.")
            break


if __name__ == "__main__":
    main()

