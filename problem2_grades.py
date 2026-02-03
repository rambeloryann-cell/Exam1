#Problème 2 : Gestion des notes d'une classe

students= [
    ("Ali", 12),
    ("Fatou", 17),
    ("Moussa", 9),
    ("Awa", 14),
    ("Ibrahima", 7),
]

def calculerMoyenne(liste):
    total=0
    for _, note in liste:
        total+=note
    return total/len(liste)

def trouverMaxMin(liste):
    notes =[note for _, note in liste]
    return max(notes), min(notes)

print("Liste des étudiants et leurs notes :")
for nom, note in students:
    print(f"{nom} : {note}")

moy=calculerMoyenne(students)
noteMax, noteMin= trouverMaxMin(students)

print("-----------------------------")
print(f"Moyenne de la classe : {moy}")
print(f"Note maximale : {noteMax}")
print(f"Note minimale : {noteMin}")

admis=[]
ajourne=[]
for nom, note in students:
    if note>=10:
        admis.append(nom)
    else:
        ajourne.append(nom)

print(f"Étudiants admis : {admis}")
print(f"Étudiants ajournés : {ajourne}")