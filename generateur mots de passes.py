import random

print("Générateur de Mot de Passe")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+~'

nb_mdp = input('Combien de mots de passe voulez-vous: ')
nb_mdp = int(nb_mdp)

nb_lettres_mdp = input('Combien de lettres voulez-vous dans votre mot de passe: ')
nb_lettres_mdp = int(nb_lettres_mdp)

print('\nVoici vos mots de passe: ')

for mots_de_passes in range(nb_mdp):
    mdp = ''
    for c in range(nb_lettres_mdp):
        mdp += random.choice(chars)
    print(mdp)