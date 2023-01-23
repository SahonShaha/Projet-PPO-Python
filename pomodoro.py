#Importe le module 'Tkinter' avec l'extension 'messagebox' et le module 'time' pour le temps. 
from tkinter import *
from tkinter import messagebox
import time 

root = Tk()

root.geometry("400x300")
root.title("Technique Pomodoro - Sahon Shaha")

heure = StringVar() 
minute = StringVar()
seconde = StringVar()

heure.set('00')
minute.set('00')
seconde.set('00')

heureEntry = Entry(root, textvariable = heure)
minuteEntry = Entry(root, textvariable=  minute)
secondeEntry = Entry(root, textvariable = seconde)

heureEntry.grid(row= 1, column= 0)
minuteEntry.grid(row= 1, column= 1)
secondeEntry.grid(row= 1, column= 2)


heureLabel = Label(root, text= "Heure")
minuteLabel = Label(root, text= "Minute")
secondeLabel = Label(root,text= "Seoncde")

heureLabel.grid(row= 0, column= 0)
minuteLabel.grid(row= 0, column= 1)
secondeLabel.grid(row= 0, column= 2)

def ok():
    temps = int(heure.get())*3600 + int(minute.get())*60 + int(seconde.get())*1

    while temps > -1:
        heure.set('0:2d'.format(heure))
        minute.set('0:2d'.format(minute))
        seconde.set('0:2d'.format(seconde))

        root.update
        time.sleep(1)

        temps -= 1

        if temps == 0:
            heure.set("00")
            minute.set("10")
            seconde.set('00')

            temps = int(2)
            messagebox.showinfo("C'est fini!" , "Felicitations pour avoir étudiez")

            while temps > -1:
                root.update
                time.sleep(1)

                temps -= 1

                if temps == 0:
                    heure.set("00")
                    minute.set("00")
                    seconde.set('00')
                    messagebox.showinfo('Message',"Continuez a etudier?")
            break

boutton = Button(root, text ='Étudiez!', command= ok)
boutton.grid(row = 2, column= 1)


root.mainloop()
