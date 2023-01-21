import tkinter as tk
from tkinter import ttk
import pandas as pd

# Chargement des données à partir d'un fichier CSV
data = pd.read_csv("Data/Main_file.csv",delimiter='|',header=0)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Tableau de données")

# Variables pour stocker les valeurs des entrées de saisie de texte
entries = {col: {i: tk.StringVar() for i in range(len(data))} for col in data.columns}

# Création d'un conteneur pour les entrées de saisie de texte
frame = ttk.Frame(root)
frame.pack()

# Fonction pour sauvegarder les modifications
def save():
    for col in data.columns:
        for i in range(len(data)):
            data.at[i, col] = entries[col][i].get()
    print(data)

# Fonction pour annuler les modifications
def cancel():
    for col in data.columns:
        for i in range(len(data)):
            entries[col][i].set(data.at[i, col])

# Ajout des entrées de saisie de texte
for i, row in data.iterrows():
    for j, col in enumerate(data.columns):
        entry = ttk.Entry(frame, textvariable=entries[col][i])
        entry.grid(row=i, column=j)

# Ajout des boutons pour sauvegarder et annuler les modifications
save_button = ttk.Button(root, text="Save", command=save)
save_button.pack()
cancel_button = ttk.Button(root, text="Cancel", command=cancel)
cancel_button.pack()

# Boucle principale de l'application
root.mainloop()
