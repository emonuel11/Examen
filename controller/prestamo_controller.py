class PrestamoController:
    def __init__(self, prestamo_service):
        self.prestamo_service = prestamo_service

    def registrar_prestamo(
        self, codigo_prestamo, identificacion_lector, codigo_libro, fecha_prestamo, cantidad
    ):
        return self.prestamo_service.registrar_prestamo(
            codigo_prestamo,
            identificacion_lector,
            codigo_libro,
            fecha_prestamo,
            cantidad,
        )

    def consultar_prestamos(self):
        return self.prestamo_service.consultar_prestamos()

    def buscar_por_lector(self, identificacion_lector):
        return self.prestamo_service.buscar_por_lector(identificacion_lector)

    def buscar_por_fecha(self, fecha_prestamo):
        return self.prestamo_service.buscar_por_fecha(fecha_prestamo)
