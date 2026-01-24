# Programa: Sistema de Gestión de Vehículos
# Demostración de Constructores y Destructores en Python (POO)

class Vehiculo:
    """
    Clase base Vehiculo
    """
    def __init__(self, marca):
        self.marca = marca
        print(f"Vehículo de marca '{self.marca}' creado.")

    def mostrar_info(self):
        print(f"Vehículo marca: {self.marca}")

    def __del__(self):
        print(f"Vehículo de marca '{self.marca}' eliminado.")


class Auto(Vehiculo):
    """
    Clase Auto que hereda de Vehiculo
    """
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.__modelo = modelo  # Encapsulación
        print(f"Auto modelo '{self.__modelo}' inicializado.")

    def mostrar_info(self):
        # Polimorfismo (método sobrescrito)
        print(f"Auto: {self.marca} - Modelo: {self.__modelo}")

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo


def main():
    print("=== Sistema de Gestión de Vehículos ===\n")

    auto1 = Auto("Toyota", "Corolla")
    auto2 = Auto("Chevrolet", "Spark")

    print("\nInformación de los vehículos:")
    auto1.mostrar_info()
    auto2.mostrar_info()

    print("\nModificando modelo del segundo auto...")
    auto2.set_modelo("Onix")
    auto2.mostrar_info()

    print("\nFin del programa.")


if __name__ == "__main__":
    main()