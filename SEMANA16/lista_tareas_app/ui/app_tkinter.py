import tkinter as tk
from tkinter import messagebox
from servicios.tarea_servicio import TareaServicio


class AppTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("520x450")
        self.root.resizable(False, False)

        self.servicio = TareaServicio()

        self.crear_componentes()
        self.vincular_eventos()

    def crear_componentes(self):
        self.label_titulo = tk.Label(
            self.root,
            text="Aplicación GUI - Lista de Tareas",
            font=("Arial", 15, "bold")
        )
        self.label_titulo.pack(pady=10)

        self.frame_superior = tk.Frame(self.root)
        self.frame_superior.pack(pady=10)

        self.entry_tarea = tk.Entry(self.frame_superior, width=35, font=("Arial", 12))
        self.entry_tarea.grid(row=0, column=0, padx=5)

        self.btn_agregar = tk.Button(
            self.frame_superior,
            text="Añadir tarea",
            width=14,
            command=self.agregar_tarea
        )
        self.btn_agregar.grid(row=0, column=1, padx=5)

        self.listbox_tareas = tk.Listbox(
            self.root,
            width=58,
            height=14,
            font=("Arial", 12),
            activestyle="none",
            selectbackground="#b7d7f7"
        )
        self.listbox_tareas.pack(pady=10)

        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=10)

        self.btn_completar = tk.Button(
            self.frame_botones,
            text="Marcar completada",
            width=18,
            command=self.marcar_tarea
        )
        self.btn_completar.grid(row=0, column=0, padx=5)

        self.btn_eliminar = tk.Button(
            self.frame_botones,
            text="Eliminar tarea",
            width=15,
            command=self.eliminar_tarea
        )
        self.btn_eliminar.grid(row=0, column=1, padx=5)

        self.label_atajos = tk.Label(
            self.root,
            text="Atajos: Enter = Añadir | C = Completar | Delete/D = Eliminar | Esc = Salir",
            font=("Arial", 10),
            fg="gray"
        )
        self.label_atajos.pack(pady=10)

    def vincular_eventos(self):
        self.entry_tarea.bind("<Return>", self.agregar_tarea_evento)
        self.root.bind("<c>", self.marcar_tarea_evento)
        self.root.bind("<C>", self.marcar_tarea_evento)
        self.root.bind("<Delete>", self.eliminar_tarea_evento)
        self.root.bind("<d>", self.eliminar_tarea_evento)
        self.root.bind("<D>", self.eliminar_tarea_evento)
        self.root.bind("<Escape>", self.cerrar_aplicacion)

    def agregar_tarea(self):
        texto = self.entry_tarea.get()
        agregado = self.servicio.agregar_tarea(texto)

        if not agregado:
            messagebox.showwarning("Advertencia", "Por favor, escriba una tarea.")
            return

        self.entry_tarea.delete(0, tk.END)
        self.entry_tarea.focus()
        self.actualizar_lista()

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def marcar_tarea(self):
        seleccion = self.listbox_tareas.curselection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcarla.")
            return

        indice = seleccion[0]
        self.servicio.marcar_completada(indice)
        self.actualizar_lista()

    def marcar_tarea_evento(self, event):
        self.marcar_tarea()

    def eliminar_tarea(self):
        seleccion = self.listbox_tareas.curselection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminarla.")
            return

        indice = seleccion[0]
        self.servicio.eliminar_tarea(indice)
        self.actualizar_lista()

    def eliminar_tarea_evento(self, event):
        self.eliminar_tarea()

    def cerrar_aplicacion(self, event=None):
        self.root.destroy()

    def actualizar_lista(self):
        self.listbox_tareas.delete(0, tk.END)

        tareas = self.servicio.obtener_tareas()

        for i, tarea in enumerate(tareas):
            if tarea.completada:
                texto = f"✔ {tarea.texto} [COMPLETADA]"
                self.listbox_tareas.insert(tk.END, texto)
                self.listbox_tareas.itemconfig(i, fg="green")
            else:
                texto = f"• {tarea.texto} [PENDIENTE]"
                self.listbox_tareas.insert(tk.END, texto)
                self.listbox_tareas.itemconfig(i, fg="black")