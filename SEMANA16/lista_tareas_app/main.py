import tkinter as tk
from ui.app_tkinter import AppTkinter


def main():
    root = tk.Tk()
    app = AppTkinter(root)
    root.mainloop()


if __name__ == "__main__":
    main()