import tkinter as tk
from tkinter import messagebox, ttk


class GestionLibros:
    """Pantalla para registrar y consultar libros."""

    def __init__(self, ventana, libro_controller):
        self.ventana = ventana
        self.libro_controller = libro_controller
        self.entradas = {}

        self.ventana.title("Gestion de Libros")
        self.ventana.geometry("850x420")
        self.crear_widgets()

    def crear_widgets(self):
        # Formulario de datos del libro.
        formulario = ttk.Frame(self.ventana, padding=10)
        formulario.pack(fill=tk.X)

        campos = ["codigo", "titulo", "autor", "categoria", "cantidad"]
        etiquetas = {
            "codigo": "Codigo",
            "titulo": "Titulo",
            "autor": "Autor",
            "categoria": "Categoria",
            "cantidad": "Cantidad disponible",
        }
        for columna, campo in enumerate(campos):
            ttk.Label(formulario, text=etiquetas[campo]).grid(
                row=0, column=columna, padx=5, pady=5, sticky=tk.W
            )
            entrada = ttk.Entry(formulario)
            entrada.grid(row=1, column=columna, padx=5, pady=5, sticky=tk.EW)
            self.entradas[campo] = entrada
            formulario.columnconfigure(columna, weight=1)

        botones = ttk.Frame(self.ventana, padding=10)
        botones.pack(fill=tk.X)

        ttk.Button(botones, text="Registrar", command=self.registrar).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(botones, text="Buscar por codigo", command=self.buscar_por_codigo).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(
            botones, text="Buscar por categoria", command=self.buscar_por_categoria
        ).pack(side=tk.LEFT, padx=5)
        ttk.Button(botones, text="Consultar todos", command=self.consultar_todos).pack(
            side=tk.LEFT, padx=5
        )

        columnas = ("codigo", "titulo", "autor", "categoria", "cantidad")
        # Tabla para mostrar libros registrados o filtrados.
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        for columna in columnas:
            self.tabla.heading(columna, text=columna.capitalize())
            self.tabla.column(columna, width=150)
        self.tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def registrar(self):
        try:
            # Se convierten datos simples de la GUI y se delega al controller.
            libro = self.libro_controller.registrar_libro(
                self.entradas["codigo"].get(),
                self.entradas["titulo"].get(),
                self.entradas["autor"].get(),
                self.entradas["categoria"].get(),
                int(self.entradas["cantidad"].get()),
            )
            self.mostrar_libros([libro])
            messagebox.showinfo("Registro exitoso", "Libro registrado correctamente.")
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def buscar_por_codigo(self):
        try:
            libro = self.libro_controller.buscar_por_codigo(
                self.entradas["codigo"].get()
            )
            self.mostrar_libros([libro])
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def buscar_por_categoria(self):
        try:
            libros = self.libro_controller.buscar_por_categoria(
                self.entradas["categoria"].get()
            )
            self.mostrar_libros(libros)
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def consultar_todos(self):
        libros = self.libro_controller.consultar_libros()
        self.mostrar_libros(libros)

    def mostrar_libros(self, libros):
        # Muestra los objetos Libro en filas de la tabla.
        self.limpiar_tabla()
        for libro in libros:
            self.tabla.insert(
                "",
                tk.END,
                values=(
                    libro.id_libro,
                    libro.titulo,
                    libro.autor,
                    libro.categoria,
                    getattr(libro, "cantidad", 0),
                ),
            )

    def limpiar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
