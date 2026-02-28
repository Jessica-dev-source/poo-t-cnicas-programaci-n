import json
from pathlib import Path
from inventario import Inventario

ARCHIVO = "inventario.json"


def guardar(inv: Inventario, ruta: str = ARCHIVO) -> None:
    with Path(ruta).open("w", encoding="utf-8") as f:
        json.dump(inv.to_dict(), f, ensure_ascii=False, indent=2)


def cargar(ruta: str = ARCHIVO) -> Inventario:
    p = Path(ruta)
    if not p.exists():
        return Inventario()
    with p.open("r", encoding="utf-8") as f:
        data = json.load(f)
        return Inventario.from_dict(data)