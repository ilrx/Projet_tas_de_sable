#############################################
# groupe 1
# Ilerioluwa OLAYODE
# Aymeric GOUDOUT
# Sam BARBOSA
# https://github.com/ilrx/Projet_tas_de_sable
#############################################

######################
#Import des librairies
######################

import tkinter as tk

##########################
#Définition des constantes
##########################

HAUTEUR = 500
LARGEUR = 500

##################################
#Définition des variables globales
##################################

liste_x = list()
liste_y = list()

#########################
#Définition des fonctions
#########################

def generation():
    pass

####################
#Programme principal
####################

root = tk.Tk()
root.title('Tas de Sable - Groupe 1')
canvas = tk.Canvas(root,height=HAUTEUR,width=LARGEUR,bg='black')
button_generation = tk.Button(root,text='Génération',command=generation,activebackground='red')

button_generation.grid(row=0,column=0)
canvas.grid(row=0,column=1)

root.mainloop()