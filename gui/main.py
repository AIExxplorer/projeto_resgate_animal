import tkinter as tk
from tkinter import messagebox
import requests

class AnimalRescueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Animal Rescue System")

        # Exemplo de GUI para adicionar um animal
        self.label_name = tk.Label(root, text="Nome do Animal")
        self.label_name.grid(row=0, column=0)

        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1)

        self.label_species = tk.Label(root, text="Espécie")
        self.label_species.grid(row=1, column=0)

        self.entry_species = tk.Entry(root)
        self.entry_species.grid(row=1, column=1)

        self.button_add = tk.Button(root, text="Adicionar Animal", command=self.add_animal)
        self.button_add.grid(row=2, columnspan=2)

    def add_animal(self):
        name = self.entry_name.get()
        species = self.entry_species.get()

        if not name or not species:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")
            return

        data = {
            "name": name,
            "species": species,
            "sex": "Desconhecido",
            "rescue_date": "2024-08-08"
        }

        response = requests.post("http://localhost:5000/animals", json=data)

        if response.status_code == 201:
            messagebox.showinfo("Sucesso", "Animal adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao adicionar o animal")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimalRescueApp(root)
    root.mainloop()