from model.libro import Libro


class LibroService:
    """Contiene las reglas de negocio relacionadas con libros."""

    def __init__(self, libro_repository):
        self.libro_repository = libro_repository

    def registrar_libro(self, codigo, titulo, autor, categoria, cantidad):
        # Antes de guardar se comprueba duplicado, datos obligatorios e inventario.
        if self.libro_repository.exists(codigo):
            raise ValueError("Ya existe un libro con ese codigo.")
        if not titulo:
            raise ValueError("El titulo del libro es obligatorio.")
        if not autor:
            raise ValueError("El autor del libro es obligatorio.")
        if not categoria:
            raise ValueError("La categoria del libro es obligatoria.")
        if cantidad <= 0:
            raise ValueError("La cantidad del libro debe ser mayor a 0.")

        libro = Libro(codigo, titulo, autor, categoria)

        # codigo y cantidad son datos usados por busquedas, inventario y prestamos.
        libro.codigo = codigo
        libro.cantidad = cantidad
        self.libro_repository.add(libro)
        return libro

    def consultar_libros(self):
        return self.libro_repository.get_all()

    def buscar_por_codigo(self, codigo):
        libro = self.libro_repository.get_by_id(codigo)
        if libro is None:
            raise ValueError("No existe un libro con ese codigo.")
        return libro

    def buscar_por_categoria(self, categoria):
        if not categoria:
            raise ValueError("La categoria es obligatoria para realizar la busqueda.")

        # Categoria no es llave primaria, por eso se filtra recorriendo todos los libros.
        libros_encontrados = []
        for libro in self.libro_repository.get_all():
            if libro.categoria == categoria:
                libros_encontrados.append(libro)

        return libros_encontrados
