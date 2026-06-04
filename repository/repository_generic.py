class RepositoryGeneric:
    def __init__(self, nombre_id):
        self.nombre_id = nombre_id
        self.elementos = []
        self.indice = {}

    def add(self, entidad):
        id_entidad = getattr(entidad, self.nombre_id)
        self.elementos.append(entidad)
        self.indice[id_entidad] = entidad

    def get_all(self):
        return list(self.elementos)

    def get_by_id(self, id_entidad):
        return self.indice.get(id_entidad)

    def exists(self, id_entidad):
        return id_entidad in self.indice

    def update(self, id_entidad, entidad_actualizada):
        if not self.exists(id_entidad):
            return False

        for posicion, entidad in enumerate(self.elementos):
            if getattr(entidad, self.nombre_id) == id_entidad:
                self.elementos[posicion] = entidad_actualizada
                break

        nuevo_id = getattr(entidad_actualizada, self.nombre_id)
        if nuevo_id != id_entidad:
            del self.indice[id_entidad]

        self.indice[nuevo_id] = entidad_actualizada
        return True
