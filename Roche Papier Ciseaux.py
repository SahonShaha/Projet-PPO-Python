#Importe l'extension "random" qui nous permettra de choisir une action au hasard 
import random

#La fonction roche. Dépendemment sur l'option choisie par le joueur (la variable "userChoice"), il va déterminer s'il perd ou gagne. 
def roche():
    if userChoice == "Roche":
        print("Égalité :/")
    elif userChoice == "Ciseaux":
        print("Tu as perdu :(")
    elif userChoice == "Papier":
        print("Tu as gagné :D")

#La fonction ciseaux. Même role que la fonction roche. 
def ciseaux():
    if userChoice == "Roche":
        print("Tu as gagné :D")")
    elif userChoice == "Ciseaux":
        print("Égalité :/")
    elif userChoice == "Papier":
        print("Tu as perdu :(")

#La fonction papier. Même role que la fonction roche et ciseaux. 
def papier():
    if userChoice == "Roche":
        print("Tu as perdu :(")
    elif userChoice== "Ciseaux":
        print("Tu as gagné :D")
    elif userChoice == "Papier":
        print("Égalité :/")


#Ici, l'ordinateur demande au joueur de choisir une option. 
userChoice = input("Roche, Papier ou Ciseaux? ")

#Ici, l'ordinateur choisit au hasard un numéro qui représentera roche, papier ou ciseaux
res = random.randrange(1, 3)

#Si le resultat du tirage est 1, l'ordinateur a choisi roche. 2, il a choisi papier. 3, il a choisi ciseaux. Ensuite, les fonctions seront activées comme montré au début. 
if res == 1:
    roche()
elif res == 2:
    papier()
elif res == 3:
    ciseaux()
