import tkinter as tk
import pygubu


class Application():
    "GUI"
    def __init__(self, master):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('OWO.ui')
        self.mainwindow = builder.get_object('PRINCIPAL', master)

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()