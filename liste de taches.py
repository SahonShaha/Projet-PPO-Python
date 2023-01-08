#Permet d'utiliser le module "Tkinter"
from tkinter import *

#Une ligne de code nécessaire pour que la fenêtre s'ouvre
root = Tk()

#Taille de la fenêtre
root.geometry("640x650")

#Titre du programme 
root.title("List de tâches")

#Endroit oû l'utilisateur peut entrer le titre de la tâche et une date
enter = Entry(root)
time = Entry(root)

#Ajout de texte 
myLabelenter = Label(root, text = "Entrer un tâche: ")
myLabeltime = Label(root, text= "Entrer une date: ")

#Place le texte
myLabelenter.grid(row=0, column= 0)
enter.grid(row= 0, column= 1)
myLabeltime.grid(row= 1, column= 0)
time.grid(row= 1, column= 1)

#Endroit oû la liste sera formée
list = Listbox(root, height= 30, width= 40)
list.grid(row = 2, column= 1) 


#Le button qui permet d'ajouter une tâche dans la liste 
def addtask():
    list.insert(END, enter.get() + " " + "|" + " " + time.get())
    enter.delete(0, END)
    time.delete(0, END)

#Boutton qui ferme l'application 
def exitbutton():
    root.destroy()
    root.quit()

#Effacer une tâche  
def deletetask():
    list.delete(ANCHOR)

#Oû les bouttons seront plaçées et leur couler, taille et nom des bouttons
addtaskButton = Button(root, text= "Ajouter la tâche", bg= "green", fg= "yellow", command= addtask)
exitButton = Button(root, text= "Quitter", bg= "red", fg= "white", command= exitbutton)
deleteButton = Button(root, text= "Enlever la tâche", command= deletetask)

#Place les bouttons
addtaskButton.grid(row= 0, column= 2)
exitButton.grid(row = 1, column= 2)
deleteButton.grid(row= 2, column= 3)


#Permet de garder l'application ifiniement 
root.mainloop() 