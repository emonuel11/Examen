import tkinter as tk
from tkinter import messagebox, ttk


class GestionLectores:
    """Pantalla para registrar y consultar lectores."""

    def __init__(self, ventana, lector_controller):
        self.ventana = ventana
        self.lector_controller = lector_controller
        self.entradas = {}

        self.ventana.title("Gestion de Lectores")
        self.ventana.geometry("760x420")
        self.crear_widgets()

    def crear_widgets(self):
        # Formulario de entrada de datos para la GUI.
        formulario = ttk.Frame(self.ventana, padding=10)
        formulario.pack(fill=tk.X)

        campos = ["identificacion", "nombre", "correo", "comunidad"]
        for columna, campo in enumerate(campos):
            ttk.Label(formulario, text=campo.capitalize()).grid(
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
        ttk.Button(
            botones,
            text="Buscar por identificacion",
            command=self.buscar_por_identificacion,
        ).pack(side=tk.LEFT, padx=5)
        ttk.Button(
            botones, text="Buscar por comunidad", command=self.buscar_por_comunidad
        ).pack(side=tk.LEFT, padx=5)
        ttk.Button(botones, text="Consultar todos", command=self.consultar_todos).pack(
            side=tk.LEFT, padx=5
        )

        columnas = ("id", "nombre", "correo", "comunidad")
        # Treeview se usa para mostrar resultados en formato de tabla.
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        for columna in columnas:
            self.tabla.heading(columna, text=columna.capitalize())
            self.tabla.column(columna, width=150)
        self.tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def registrar(self):
        try:
            # La vista toma valores del formulario y llama al controller.
            lector = self.lector_controller.registrar_lector(
                int(self.entradas["identificacion"].get()),
                self.entradas["nombre"].get(),
                self.entradas["correo"].get(),
                "No registrado",
                self.entradas["comunidad"].get(),
            )
            self.mostrar_lectores([lector])
            messagebox.showinfo("Registro exitoso", "Lector registrado correctamente.")
        except ValueError as error:
            # Los errores de negocio vienen desde service y se muestran aqui.
            messagebox.showerror("Error", str(error))

    def buscar_por_identificacion(self):
        try:
            lector = self.lector_controller.buscar_por_identificacion(
                int(self.entradas["identificacion"].get())
            )
            self.mostrar_lectores([lector])
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def buscar_por_comunidad(self):
        try:
            lectores = self.lector_controller.buscar_por_comunidad(
                self.entradas["comunidad"].get()
            )
            self.mostrar_lectores(lectores)
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def consultar_todos(self):
        lectores = self.lector_controller.consultar_lectores()
        self.mostrar_lectores(lectores)

    def mostrar_lectores(self, lectores):
        # La vista solo presenta datos recibidos; no decide reglas.
        self.limpiar_tabla()
        for lector in lectores:
            self.tabla.insert(
                "",
                tk.END,
                values=(
                    lector.id_lector,
                    lector.nombre,
                    lector.correo,
                    getattr(lector, "comunidad", ""),
                ),
            )

    def limpiar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
