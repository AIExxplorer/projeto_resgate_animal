import tkinter as tk
from tkinter import ttk
try:
    import requests
except ImportError:
    print("Please install the 'requests' module.")

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Gestão de Resgate Animal")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill='both')

        animais_frame = ttk.Frame(notebook)
        doacoes_frame = ttk.Frame(notebook)
        doadores_frame = ttk.Frame(notebook)

        notebook.add(animais_frame, text='Animais')
        notebook.add(doacoes_frame, text='Doações')
        notebook.add(doadores_frame, text='Doadores')

        self.create_animais_widgets(animais_frame)
        self.create_doacoes_widgets(doacoes_frame)
        self.create_doadores_widgets(doadores_frame)

    def create_animais_widgets(self, frame):
        tree = ttk.Treeview(frame, columns=('ID', 'Nome', 'Espécie'), show='headings')
        tree.heading('ID', text='ID')
        tree.heading('Nome', text='Nome')
        tree.heading('Espécie', text='Espécie')
        tree.pack(expand=True, fill='both')

        refresh_button = ttk.Button(frame, text='Atualizar', command=lambda: self.refresh_data(tree, 'animais'))
        refresh_button.pack()

    def create_doacoes_widgets(self, frame):
        tree = ttk.Treeview(frame, columns=('ID', 'Valor', 'Data'), show='headings')
        tree.heading('ID', text='ID')
        tree.heading('Valor', text='Valor')
        tree.heading('Data', text='Data')
        tree.pack(expand=True, fill='both')

        refresh_button = ttk.Button(frame, text='Atualizar', command=lambda: self.refresh_data(tree, 'doacoes'))
        refresh_button.pack()

    def create_doadores_widgets(self, frame):
        tree = ttk.Treeview(frame, columns=('ID', 'Nome', 'Email'), show='headings')
        tree.heading('ID', text='ID')
        tree.heading('Nome', text='Nome')
        tree.heading('Email', text='Email')
        tree.pack(expand=True, fill='both')

        refresh_button = ttk.Button(frame, text='Atualizar', command=lambda: self.refresh_data(tree, 'doadores'))
        refresh_button.pack()

    def refresh_data(self, tree, endpoint):
        tree.delete(*tree.get_children())
        response = requests.get(f'http://localhost:5000/api/{endpoint}')
        data = response.json()
        for item in data:
            tree.insert('', 'end', values=tuple(item.values()))

if __name__ == "__main__":
    app = Application()
    app.mainloop()