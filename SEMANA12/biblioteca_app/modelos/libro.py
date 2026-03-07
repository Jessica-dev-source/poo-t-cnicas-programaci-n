class Libro:
    """
    Representa un libro dentro del sistema de biblioteca.
    Se utiliza una tupla para almacenar autor y título,
    ya que estos datos no deben cambiar una vez creado el objeto.
    """

    def __init__(self, autor: str, titulo: str, categoria: str, isbn: str):
        self._autor_titulo = (autor, titulo)  # Tupla inmutable
        self._categoria = categoria
        self._isbn = isbn

    @property
    def autor(self):
        return self._autor_titulo[0]

    @property
    def titulo(self):
        return self._autor_titulo[1]

    @property
    def categoria(self):
        return self._categoria

    @property
    def isbn(self):
        return self._isbn

    def __str__(self):
        return f"'{self.titulo}' - {self.autor} | Categoría: {self.categoria} | ISBN: {self.isbn}"