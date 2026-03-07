from servicios.biblioteca_servicio import BibliotecaServicio


def mostrar_menu():
    print("\n===== SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL =====")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro por título")
    print("8. Buscar libro por autor")
    print("9. Buscar libro por categoría")
    print("10. Listar libros prestados de un usuario")
    print("11. Listar libros disponibles")
    print("12. Listar usuarios registrados")
    print("0. Salir")


def main():
    biblioteca = BibliotecaServicio()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            autor = input("Autor: ")
            titulo = input("Título: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            exito, mensaje = biblioteca.agregar_libro(autor, titulo, categoria, isbn)
            print(mensaje)

        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            exito, mensaje = biblioteca.quitar_libro(isbn)
            print(mensaje)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            user_id = input("ID del usuario: ")
            exito, mensaje = biblioteca.registrar_usuario(nombre, user_id)
            print(mensaje)

        elif opcion == "4":
            user_id = input("ID del usuario a dar de baja: ")
            exito, mensaje = biblioteca.dar_baja_usuario(user_id)
            print(mensaje)

        elif opcion == "5":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            exito, mensaje = biblioteca.prestar_libro(user_id, isbn)
            print(mensaje)

        elif opcion == "6":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            exito, mensaje = biblioteca.devolver_libro(user_id, isbn)
            print(mensaje)

        elif opcion == "7":
            titulo = input("Ingrese el título a buscar: ")
            resultados = biblioteca.buscar_por_titulo(titulo)
            if resultados:
                print("\nResultados encontrados:")
                for libro in resultados:
                    print("-", libro)
            else:
                print("No se encontraron libros con ese título.")

        elif opcion == "8":
            autor = input("Ingrese el autor a buscar: ")
            resultados = biblioteca.buscar_por_autor(autor)
            if resultados:
                print("\nResultados encontrados:")
                for libro in resultados:
                    print("-", libro)
            else:
                print("No se encontraron libros de ese autor.")

        elif opcion == "9":
            categoria = input("Ingrese la categoría a buscar: ")
            resultados = biblioteca.buscar_por_categoria(categoria)
            if resultados:
                print("\nResultados encontrados:")
                for libro in resultados:
                    print("-", libro)
            else:
                print("No se encontraron libros en esa categoría.")

        elif opcion == "10":
            user_id = input("Ingrese el ID del usuario: ")
            libros = biblioteca.listar_libros_prestados_usuario(user_id)

            if libros is None:
                print("El usuario no existe.")
            elif not libros:
                print("El usuario no tiene libros prestados.")
            else:
                print("\nLibros prestados:")
                for libro in libros:
                    print("-", libro)

        elif opcion == "11":
            libros = biblioteca.listar_libros_disponibles()
            if not libros:
                print("No hay libros disponibles.")
            else:
                print("\nLibros disponibles:")
                for libro in libros:
                    print("-", libro)

        elif opcion == "12":
            usuarios = biblioteca.listar_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                print("\nUsuarios registrados:")
                for usuario in usuarios:
                    print("-", usuario)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()