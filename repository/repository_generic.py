from typing import Callable, Generic, TypeVar


T = TypeVar("T")


class RepositoryGeneric(Generic[T]):
    """Repositorio reutilizable para guardar y buscar cualquier entidad."""

    def __init__(self, obtener_id: str | Callable[[T], object]):
        # obtener_id puede ser el nombre de un atributo o una funcion que devuelva la llave.
        self.obtener_id = obtener_id

        # La lista mantiene el almacenamiento general y permite recorrer todo.
        self.elementos: list[T] = []

        # El diccionario permite busquedas rapidas por identificador.
        self.indice: dict[object, T] = {}

    def _obtener_id(self, entidad: T):
        if callable(self.obtener_id):
            return self.obtener_id(entidad)

        return getattr(entidad, self.obtener_id)

    def add(self, entidad: T):
        # Se obtiene la llave de forma dinamica para servir a cualquier modelo.
        id_entidad = self._obtener_id(entidad)
        self.elementos.append(entidad)
        self.indice[id_entidad] = entidad

    def get_all(self) -> list[T]:
        # Se devuelve una copia para proteger la lista interna.
        return list(self.elementos)

    def get_by_id(self, id_entidad: object) -> T | None:
        # La busqueda usa dict, por eso no necesita recorrer toda la lista.
        return self.indice.get(id_entidad)

    def exists(self, id_entidad: object) -> bool:
        return id_entidad in self.indice

    def update(self, id_entidad: object, entidad_actualizada: T) -> bool:
        # Si no existe, se informa con False para que service decida que hacer.
        if not self.exists(id_entidad):
            return False

        # Se actualiza tambien la lista para mantener sincronizados list y dict.
        for posicion, entidad in enumerate(self.elementos):
            if self._obtener_id(entidad) == id_entidad:
                self.elementos[posicion] = entidad_actualizada
                break

        nuevo_id = self._obtener_id(entidad_actualizada)
        if nuevo_id != id_entidad:
            del self.indice[id_entidad]

        self.indice[nuevo_id] = entidad_actualizada
        return True
