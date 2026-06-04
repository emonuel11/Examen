class Prestamo:
    def __init__(self, id_prestamo, lector, libro, fecha_prestamo):
        self.id_prestamo = id_prestamo
        self.lector = lector
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None
        self.activo = True
