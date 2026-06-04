import tkinter as tk
from tkinter import messagebox, ttk


class GestionPrestamos:
    """Pantalla para registrar y consultar prestamos."""

    def __init__(self, ventana, prestamo_controller):
        self.ventana = ventana
        self.prestamo_controller = prestamo_controller
        self.entradas = {}

        self.ventana.title("Gestion de Prestamos")
        self.ventana.geometry("900x420")
        self.crear_widgets()

    def crear_widgets(self):
        # Formulario con los datos necesarios para solicitar un prestamo.
        formulario = ttk.Frame(self.ventana, padding=10)
        formulario.pack(fill=tk.X)

        campos = [
            "codigo_prestamo",
            "identificacion_lector",
            "codigo_libro",
            "fecha",
            "cantidad",
        ]
        etiquetas = {
            "codigo_prestamo": "Codigo prestamo",
            "identificacion_lector": "Identificacion lector",
            "codigo_libro": "Codigo libro",
            "fecha": "Fecha",
            "cantidad": "Cantidad",
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
        ttk.Button(botones, text="Buscar por lector", command=self.buscar_por_lector).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(botones, text="Buscar por fecha", command=self.buscar_por_fecha).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(botones, text="Consultar todos", command=self.consultar_todos).pack(
            side=tk.LEFT, padx=5
        )

        columnas = ("codigo", "lector", "libro", "fecha", "cantidad")
        # Tabla con los prestamos encontrados o registrados.
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        for columna in columnas:
            self.tabla.heading(columna, text=columna.capitalize())
            self.tabla.column(columna, width=150)
        self.tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def registrar(self):
        try:
            # La regla de inventario no esta aqui; se ejecuta en PrestamoService.
            prestamo = self.prestamo_controller.registrar_prestamo(
                self.entradas["codigo_prestamo"].get(),
                int(self.entradas["identificacion_lector"].get()),
                self.entradas["codigo_libro"].get(),
                self.entradas["fecha"].get(),
                int(self.entradas["cantidad"].get()),
            )
            self.mostrar_prestamos([prestamo])
            messagebox.showinfo("Registro exitoso", "Prestamo registrado correctamente.")
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def buscar_por_lector(self):
        try:
            prestamos = self.prestamo_controller.buscar_por_lector(
                int(self.entradas["identificacion_lector"].get())
            )
            self.mostrar_prestamos(prestamos)
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def buscar_por_fecha(self):
        try:
            prestamos = self.prestamo_controller.buscar_por_fecha(
                self.entradas["fecha"].get()
            )
            self.mostrar_prestamos(prestamos)
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def consultar_todos(self):
        prestamos = self.prestamo_controller.consultar_prestamos()
        self.mostrar_prestamos(prestamos)

    def mostrar_prestamos(self, prestamos):
        # Convierte cada prestamo en una fila visual de la tabla.
        self.limpiar_tabla()
        for prestamo in prestamos:
            self.tabla.insert(
                "",
                tk.END,
                values=(
                    prestamo.id_prestamo,
                    prestamo.lector.id_lector,
                    prestamo.libro.id_libro,
                    prestamo.fecha_prestamo,
                    getattr(prestamo, "cantidad", 0),
                ),
            )

    def limpiar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
