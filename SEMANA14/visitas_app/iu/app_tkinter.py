import tkinter as tk
from tkinter import ttk, messagebox


class AppTkinter:
    """
    Clase que construye la interfaz gráfica del sistema.
    Recibe el servicio por parámetro (inyección de dependencias).
    """

    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        self.root.title("Sistema de Registro de Visitantes")
        self.root.geometry("800x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#EAF2F8")

        self.crear_interfaz()

    def crear_interfaz(self):
        """
        Construye todos los componentes de la interfaz gráfica.
        """
        titulo = tk.Label(
            self.root,
            text="Sistema de Registro de Visitantes",
            font=("Arial", 18, "bold"),
            bg="#EAF2F8",
            fg="#1F3A5F"
        )
        titulo.pack(pady=15)

        # Frame principal
        frame_principal = tk.Frame(self.root, bg="#EAF2F8")
        frame_principal.pack(fill="both", expand=True, padx=20, pady=10)

        # =========================
        # FORMULARIO
        # =========================
        frame_formulario = tk.Frame(frame_principal, bg="white", bd=2, relief="groove")
        frame_formulario.pack(side="left", fill="y", padx=(0, 15))

        subtitulo_form = tk.Label(
            frame_formulario,
            text="Datos del Visitante",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#1F3A5F"
        )
        subtitulo_form.pack(pady=15)

        # Cédula
        lbl_cedula = tk.Label(frame_formulario, text="Cédula:", font=("Arial", 11, "bold"), bg="white")
        lbl_cedula.pack(anchor="w", padx=20, pady=(10, 5))

        self.entry_cedula = tk.Entry(frame_formulario, font=("Arial", 11), width=25)
        self.entry_cedula.pack(padx=20, pady=(0, 10))

        # Nombre completo
        lbl_nombre = tk.Label(frame_formulario, text="Nombre completo:", font=("Arial", 11, "bold"), bg="white")
        lbl_nombre.pack(anchor="w", padx=20, pady=(10, 5))

        self.entry_nombre = tk.Entry(frame_formulario, font=("Arial", 11), width=25)
        self.entry_nombre.pack(padx=20, pady=(0, 10))

        # Motivo de visita
        lbl_motivo = tk.Label(frame_formulario, text="Motivo de visita:", font=("Arial", 11, "bold"), bg="white")
        lbl_motivo.pack(anchor="w", padx=20, pady=(10, 5))

        self.entry_motivo = tk.Entry(frame_formulario, font=("Arial", 11), width=25)
        self.entry_motivo.pack(padx=20, pady=(0, 15))

        # Botones
        btn_registrar = tk.Button(
            frame_formulario,
            text="Registrar",
            font=("Arial", 11, "bold"),
            bg="#2E8B57",
            fg="white",
            width=20,
            command=self.registrar_visitante
        )
        btn_registrar.pack(pady=8)

        btn_eliminar = tk.Button(
            frame_formulario,
            text="Eliminar",
            font=("Arial", 11, "bold"),
            bg="#C0392B",
            fg="white",
            width=20,
            command=self.eliminar_visitante
        )
        btn_eliminar.pack(pady=8)

        btn_limpiar = tk.Button(
            frame_formulario,
            text="Limpiar Campos",
            font=("Arial", 11, "bold"),
            bg="#2874A6",
            fg="white",
            width=20,
            command=self.limpiar_campos
        )
        btn_limpiar.pack(pady=8)

        # =========================
        # TABLA
        # =========================
        frame_tabla = tk.Frame(frame_principal, bg="white", bd=2, relief="groove")
        frame_tabla.pack(side="right", fill="both", expand=True)

        subtitulo_tabla = tk.Label(
            frame_tabla,
            text="Lista de Visitantes",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#1F3A5F"
        )
        subtitulo_tabla.pack(pady=15)

        columnas = ("Cédula", "Nombre completo", "Motivo de visita")

        self.tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=15)

        self.tree.heading("Cédula", text="Cédula")
        self.tree.heading("Nombre completo", text="Nombre completo")
        self.tree.heading("Motivo de visita", text="Motivo de visita")

        self.tree.column("Cédula", width=120, anchor="center")
        self.tree.column("Nombre completo", width=180, anchor="center")
        self.tree.column("Motivo de visita", width=180, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=15, pady=15)

    def registrar_visitante(self):
        """
        Registra un visitante utilizando el servicio.
        """
        cedula = self.entry_cedula.get().strip()
        nombre = self.entry_nombre.get().strip()
        motivo = self.entry_motivo.get().strip()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return

        exito = self.servicio.registrar_visitante(cedula, nombre, motivo)

        if not exito:
            messagebox.showerror("Error", "Ya existe un visitante con esa cédula.")
            return

        self.actualizar_tabla()
        self.limpiar_campos()
        messagebox.showinfo("Registro exitoso", "Visitante registrado correctamente.")

    def eliminar_visitante(self):
        """
        Elimina el visitante seleccionado en la tabla.
        """
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning("Sin selección", "Seleccione un visitante para eliminar.")
            return

        valores = self.tree.item(seleccionado[0], "values")
        cedula = valores[0]

        eliminado = self.servicio.eliminar_visitante(cedula)

        if eliminado:
            self.actualizar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Eliminado", "Visitante eliminado correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo eliminar el visitante.")

    def limpiar_campos(self):
        """
        Limpia los campos del formulario.
        """
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)

    def actualizar_tabla(self):
        """
        Limpia y vuelve a cargar la tabla con los datos actuales.
        """
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        for visitante in self.servicio.obtener_visitantes():
            self.tree.insert(
                "",
                "end",
                values=(visitante.cedula, visitante.nombre_completo, visitante.motivo_visita)
            )