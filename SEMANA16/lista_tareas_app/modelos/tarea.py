class Tarea:
    def __init__(self, texto):
        self.texto = texto
        self.completada = False

    def marcar_completada(self):
        self.completada = True