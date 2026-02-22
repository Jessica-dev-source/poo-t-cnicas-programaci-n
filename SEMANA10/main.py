# ==========================================================
# SISTEMA DE GESTIÓN DE INVENTARIOS MEJORADO - SEMANA 10
# - Persistencia en inventario.txt
# - Carga automática al iniciar
# - Manejo robusto de excepciones (FileNotFoundError, PermissionError, etc.)
# - Notificaciones claras al usuario en consola
# ==========================================================

import os


# -------------------------------
# Clase Producto
# -------------------------------
class Producto:
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self) -> str:
        return self.__id

    def get_nombre(self) -> str:
        return self.__nombre

    def get_cantidad(self) -> int:
        return self.__cantidad

    def get_precio(self) -> float:
        return self.__precio

    # Setters
    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def set_cantidad(self, cantidad: int):
        self.__cantidad = cantidad

    def set_precio(self, precio: float):
        self.__precio = precio

    # ---- Archivo ----
    def to_linea(self) -> str:
        """Convierte el producto a una línea de texto: id|nombre|cantidad|precio"""
        return f"{self.__id}|{self.__nombre}|{self.__cantidad}|{self.__precio}"

    @staticmethod
    def desde_linea(linea: str):
        """
        Reconstruye un Producto desde una línea del archivo.
        Lanza ValueError si la línea está corrupta.
        """
        partes = linea.strip().split("|")
        if len(partes) != 4:
            raise ValueError("Formato inválido (se esperaban 4 campos).")

        id_producto = partes[0].strip()
        nombre = partes[1].strip()
        cantidad = int(partes[2].strip())
        precio = float(partes[3].strip())

        if id_producto == "" or nombre == "":
            raise ValueError("ID o nombre vacío.")
        if cantidad < 0 or precio < 0:
            raise ValueError("Cantidad o precio negativos.")

        return Producto(id_producto, nombre, cantidad, precio)

    def __str__(self) -> str:
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"


# -------------------------------
# Clase Inventario
# -------------------------------
class Inventario:
    def __init__(self, ruta_archivo: str = "inventario.txt"):
        self.__productos = []
        self.__ruta = ruta_archivo

        # Carga automática al iniciar (requisito)
        ok, msg = self.cargar_desde_archivo()
        print(("✅" if ok else "❌"), msg)

    # ---- Utilidades ----
    def id_existe(self, id_producto: str) -> bool:
        for p in self.__productos:
            if p.get_id() == id_producto:
                return True
        return False

    def obtener_por_id(self, id_producto: str):
        for p in self.__productos:
            if p.get_id() == id_producto:
                return p
        return None

    def mostrar_todos(self):
        return self.__productos

    def buscar_por_nombre(self, texto: str):
        texto = texto.strip().lower()
        return [p for p in self.__productos if texto in p.get_nombre().lower()]

    # -------------------------------
    # Persistencia en archivo
    # -------------------------------
    def asegurar_archivo(self):
        """
        Asegura que el archivo exista. Si no existe, lo crea.
        Maneja PermissionError y OSError.
        """
        try:
            if not os.path.exists(self.__ruta):
                with open(self.__ruta, "w", encoding="utf-8") as f:
                    f.write("")
            return True, "Archivo listo."
        except PermissionError:
            return False, "PermissionError: No hay permisos para crear/escribir el archivo."
        except OSError as e:
            return False, f"OSError: Error del sistema al asegurar el archivo. {e}"

    def cargar_desde_archivo(self):
        """
        Carga el inventario desde inventario.txt.
        - Si no existe, lo crea.
        - Si hay líneas corruptas, las ignora (sin romper el programa).
        """
        ok, msg = self.asegurar_archivo()
        if not ok:
            return False, msg

        try:
            self.__productos = []
            corruptas = 0

            with open(self.__ruta, "r", encoding="utf-8") as f:
                for linea in f:
                    if linea.strip() == "":
                        continue
                    try:
                        prod = Producto.desde_linea(linea)
                        if not self.id_existe(prod.get_id()):
                            self.__productos.append(prod)
                    except ValueError:
                        corruptas += 1

            if corruptas > 0:
                return True, f"Inventario cargado con advertencia: {corruptas} línea(s) corrupta(s) ignoradas."
            return True, "Inventario cargado correctamente desde archivo."

        except FileNotFoundError:
            return False, "FileNotFoundError: No se encontró el archivo del inventario."
        except PermissionError:
            return False, "PermissionError: No hay permisos para leer el archivo."
        except OSError as e:
            return False, f"OSError: Error del sistema al leer el archivo. {e}"

    def guardar_en_archivo(self):
        """
        Guarda TODO el inventario en inventario.txt.
        Estrategia segura: escribir en archivo temporal y reemplazar.
        """
        ok, msg = self.asegurar_archivo()
        if not ok:
            return False, msg

        temp = self.__ruta + ".tmp"

        try:
            with open(temp, "w", encoding="utf-8") as f:
                for p in self.__productos:
                    f.write(p.to_linea() + "\n")

            os.replace(temp, self.__ruta)
            return True, "Archivo actualizado correctamente."

        except PermissionError:
            return False, "PermissionError: No hay permisos para escribir en el archivo."
        except OSError as e:
            return False, f"OSError: Error del sistema al escribir el archivo. {e}"
        finally:
            # Limpieza por si quedó el temp
            try:
                if os.path.exists(temp):
                    os.remove(temp)
            except Exception:
                pass

    # -------------------------------
    # Operaciones CRUD (con guardado)
    # -------------------------------
    def anadir_producto(self, producto: Producto):
        if self.id_existe(producto.get_id()):
            return False, "Ese ID ya existe. No se agregó el producto."

        self.__productos.append(producto)

        ok_arch, msg_arch = self.guardar_en_archivo()
        if ok_arch:
            return True, "Producto agregado y guardado en inventario.txt correctamente."
        return False, f"Producto agregado en memoria, pero falló el guardado en archivo. Detalle: {msg_arch}"

    def eliminar_por_id(self, id_producto: str):
        for i, p in enumerate(self.__productos):
            if p.get_id() == id_producto:
                self.__productos.pop(i)

                ok_arch, msg_arch = self.guardar_en_archivo()
                if ok_arch:
                    return True, "Producto eliminado y archivo actualizado correctamente."
                return False, f"Producto eliminado en memoria, pero falló la actualización del archivo. Detalle: {msg_arch}"

        return False, "No se encontró un producto con ese ID."

    def actualizar_por_id(self, id_producto: str, nueva_cantidad: int, nuevo_precio: float):
        """
        Actualiza ambos: cantidad y precio (requisito que pediste).
        """
        p = self.obtener_por_id(id_producto)
        if p is None:
            return False, "No se encontró un producto con ese ID."

        p.set_cantidad(nueva_cantidad)
        p.set_precio(nuevo_precio)

        ok_arch, msg_arch = self.guardar_en_archivo()
        if ok_arch:
            return True, "Producto actualizado (cantidad y precio) y guardado en inventario.txt."
        return False, f"Producto actualizado en memoria, pero falló el guardado en archivo. Detalle: {msg_arch}"


