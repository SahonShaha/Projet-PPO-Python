#Importe le module 'Tkinter' avec l'extension 'messagebox' et le module 'time' pour le temps. 
from tkinter import *
from tkinter import messagebox
import time 

#Une ligne de code nécessaire pour que la fenêtre s'ouvre
root = Tk()

#Taille de la fenêtre et nom de l'application 
root.geometry("400x300")
root.title("Technique Pomodoro - Sahon Shaha")

#Si nous le mettons pas ces variables en 'StringVar()', 'Tkinter' ne peut pas analyser les données. 
heure = StringVar() 
minute = StringVar()
seconde = StringVar()

#L'heure, minute et seconde commence a 00.
heure.set('00')
minute.set('00')
seconde.set('00')

#Le temps que l'utilisateur entre devient les variables de tantôt. 
heureEntry = Entry(root, textvariable = heure)
minuteEntry = Entry(root, textvariable=  minute)
secondeEntry = Entry(root, textvariable = seconde)

#Pour placer les 'Entry'. 
heureEntry.grid(row= 1, column= 0)
minuteEntry.grid(row= 1, column= 1)
secondeEntry.grid(row= 1, column= 2)

#Pour indentifiez l'endroit ou l'utilisateur peut entrer les données de temps. 
heureLabel = Label(root, text= "Heure")
minuteLabel = Label(root, text= "Minute")
secondeLabel = Label(root,text= "Seoncde")

#Place les textes. 
heureLabel.grid(row= 0, column= 0)
minuteLabel.grid(row= 0, column= 1)
secondeLabel.grid(row= 0, column= 2)


def principale():
    #On transforme les données de l'utilisateur en seconde pour faciliter les calculations. 
    temps = int(heure.get())*3600 + int(minute.get())*60 + int(seconde.get())*1
    #Quand le temps atteint 0, le programme s'arretera.  
    while temps > -1:
        #Le temps s'affiche. '0:2d' signifie qu'il y a deux décimals pour afficher l'heure, la minute et la seconde. 
        heure.set('0:2d'.format(heure))
        minute.set('0:2d'.format(minute))
        seconde.set('0:2d'.format(seconde))
        
        #'root.update' est la manière pour mettre a jour l'interface graphique.
        root.update
        #Ensuite, on met a jour le programme par un 'tick' qui dure 1/10000000 d'une seconde 
        time.sleep(1)
        
        #On soustrait le temps par 1. 
        temps -= 1

        #Une fois que le temps atteint 0, une compte a rebours de 10 minutes commence qui s'agit comme pause. 
        if temps == 0:
            heure.set("00")
            minute.set("10")
            seconde.set('00')

            temps = int(600)
            messagebox.showinfo("C'est fini!" , "Felicitations pour avoir étudiez")
            
            # Une fois que le compte à rebours de la pause est terminé, un nouveau message apparait et on remet le temps a 00.
            while temps > -1:
                root.update
                time.sleep(1)

                temps -= 1

                if temps == 0:
                    heure.set("00")
                    minute.set("00")
                    seconde.set('00')
                    messagebox.showinfo('Message',"Continuez a etudier?")
            break #'break' permet d'arreter la boucle. 

#On affiche le boutton et on attache la fonction 'principale()' avec 'Button(command=)'
boutton = Button(root, text ='Étudiez!', command= principale)
boutton.grid(row = 2, column= 1)

#Permet de garder l'application ifiniement 
root.mainloop()
