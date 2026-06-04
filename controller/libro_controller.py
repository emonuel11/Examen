class LibroController:
    def __init__(self, libro_service):
        self.libro_service = libro_service

    def registrar_libro(self, codigo, titulo, autor, categoria, cantidad):
        return self.libro_service.registrar_libro(
            codigo, titulo, autor, categoria, cantidad
        )

    def consultar_libros(self):
        return self.libro_service.consultar_libros()

    def buscar_por_codigo(self, codigo):
        return self.libro_service.buscar_por_codigo(codigo)

    def buscar_por_categoria(self, categoria):
        return self.libro_service.buscar_por_categoria(categoria)
