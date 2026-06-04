class Lector:
    """Representa a una persona que puede pedir libros prestados."""

    def __init__(self, id_lector, nombre, correo, telefono):
        # El modelo solo guarda datos; las validaciones fuertes viven en service.
        self.id_lector = id_lector
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.activo = True
