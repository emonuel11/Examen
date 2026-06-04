import tkinter as tk
from tkinter import messagebox, ttk


class GestionReportes:
    def __init__(self, ventana, reporte_controller):
        self.ventana = ventana
        self.reporte_controller = reporte_controller

        self.ventana.title("Reportes")
        self.ventana.geometry("760x420")
        self.crear_widgets()

    def crear_widgets(self):
        botones = ttk.Frame(self.ventana, padding=10)
        botones.pack(fill=tk.X)

        ttk.Button(
            botones,
            text="Lectores por comunidad",
            command=self.lectores_por_comunidad,
        ).pack(side=tk.LEFT, padx=5)
        ttk.Button(
            botones,
            text="Libros con inventario bajo",
            command=self.libros_inventario_bajo,
        ).pack(side=tk.LEFT, padx=5)
        ttk.Button(
            botones,
            text="Top 3 libros mas prestados",
            command=self.top_3_libros_mas_prestados,
        ).pack(side=tk.LEFT, padx=5)

        self.tabla = ttk.Treeview(self.ventana, show="headings")
        self.tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def lectores_por_comunidad(self):
        try:
            resultados = self.reporte_controller.lectores_por_comunidad()
            self.configurar_tabla(("comunidad", "cantidad"))
            self.mostrar_resultados(resultados)
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def libros_inventario_bajo(self):
        try:
            resultados = self.reporte_controller.libros_inventario_bajo()
            self.configurar_tabla(("codigo", "titulo", "cantidad"))
            self.mostrar_resultados(resultados)
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def top_3_libros_mas_prestados(self):
        try:
            resultados = self.reporte_controller.top_3_libros_mas_prestados()
            self.configurar_tabla(("codigo", "titulo", "cantidad prestada"))
            self.mostrar_resultados(resultados)
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def configurar_tabla(self, columnas):
        self.tabla["columns"] = columnas
        for columna in columnas:
            self.tabla.heading(columna, text=columna.capitalize())
            self.tabla.column(columna, width=180)

    def mostrar_resultados(self, resultados):
        self.limpiar_tabla()
        for resultado in resultados:
            self.tabla.insert("", tk.END, values=resultado)

    def limpiar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
