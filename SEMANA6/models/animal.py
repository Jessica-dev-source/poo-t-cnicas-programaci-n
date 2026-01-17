# ===== models/animal.py (todo en un solo archivo) =====
class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def hacer_sonido(self):
        print(f"Un {self.nombre} hace {self.sonido}")

    def __str__(self):
        return f"Animal: {self.nombre}, Sonido: {self.sonido}"


# ===== models/perro.py (todo en un solo archivo) =====
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre, "Guau")
        self.raza = raza
        self._edad = None

    def hacer_sonido(self):
        print(f"El perro {self.nombre} de raza {self.raza} dice: {self.sonido}!")

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            print("La edad debe ser un entero no negativo.")

    def __str__(self):
        return f"Perro: {self.nombre}, Raza: {self.raza}, Sonido: {self.sonido}, Edad: {self._edad}"


# ===== services/animal_service.py (todo en un solo archivo) =====
class AnimalService:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def listar_animales(self):
        if not self.animales:
            print("No hay animales registrados.")
        else:
            for animal in self.animales:
                print(animal)

    def hacer_sonidos(self):
        if not self.animales:
            print("No hay animales para hacer sonidos.")
        else:
            for animal in self.animales:
                animal.hacer_sonido()


# ===== main.py (todo en un solo archivo) =====
def main():
    animal1 = Animal("Gato", "Miau")
    perro1 = Perro("Buddy", "Golden Retriever")
    perro1.set_edad(3)

    print(animal1)
    print(perro1)

    animal1.hacer_sonido()
    perro1.hacer_sonido()

    animal_service = AnimalService()
    animal_service.agregar_animal(animal1)
    animal_service.agregar_animal(perro1)

    print("\nListado de animales:")
    animal_service.listar_animales()

    print("\nAnimales haciendo sonidos:")
    animal_service.hacer_sonidos()

if __name__ == "__main__":
    main()