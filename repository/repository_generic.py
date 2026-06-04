class RepositoryGeneric:
    """Repositorio reutilizable para guardar y buscar cualquier entidad."""

    def __init__(self, nombre_id):
        # nombre_id indica que atributo se usara como llave: id_lector, id_libro, etc.
        self.nombre_id = nombre_id

        # La lista mantiene el almacenamiento general y permite recorrer todo.
        self.elementos = []

        # El diccionario permite busquedas rapidas por identificador.
        self.indice = {}

    def add(self, entidad):
        # Se obtiene el id dinamicamente para que el repositorio sirva a varios modelos.
        id_entidad = getattr(entidad, self.nombre_id)
        self.elementos.append(entidad)
        self.indice[id_entidad] = entidad

    def get_all(self):
        # Se devuelve una copia para proteger la lista interna.
        return list(self.elementos)

    def get_by_id(self, id_entidad):
        # La busqueda usa dict, por eso no necesita recorrer toda la lista.
        return self.indice.get(id_entidad)

    def exists(self, id_entidad):
        return id_entidad in self.indice

    def update(self, id_entidad, entidad_actualizada):
        # Si no existe, se informa con False para que service decida que hacer.
        if not self.exists(id_entidad):
            return False

        # Se actualiza tambien la lista para mantener sincronizados list y dict.
        for posicion, entidad in enumerate(self.elementos):
            if getattr(entidad, self.nombre_id) == id_entidad:
                self.elementos[posicion] = entidad_actualizada
                break

        nuevo_id = getattr(entidad_actualizada, self.nombre_id)
        if nuevo_id != id_entidad:
            del self.indice[id_entidad]

        self.indice[nuevo_id] = entidad_actualizada
        return True
