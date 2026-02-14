# ==========================================
# SISTEMA DE GESTIÓN DE INVENTARIOS
# ==========================================

# ------------------------------------------
# Clase Producto
# ------------------------------------------

class Producto:
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"


# ------------------------------------------
# Clase Inventario
# ------------------------------------------

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("✅ Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("✅ Producto eliminado.")
                return
        print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("✅ Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                encontrados.append(p)

        if encontrados:
            print("🔎 Productos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("📋 Inventario actual:")
            for p in self.productos:
                print(p)


# ------------------------------------------
# Funciones auxiliares
# ------------------------------------------

def leer_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Debes ingresar un número entero.")

def leer_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Debes ingresar un número válido.")


# ------------------------------------------
# Menú Principal
# ------------------------------------------

def main():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = leer_int("Seleccione una opción: ")

        if opcion == 1:
            id_producto = leer_int("ID: ")
            nombre = input("Nombre: ")
            cantidad = leer_int("Cantidad: ")
            precio = leer_float("Precio: ")

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == 2:
            id_producto = leer_int("Ingrese el ID a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == 3:
            id_producto = leer_int("Ingrese el ID a actualizar: ")
            cantidad = leer_int("Nueva cantidad: ")
            precio = leer_float("Nuevo precio: ")
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == 4:
            nombre = input("Ingrese el nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == 5:
            inventario.mostrar_inventario()

        elif opcion == 6:
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    main()
