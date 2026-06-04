import tkinter as tk
from tkinter import ttk

from view.gestion_lectores import GestionLectores
from view.gestion_libros import GestionLibros
from view.gestion_prestamos import GestionPrestamos
from view.gestion_reportes import GestionReportes


class MainWindow:
    def __init__(
        self,
        root,
        lector_controller,
        libro_controller,
        prestamo_controller,
        reporte_controller,
    ):
        self.root = root
        self.lector_controller = lector_controller
        self.libro_controller = libro_controller
        self.prestamo_controller = prestamo_controller
        self.reporte_controller = reporte_controller

        self.root.title("Biblioteca Comunitaria")
        self.root.geometry("420x320")
        self.crear_widgets()

    def crear_widgets(self):
        contenedor = ttk.Frame(self.root, padding=20)
        contenedor.pack(fill=tk.BOTH, expand=True)

        titulo = ttk.Label(
            contenedor,
            text="Sistema de Gestion de Biblioteca Comunitaria",
            font=("Arial", 14, "bold"),
        )
        titulo.pack(pady=10)

        ttk.Button(
            contenedor,
            text="Gestion de Lectores",
            command=self.abrir_gestion_lectores,
        ).pack(fill=tk.X, pady=5)
        ttk.Button(
            contenedor,
            text="Gestion de Libros",
            command=self.abrir_gestion_libros,
        ).pack(fill=tk.X, pady=5)
        ttk.Button(
            contenedor,
            text="Gestion de Prestamos",
            command=self.abrir_gestion_prestamos,
        ).pack(fill=tk.X, pady=5)
        ttk.Button(
            contenedor,
            text="Reportes",
            command=self.abrir_gestion_reportes,
        ).pack(fill=tk.X, pady=5)
        ttk.Button(contenedor, text="Salir", command=self.root.destroy).pack(
            fill=tk.X, pady=15
        )

    def abrir_gestion_lectores(self):
        ventana = tk.Toplevel(self.root)
        GestionLectores(ventana, self.lector_controller)

    def abrir_gestion_libros(self):
        ventana = tk.Toplevel(self.root)
        GestionLibros(ventana, self.libro_controller)

    def abrir_gestion_prestamos(self):
        ventana = tk.Toplevel(self.root)
        GestionPrestamos(ventana, self.prestamo_controller)

    def abrir_gestion_reportes(self):
        ventana = tk.Toplevel(self.root)
        GestionReportes(ventana, self.reporte_controller)
