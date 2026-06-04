from model.lector import Lector
from model.libro import Libro
from model.prestamo import Prestamo
from repository.repository_generic import RepositoryGeneric


class ReporteService:
    """Genera reportes sin depender de la interfaz grafica."""

    def __init__(
        self,
        lector_repository: RepositoryGeneric[Lector],
        libro_repository: RepositoryGeneric[Libro],
        prestamo_repository: RepositoryGeneric[Prestamo],
    ):
        self.lector_repository = lector_repository
        self.libro_repository = libro_repository
        self.prestamo_repository = prestamo_repository

    def lectores_por_comunidad(self):
        # set evita repetir comunidades al construir el reporte.
        comunidades = set()
        for lector in self.lector_repository.get_all():
            comunidad = getattr(lector, "comunidad", None)
            if comunidad:
                comunidades.add(comunidad)

        reporte = []
        for comunidad in comunidades:
            cantidad = 0
            for lector in self.lector_repository.get_all():
                if getattr(lector, "comunidad", None) == comunidad:
                    cantidad += 1

            # Cada resultado del reporte se guarda como tupla.
            reporte.append((comunidad, cantidad))

        return reporte

    def libros_inventario_bajo(self, cantidad_minima=3):
        reporte = []
        for libro in self.libro_repository.get_all():
            cantidad = getattr(libro, "cantidad", 0)
            if cantidad <= cantidad_minima:
                # Tupla: codigo, titulo y cantidad disponible.
                reporte.append((libro.id_libro, libro.titulo, cantidad))

        return reporte

    def top_3_libros_mas_prestados(self):
        # dict acumula la cantidad prestada por cada codigo de libro.
        prestamos_por_libro = {}
        for prestamo in self.prestamo_repository.get_all():
            codigo_libro = prestamo.libro.id_libro
            cantidad = getattr(prestamo, "cantidad", 1)

            if codigo_libro not in prestamos_por_libro:
                prestamos_por_libro[codigo_libro] = 0

            prestamos_por_libro[codigo_libro] += cantidad

        reporte = []
        for codigo_libro, cantidad_prestada in prestamos_por_libro.items():
            libro = self.libro_repository.get_by_id(codigo_libro)
            if libro is not None:
                # Tupla: codigo, titulo y total prestado.
                reporte.append((codigo_libro, libro.titulo, cantidad_prestada))

        # Se ordena de mayor a menor y se devuelven solo los primeros tres.
        reporte.sort(key=lambda resultado: resultado[2], reverse=True)
        return reporte[:3]
