from model.lector import Lector


class LectorService:
    def __init__(self, lector_repository):
        self.lector_repository = lector_repository

    def registrar_lector(self, id_lector, nombre, correo, telefono, comunidad):
        if self.lector_repository.exists(id_lector):
            raise ValueError("Ya existe un lector con esa identificacion.")
        if not nombre:
            raise ValueError("El nombre del lector es obligatorio.")
        if not correo:
            raise ValueError("El correo del lector es obligatorio.")
        if not telefono:
            raise ValueError("El telefono del lector es obligatorio.")
        if not comunidad:
            raise ValueError("La comunidad del lector es obligatoria.")

        lector = Lector(id_lector, nombre, correo, telefono)
        lector.comunidad = comunidad
        self.lector_repository.add(lector)
        return lector

    def consultar_lectores(self):
        return self.lector_repository.get_all()

    def buscar_por_identificacion(self, identificacion):
        lector = self.lector_repository.get_by_id(identificacion)
        if lector is None:
            raise ValueError("No existe un lector con esa identificacion.")
        return lector

    def buscar_por_comunidad(self, comunidad):
        if not comunidad:
            raise ValueError("La comunidad es obligatoria para realizar la busqueda.")

        lectores_encontrados = []
        for lector in self.lector_repository.get_all():
            if getattr(lector, "comunidad", None) == comunidad:
                lectores_encontrados.append(lector)

        return lectores_encontrados
