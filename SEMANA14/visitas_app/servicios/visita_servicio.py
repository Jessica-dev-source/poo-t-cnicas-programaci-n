from modelos.visitante import Visitante


class VisitaServicio:
    """
    Clase encargada de gestionar la lógica CRUD de los visitantes.
    """

    def __init__(self):
        self._visitantes = []

    def registrar_visitante(self, cedula, nombre_completo, motivo_visita):
        """
        Registra un nuevo visitante si la cédula no está repetida.
        """
        if self.buscar_por_cedula(cedula) is not None:
            return False

        nuevo_visitante = Visitante(cedula, nombre_completo, motivo_visita)
        self._visitantes.append(nuevo_visitante)
        return True

    def obtener_visitantes(self):
        """
        Devuelve la lista actual de visitantes.
        """
        return self._visitantes

    def eliminar_visitante(self, cedula):
        """
        Elimina un visitante según su cédula.
        """
        visitante = self.buscar_por_cedula(cedula)

        if visitante is not None:
            self._visitantes.remove(visitante)
            return True

        return False

    def buscar_por_cedula(self, cedula):
        """
        Busca un visitante por su cédula.
        """
        for visitante in self._visitantes:
            if visitante.cedula == cedula:
                return visitante
        return None