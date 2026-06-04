from model.prestamo import Prestamo


class PrestamoService:
    def __init__(self, prestamo_repository, lector_repository, libro_repository):
        self.prestamo_repository = prestamo_repository
        self.lector_repository = lector_repository
        self.libro_repository = libro_repository

    def registrar_prestamo(self, codigo_prestamo, identificacion_lector, codigo_libro, fecha_prestamo, cantidad):
        if self.prestamo_repository.exists(codigo_prestamo):
            raise ValueError("Ya existe un prestamo con ese codigo.")
        if not self.lector_repository.exists(identificacion_lector):
            raise ValueError("El lector indicado no existe.")
        if not self.libro_repository.exists(codigo_libro):
            raise ValueError("El libro indicado no existe.")
        if cantidad <= 0:
            raise ValueError("La cantidad del prestamo debe ser mayor a 0.")

        lector = self.lector_repository.get_by_id(identificacion_lector)
        libro = self.libro_repository.get_by_id(codigo_libro)
        inventario_actual = getattr(libro, "cantidad", 0)

        if inventario_actual < cantidad:
            raise ValueError("No hay inventario suficiente para realizar el prestamo.")

        prestamo = Prestamo(codigo_prestamo, lector, libro, fecha_prestamo)
        prestamo.codigo_prestamo = codigo_prestamo
        prestamo.cantidad = cantidad

        libro.cantidad = inventario_actual - cantidad
        libro.disponible = libro.cantidad > 0

        self.libro_repository.update(codigo_libro, libro)
        self.prestamo_repository.add(prestamo)
        return prestamo

    def consultar_prestamos(self):
        return self.prestamo_repository.get_all()

    def buscar_por_lector(self, identificacion_lector):
        prestamos_encontrados = []
        for prestamo in self.prestamo_repository.get_all():
            if prestamo.lector.id_lector == identificacion_lector:
                prestamos_encontrados.append(prestamo)

        return prestamos_encontrados

    def buscar_por_fecha(self, fecha_prestamo):
        prestamos_encontrados = []
        for prestamo in self.prestamo_repository.get_all():
            if prestamo.fecha_prestamo == fecha_prestamo:
                prestamos_encontrados.append(prestamo)

        return prestamos_encontrados
