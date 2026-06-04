class ReporteController:
    """Intermediario entre la vista de reportes y ReporteService."""

    def __init__(self, reporte_service):
        self.reporte_service = reporte_service

    def lectores_por_comunidad(self):
        # Devuelve datos ya preparados por service para que la vista solo los muestre.
        return self.reporte_service.lectores_por_comunidad()

    def libros_inventario_bajo(self, cantidad_minima=3):
        return self.reporte_service.libros_inventario_bajo(cantidad_minima)

    def top_3_libros_mas_prestados(self):
        return self.reporte_service.top_3_libros_mas_prestados()
