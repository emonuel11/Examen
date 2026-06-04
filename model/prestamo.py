class Prestamo:
    """Representa la relacion entre un lector, un libro y una fecha."""

    def __init__(self, id_prestamo, lector, libro, fecha_prestamo):
        # Prestamo conecta objetos ya existentes; no decide reglas de inventario.
        self.id_prestamo = id_prestamo
        self.lector = lector
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None
        self.activo = True
