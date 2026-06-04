class ReporteService:
    def __init__(self, lector_repository, libro_repository, prestamo_repository):
        self.lector_repository = lector_repository
        self.libro_repository = libro_repository
        self.prestamo_repository = prestamo_repository

    def lectores_por_comunidad(self):
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
            reporte.append((comunidad, cantidad))

        return reporte

    def libros_inventario_bajo(self, cantidad_minima=3):
        reporte = []
        for libro in self.libro_repository.get_all():
            cantidad = getattr(libro, "cantidad", 0)
            if cantidad <= cantidad_minima:
                reporte.append((libro.id_libro, libro.titulo, cantidad))

        return reporte

    def top_3_libros_mas_prestados(self):
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
                reporte.append((codigo_libro, libro.titulo, cantidad_prestada))

        reporte.sort(key=lambda resultado: resultado[2], reverse=True)
        return reporte[:3]
