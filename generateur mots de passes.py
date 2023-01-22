#Importe l'extension "random" qui nous permettra de choisir une lettre au hasard
import random

#C'est le titre du programme 
print("Générateur de Mot de Passe")

#Les possiblités de caractères pour créer un mot de passe
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+~'

#La fonction 'input()' permet de se souvenir d'une réposne de l'utilisateur en le plaçant dans un variable. 
nb_mdp = input('Combien de mots de passe voulez-vous: ')
nb_mdp = int(nb_mdp) #'int()' permet de transformer une phrase en chiffre. Chaque message envoyé par l'utilisateur est considéré comme un 'str()' c'est à dire une phrase.

#Même utilité que le morceau de code dernier sauf pour la quantité de lettres dans le mot de passe. 
nb_lettres_mdp = input('Combien de lettres voulez-vous dans votre mot de passe: ')
nb_lettres_mdp = int(nb_lettres_mdp)

#'\n' permet de sauter une ligne. C'est pas nécessaire mais ça rend plus beau. 
print('\nVoici vos mots de passe: ')

#Un boucle est contruit avec une variable (dans ce cas 'mots_de_passes') pour le nombre dans 'nb_mdp'. C'est comme dire pour x dans 7, fait quelque chose 7 fois.
for mots_de_passes in range(nb_mdp):
    mdp = '' #On garde cette variable vide pour ajouter des caractères. 
    for c in range(nb_lettres_mdp): #On ajoute une lettre pour le nombre de lettre que l'utilisateur va demander. 
        mdp += random.choice(chars) #L'ordinateur choisi au hasard un caractère de la liste 'chars'. Cette action va se répéter pour le nombre dans 'nb_lettres_mdp'.
    print(mdp) #On affiche le mots de passe. Puis on le repete dépendemment sur le nombre de mots de passe demandé. 

#Fondamentalement, c'est une boucle dans un boucle qui, en premier creer un mot de passe de la taille choisi, puis répète cette action pour le nombre de mots de passe demandé. 
