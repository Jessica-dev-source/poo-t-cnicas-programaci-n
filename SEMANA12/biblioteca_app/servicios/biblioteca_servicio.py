from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    """
    Gestiona la lógica del negocio del sistema de biblioteca digital.
    Aquí se administran los libros, los usuarios y los préstamos.
    """

    def __init__(self):
        # Diccionario para libros disponibles: ISBN -> Libro
        self._libros_disponibles = {}

        # Diccionario para usuarios registrados: user_id -> Usuario
        self._usuarios = {}

        # Conjunto para garantizar IDs únicos
        self._ids_usuarios = set()

    # =========================
    # Gestión de libros
    # =========================

    def agregar_libro(self, autor, titulo, categoria, isbn):
        if isbn in self._libros_disponibles:
            return False, "Ya existe un libro con ese ISBN."

        libro = Libro(autor, titulo, categoria, isbn)
        self._libros_disponibles[isbn] = libro
        return True, "Libro agregado correctamente."

    def quitar_libro(self, isbn):
        if isbn not in self._libros_disponibles:
            return False, "No existe un libro disponible con ese ISBN."

        del self._libros_disponibles[isbn]
        return True, "Libro quitado correctamente."

    def listar_libros_disponibles(self):
        return list(self._libros_disponibles.values())

    # =========================
    # Gestión de usuarios
    # =========================

    def registrar_usuario(self, nombre, user_id):
        if user_id in self._ids_usuarios:
            return False, "El ID de usuario ya está registrado."

        usuario = Usuario(nombre, user_id)
        self._usuarios[user_id] = usuario
        self._ids_usuarios.add(user_id)
        return True, "Usuario registrado correctamente."

    def dar_baja_usuario(self, user_id):
        if user_id not in self._usuarios:
            return False, "El usuario no existe."

        usuario = self._usuarios[user_id]

        if usuario.libros_prestados:
            return False, "No se puede dar de baja a un usuario con libros prestados."

        del self._usuarios[user_id]
        self._ids_usuarios.remove(user_id)
        return True, "Usuario dado de baja correctamente."

    def listar_usuarios(self):
        return list(self._usuarios.values())

    # =========================
    # Préstamos y devoluciones
    # =========================

    def prestar_libro(self, user_id, isbn):
        if user_id not in self._usuarios:
            return False, "El usuario no existe."

        if isbn not in self._libros_disponibles:
            return False, "El libro no está disponible."

        usuario = self._usuarios[user_id]
        libro = self._libros_disponibles[isbn]

        usuario.prestar_libro(libro)
        del self._libros_disponibles[isbn]

        return True, "Libro prestado correctamente."

    def devolver_libro(self, user_id, isbn):
        if user_id not in self._usuarios:
            return False, "El usuario no existe."

        usuario = self._usuarios[user_id]
        libro = usuario.devolver_libro(isbn)

        if libro is None:
            return False, "El usuario no tiene prestado ese libro."

        self._libros_disponibles[isbn] = libro
        return True, "Libro devuelto correctamente."

    def listar_libros_prestados_usuario(self, user_id):
        if user_id not in self._usuarios:
            return None

        return self._usuarios[user_id].libros_prestados

    # =========================
    # Búsquedas
    # =========================

    def buscar_por_titulo(self, titulo):
        resultados = []

        # Buscar en libros disponibles
        for libro in self._libros_disponibles.values():
            if titulo.lower() in libro.titulo.lower():
                resultados.append(libro)

        # Buscar en libros prestados
        for usuario in self._usuarios.values():
            for libro in usuario.libros_prestados:
                if titulo.lower() in libro.titulo.lower():
                    resultados.append(libro)

        return resultados

    def buscar_por_autor(self, autor):
        resultados = []

        for libro in self._libros_disponibles.values():
            if autor.lower() in libro.autor.lower():
                resultados.append(libro)

        for usuario in self._usuarios.values():
            for libro in usuario.libros_prestados:
                if autor.lower() in libro.autor.lower():
                    resultados.append(libro)

        return resultados

    def buscar_por_categoria(self, categoria):
        resultados = []

        for libro in self._libros_disponibles.values():
            if categoria.lower() == libro.categoria.lower():
                resultados.append(libro)

        for usuario in self._usuarios.values():
            for libro in usuario.libros_prestados:
                if categoria.lower() == libro.categoria.lower():
                    resultados.append(libro)

        return resultados