# -------------------------------
# Entrada segura
# -------------------------------
def leer_texto(mensaje: str) -> str:
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("❌ No puede estar vacío.")
            continue
        return texto


def leer_entero(mensaje: str) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("❌ No se permiten negativos.")
                continue
            return valor
        except ValueError:
            print("❌ Ingresa un entero válido.")


def leer_flotante(mensaje: str) -> float:
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("❌ No se permiten negativos.")
                continue
            return valor
        except ValueError:
            print("❌ Ingresa un número válido (ej. 10.50).")


# -------------------------------
# Menú principal
# -------------------------------
def main():
    inventario = Inventario("inventario.txt")

    while True:
        print("\n" + "=" * 55)
        print("📦 SISTEMA DE GESTIÓN DE INVENTARIOS (MEJORADO)")
        print("=" * 55)
        print("1. Añadir producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad y precio por ID")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar inventario")
        print("0. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            print("\n➕ AÑADIR PRODUCTO")
            id_prod = leer_texto("ID (puede ser número o texto): ")
            nombre = leer_texto("Nombre: ")
            cantidad = leer_entero("Cantidad: ")
            precio = leer_flotante("Precio: ")

            ok, msg = inventario.anadir_producto(Producto(id_prod, nombre, cantidad, precio))
            print(("✅" if ok else "❌"), msg)

        elif opcion == "2":
            print("\n🗑 ELIMINAR PRODUCTO")
            id_prod = leer_texto("ID a eliminar: ")
            ok, msg = inventario.eliminar_por_id(id_prod)
            print(("✅" if ok else "❌"), msg)

        elif opcion == "3":
            print("\n✏ ACTUALIZAR PRODUCTO (CANTIDAD Y PRECIO)")
            id_prod = leer_texto("ID a actualizar: ")
            nueva_cantidad = leer_entero("Nueva cantidad: ")
            nuevo_precio = leer_flotante("Nuevo precio: ")
            ok, msg = inventario.actualizar_por_id(id_prod, nueva_cantidad, nuevo_precio)
            print(("✅" if ok else "❌"), msg)

        elif opcion == "4":
            print("\n🔎 BUSCAR POR NOMBRE")
            texto = leer_texto("Nombre o parte del nombre: ")
            resultados = inventario.buscar_por_nombre(texto)
            if not resultados:
                print("❌ No se encontraron productos con ese criterio.")
            else:
                print(f"✅ Coincidencias: {len(resultados)}")
                for p in resultados:
                    print(" -", p)

        elif opcion == "5":
            print("\n📋 INVENTARIO")
            productos = inventario.mostrar_todos()
            if not productos:
                print("📭 Inventario vacío.")
            else:
                for p in productos:
                    print(" -", p)

        elif opcion == "0":
            print("\n👋 Saliendo del sistema. Inventario guardado.")
            break

        else:
            print("❌ Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()