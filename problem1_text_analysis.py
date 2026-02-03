#Problème 1 : Analyse et transformation d'un texte

def cptVoyelle(texte):
    voyelles="aeiouy"
    nb=0
    for c in texte:
        if c in voyelles:
            nb+= 1
    return nb

phrase=input("Entrez une phrase : ")

while not phrase.replace(" ", "").isalpha():
    print("Veuillez saisir que des lettres")
    phrase = input("Entrez une phrase: ")

phraseMin=phrase.lower()
liste=phraseMin.split()

nbMots=len(liste)
motLong=max(liste, key=len)
nbVoyelles=cptVoyelle(phraseMin)

nouvelleListe=[]
for mot in liste:
    if len(mot)%2 ==1:
        nouvelleListe.append(mot.upper())
    else:
        nouvelleListe.append(mot)
nouvellePhrase=" ".join(nouvelleListe)

print(f"-------------------------------\nPhrase en minuscules : {phraseMin}")
print(f"Liste de mots : {liste}")
print(f"Nombre total de mots : {nbMots}")
print(f"Mot le plus long : {motLong}")
print(f"Nombre de voyelles : {nbVoyelles}")
print(f"Nouvelle phrase : {nouvellePhrase}")