import tkinter as tk
from tkinter import ttk
import pandas as pd

# Chargement des données à partir d'un fichier CSV
data = pd.read_csv("Data/Main_file.csv",delimiter='|',header=0)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Tableau de données")

# Création d'un widget de table
table = ttk.Treeview(root, columns=data.columns, show="headings")
table.pack()

# Configuration des colonnes
indx=0
for col in data.columns:
    print(col)
    table.heading(indx, text=col)
    indx+=1

# Ajout des lignes de données
for _, row in data.iterrows():
    table.insert("", "end", values=list(row))

# Boucle principale de l'application
root.mainloop()
