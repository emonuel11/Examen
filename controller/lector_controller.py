class LectorController:
    """Intermediario entre la vista de lectores y LectorService."""

    def __init__(self, lector_service):
        self.lector_service = lector_service

    def registrar_lector(self, id_lector, nombre, correo, telefono, comunidad):
        # El controller no valida negocio; solo delega al service.
        return self.lector_service.registrar_lector(
            id_lector, nombre, correo, telefono, comunidad
        )

    def consultar_lectores(self):
        return self.lector_service.consultar_lectores()

    def buscar_por_identificacion(self, identificacion):
        return self.lector_service.buscar_por_identificacion(identificacion)

    def buscar_por_comunidad(self, comunidad):
        return self.lector_service.buscar_por_comunidad(comunidad)
