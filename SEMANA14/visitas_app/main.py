import tkinter as tk
from servicios.visita_servicio import VisitaServicio
from iu.app_tkinter import AppTkinter


def main():
    root = tk.Tk()
    servicio = VisitaServicio()
    app = AppTkinter(root, servicio)
    root.mainloop()


if __name__ == "__main__":
    main()