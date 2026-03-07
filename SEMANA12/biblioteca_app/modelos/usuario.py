class Usuario:
    """
    Representa un usuario registrado en la biblioteca.
    Se utiliza una lista para almacenar los libros prestados,
    porque esta colección cambia dinámicamente.
    """

    def __init__(self, nombre: str, user_id: str):
        self._nombre = nombre
        self._user_id = user_id
        self._libros_prestados = []  # Lista dinámica

    @property
    def nombre(self):
        return self._nombre

    @property
    def user_id(self):
        return self._user_id

    @property
    def libros_prestados(self):
        return self._libros_prestados

    def prestar_libro(self, libro):
        self._libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self._libros_prestados:
            if libro.isbn == isbn:
                self._libros_prestados.remove(libro)
                return libro
        return None

    def __str__(self):
        return f"{self.nombre} (ID: {self.user_id})"