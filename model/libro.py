class Libro:
    """Representa un libro disponible dentro de la biblioteca."""

    def __init__(self, id_libro, titulo, autor, categoria):
        # El modelo conserva la informacion basica del libro.
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponible = True
