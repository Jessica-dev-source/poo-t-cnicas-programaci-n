from modelos.tarea import Tarea


class TareaServicio:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, texto):
        texto = texto.strip()
        if texto == "":
            return False
        nueva_tarea = Tarea(texto)
        self.tareas.append(nueva_tarea)
        return True

    def obtener_tareas(self):
        return self.tareas

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()
            return True
        return False

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            return True
        return False