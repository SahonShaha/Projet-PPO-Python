#Les variables suivantes demandent à l'utilisateur d'entrez leur résultat. 
fr = input("Entrez votre résulat de français: ")
chimie = input("Entrez votre résultat de chimie: ")
phy = input("Entrez votre résultat de physique: ")
eng = input("Entrez votre résultat d'anglais: ")
fin = input('Entrez votre résulat de finance: ')
mc = input('Entrez votre résultat de monde contemporain: ')
math = input("Entrez votre résulatat de mathématiques: ")
art = input("Entrez votre résultat d'arts plastiques: ")
gym = input("Entrez votre résultat d'éducation physique: ")
ecr = input("Entrez votre résulatat d'éthique et culture religieuse: ")



#'try:' est la commande qui permet d'essayer une action, dans ce cas un calcul. Si il y a une erreur, la calculation ne marchera pas et il y aura un message d'erreur qui apparaitra avec la commande 'except'.
try:
 print(round(((int(fr) * 8) + (int(chimie) * 4) + (int(phy) * 4) + (int(eng) * 4) + (int(fin) * 2) + (int(mc) * 2) + (int(math) * 6) + (int(art) * 2) + (int(gym) * 2) + (int(ecr) * 2))/36))
except:
    print("Résulat invalide. S'il vous plaît entrez des données valables.")
