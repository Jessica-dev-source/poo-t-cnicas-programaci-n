from producto import Producto
from storage import cargar, guardar, ARCHIVO


def leer_texto(msg: str) -> str:
    while True:
        t = input(msg).strip()
        if t:
            return t
        print("Error: no puede estar vacío.")


def leer_int(msg: str, minimo: int = 0) -> int:
    while True:
        try:
            v = int(input(msg).strip())
            if v < minimo:
                print(f"Error: debe ser >= {minimo}.")
                continue
            return v
        except ValueError:
            print("Error: ingrese un entero válido.")


def leer_float(msg: str, minimo: float = 0.0) -> float:
    while True:
        try:
            v = float(input(msg).strip())
            if v < minimo:
                print(f"Error: debe ser >= {minimo}.")
                continue
            return v
        except ValueError:
            print("Error: ingrese un número válido.")


def mostrar(p: Producto) -> None:
    print(f"ID: {p.id} | Nombre: {p.nombre} | Cantidad: {p.cantidad} | Precio: ${p.precio:.2f}")


def menu() -> None:
    print("\n=== SISTEMA AVANZADO DE INVENTARIO ===")
    print("1) Añadir producto")
    print("2) Eliminar por ID")
    print("3) Actualizar cantidad/precio")
    print("4) Buscar por nombre")
    print("5) Mostrar todos")
    print("6) Resumen")
    print("7) Guardar")
    print("0) Salir")


def main():
    inv = cargar(ARCHIVO)
    print(f"Inventario cargado desde '{ARCHIVO}'.")

    while True:
        menu()
        op = input("Seleccione una opción: ").strip()

        try:
            if op == "1":
                pid = leer_texto("ID único: ")
                nombre = leer_texto("Nombre: ")
                cantidad = leer_int("Cantidad (>=0): ", 0)
                precio = leer_float("Precio (>=0): ", 0.0)
                inv.agregar_producto(Producto(pid, nombre, cantidad, precio))
                print("Producto agregado.")

            elif op == "2":
                pid = leer_texto("ID a eliminar: ")
                inv.eliminar_producto(pid)
                print("Producto eliminado.")

            elif op == "3":
                pid = leer_texto("ID a actualizar: ")
                p = inv.obtener_producto(pid)
                if not p:
                    print("No existe ese ID.")
                    continue
                print("Producto actual:")
                mostrar(p)

                print("1) Cantidad  2) Precio  3) Ambos")
                sub = input("Opción: ").strip()

                if sub == "1":
                    c = leer_int("Nueva cantidad: ", 0)
                    inv.actualizar_producto(pid, nueva_cantidad=c)
                elif sub == "2":
                    pr = leer_float("Nuevo precio: ", 0.0)
                    inv.actualizar_producto(pid, nuevo_precio=pr)
                elif sub == "3":
                    c = leer_int("Nueva cantidad: ", 0)
                    pr = leer_float("Nuevo precio: ", 0.0)
                    inv.actualizar_producto(pid, nueva_cantidad=c, nuevo_precio=pr)
                else:
                    print("Opción inválida.")
                    continue

                print("Producto actualizado.")

            elif op == "4":
                txt = leer_texto("Nombre (o parte): ")
                res = inv.buscar_por_nombre(txt)
                if not res:
                    print("No se encontraron productos.")
                else:
                    for p in res:
                        mostrar(p)

            elif op == "5":
                lista = inv.listar_todos()
                if not lista:
                    print("Inventario vacío.")
                else:
                    for p in lista:
                        mostrar(p)

            elif op == "6":
                distintos, unidades, total = inv.resumen()
                print("\n--- RESUMEN ---")
                print(f"Productos distintos: {distintos}")
                print(f"Unidades totales: {unidades}")
                print(f"Valor total: ${total:.2f}")

            elif op == "7":
                guardar(inv, ARCHIVO)
                print(f"Inventario guardado en '{ARCHIVO}'.")

            elif op == "0":
                guardar(inv, ARCHIVO)  # guardado automático
                print("Guardado final realizado. Saliendo...")
                break

            else:
                print("Opción inválida.")

        except (ValueError, KeyError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()