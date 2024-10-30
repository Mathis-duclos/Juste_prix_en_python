from random import randint
from time import time
import tkinter as tk
from tkinter import messagebox

class JustePrixGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Le Juste Prix")
        self.master.geometry("400x300")
        background_color = '#C0E0DE'  # Teinte de fond 
        self.master.configure(bg=background_color)

        self.liste_prix = [4, 35, 5, 1200, 42990, 1229, 949, 22, 65, 11, 359, 1139, 449, 49, 365, 79]
        self.liste_objet = ["Brosse à dent en bambou", "Bouteille de gaz de 13kg", "Rose Rouge à l'unité",
                            "Prix du permis de conduire en conduite accompagnée", "Tesla modèle 3",
                            "iPhone 15 Pro", "Aspirateur balai Dyson v15s", "Une souris filaire sur Amazon",
                            "Amazon Echo Dot 5", "place de cinéma CGR Plein tarif",
                            "Lunettes Ray-Ban Meta Healiner avec verres polarisants",
                            "Samsung Galaxy Z Flip 5", "Google Pixel Watch 2 4G",
                            "Oreiller à mémoire de forme Emma", "Cookeo Connect avce 3 accessoires Moulinex",
                            "Machine à café Mini Me Automatique Nescafé Dolce Gusto"]

        self.label_objet = tk.Label(master, text="Quel est le prix de cet objet?", bg=background_color)
        self.label_objet.pack()

        self.objet_var = tk.StringVar()
        self.objet_label = tk.Label(master, textvariable=self.objet_var, bg=background_color)
        self.objet_label.pack()

        self.approximation_entry = tk.Entry(master)
        self.approximation_entry.pack()

        self.submit_button = tk.Button(master, text="Soumettre", command=self.deviner, bg="#6879D0", fg="white")
        self.submit_button.pack()

        self.restart_button = tk.Button(master, text="Rejouer", command=self.rejouer, bg="#6879D0", fg="white")
        self.restart_button.pack()

        self.quitter_button = tk.Button(master, text="Quitter", command=self.quitter, bg="#ED254E", fg="white")
        self.quitter_button.pack()

        self.t1 = 0
        self.nb_erreurs = 0
        self.index_objet = 0  # Indice de l'objet actuel
        self.jouer()

    def jouer(self):
        self.index_objet = randint(0, len(self.liste_objet) - 1)
        self.prix = self.liste_prix[self.index_objet]
        self.objet = self.liste_objet[self.index_objet]
        self.objet_var.set(self.objet)
        self.t1 = time()

    def deviner(self):
        try:
            approximation = int(self.approximation_entry.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")
            return

        if approximation < self.prix:
            messagebox.showinfo("Résultat", "C'est plus.")
            self.nb_erreurs += 1
        elif approximation > self.prix:
            messagebox.showinfo("Résultat", "C'est moins.")
            self.nb_erreurs += 1
        else:
            t2 = int(time() - self.t1)
            messagebox.showinfo("Résultat", "Oui oui oui, c'est le juste prix !\nTemps : {} secondes\nErreurs : {}".format(t2, self.nb_erreurs))
            self.rejouer()

    def rejouer(self):
        self.approximation_entry.delete(0, tk.END)
        self.nb_erreurs = 0
        self.jouer()

    def quitter(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = JustePrixGame(root)
    root.mainloop()
    