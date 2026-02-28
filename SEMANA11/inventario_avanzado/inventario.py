from typing import Dict, List, Optional, Tuple, Set
from producto import Producto


class Inventario:
    def __init__(self) -> None:
        self.productos: Dict[str, Producto] = {}     # dict principal: id -> Producto
        self._index_nombres: Set[str] = set()         # set para indexar nombres normalizados

    @staticmethod
    def _norm(txt: str) -> str:
        return txt.strip().lower()

    def _reconstruir_index(self) -> None:
        self._index_nombres = {self._norm(p.nombre) for p in self.productos.values()}

    def agregar_producto(self, producto: Producto) -> None:
        pid = producto.get_id().strip()
        if pid in self.productos:
            raise ValueError(f"Ya existe un producto con ID '{pid}'.")
        self.productos[pid] = producto
        self._index_nombres.add(self._norm(producto.get_nombre()))

    def eliminar_producto(self, producto_id: str) -> None:
        pid = producto_id.strip()
        if pid not in self.productos:
            raise KeyError(f"No existe producto con ID '{pid}'.")
        self.productos.pop(pid)
        self._reconstruir_index()

    def actualizar_producto(self, producto_id: str,
                            nueva_cantidad: Optional[int] = None,
                            nuevo_precio: Optional[float] = None) -> None:
        pid = producto_id.strip()
        if pid not in self.productos:
            raise KeyError(f"No existe producto con ID '{pid}'.")
        p = self.productos[pid]

        if nueva_cantidad is not None:
            p.set_cantidad(nueva_cantidad)
        if nuevo_precio is not None:
            p.set_precio(nuevo_precio)

    def buscar_por_nombre(self, texto: str) -> List[Producto]:
        consulta = self._norm(texto)
        if not consulta:
            return []
        resultados = [p for p in self.productos.values()
                      if consulta in self._norm(p.get_nombre())]
        resultados.sort(key=lambda p: self._norm(p.get_nombre()))
        return resultados

    def listar_todos(self) -> List[Producto]:
        lista = list(self.productos.values())  # list
        lista.sort(key=lambda p: (self._norm(p.get_nombre()), p.get_id()))
        return lista

    def obtener_producto(self, producto_id: str) -> Optional[Producto]:
        return self.productos.get(producto_id.strip())

    def resumen(self) -> Tuple[int, int, float]:
        # tuple (inmutable)
        distintos = len(self.productos)
        unidades = sum(p.get_cantidad() for p in self.productos.values())
        total = sum(p.get_cantidad() * p.get_precio() for p in self.productos.values())
        return (distintos, unidades, round(total, 2))

    def to_dict(self) -> dict:
        return {"productos": [p.to_dict() for p in self.productos.values()]}

    @staticmethod
    def from_dict(data: dict) -> "Inventario":
        inv = Inventario()
        for item in data.get("productos", []):
            prod = Producto.from_dict(item)
            inv.productos[prod.get_id()] = prod
        inv._reconstruir_index()
        return inv