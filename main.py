import tkinter as tk

from controller.lector_controller import LectorController
from controller.libro_controller import LibroController
from controller.prestamo_controller import PrestamoController
from controller.reporte_controller import ReporteController
from repository.repository_generic import RepositoryGeneric
from service.lector_service import LectorService
from service.libro_service import LibroService
from service.prestamo_service import PrestamoService
from service.reporte_service import ReporteService
from view.main_window import MainWindow


def crear_aplicacion(root):
    lector_repository = RepositoryGeneric("id_lector")
    libro_repository = RepositoryGeneric("id_libro")
    prestamo_repository = RepositoryGeneric("id_prestamo")

    lector_service = LectorService(lector_repository)
    libro_service = LibroService(libro_repository)
    prestamo_service = PrestamoService(
        prestamo_repository,
        lector_repository,
        libro_repository,
    )
    reporte_service = ReporteService(
        lector_repository,
        libro_repository,
        prestamo_repository,
    )

    lector_controller = LectorController(lector_service)
    libro_controller = LibroController(libro_service)
    prestamo_controller = PrestamoController(prestamo_service)
    reporte_controller = ReporteController(reporte_service)

    return MainWindow(
        root,
        lector_controller,
        libro_controller,
        prestamo_controller,
        reporte_controller,
    )


def main():
    root = tk.Tk()
    crear_aplicacion(root)
    root.mainloop()


if __name__ == "__main__":
    main()
