from dataclasses import dataclass


@dataclass
class Producto:
    id: str
    nombre: str
    cantidad: int
    precio: float

    def get_id(self) -> str:
        return self.id

    def set_id(self, nuevo_id: str) -> None:
        if not nuevo_id or not nuevo_id.strip():
            raise ValueError("El ID no puede estar vacío.")
        self.id = nuevo_id.strip()

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nuevo_nombre: str) -> None:
        if not nuevo_nombre or not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.nombre = nuevo_nombre.strip()

    def get_cantidad(self) -> int:
        return self.cantidad

    def set_cantidad(self, nueva_cantidad: int) -> None:
        if int(nueva_cantidad) < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.cantidad = int(nueva_cantidad)

    def get_precio(self) -> float:
        return self.precio

    def set_precio(self, nuevo_precio: float) -> None:
        if float(nuevo_precio) < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = float(nuevo_precio)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data: dict) -> "Producto":
        return Producto(
            id=str(data["id"]),
            nombre=str(data["nombre"]),
            cantidad=int(data["cantidad"]),
            precio=float(data["precio"])
        )