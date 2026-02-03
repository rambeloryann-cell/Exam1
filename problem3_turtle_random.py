#Problème 3 : Dessin graphique aléatoire avec Turtle

import turtle
import random

def carre(taille):
    for _ in range(4):
        turtle.forward(taille)
        turtle.right(90)

def triangle(taille):
    for _ in range(3):
        turtle.forward(taille)
        turtle.right(120)

def cercle(taille):
    turtle.circle(taille)

while True:
    try:
        N=int(input("Entrez un entier (entre 0 et 9) : "))
        if 0<=N<=9:
            break
        else:
            print("Entrez un entier (entre 0 et 9) : ")
    except ValueError:
        print("Veillez saisir un entier entre 0 et 9")

formes=[carre, triangle, cercle]
couleurs=["red", "blue", "green", "purple", "orange", "black"]
turtle.speed(0)

for i in range(N):
    turtle.penup()
    x=random.randint(-200, 200)
    y=random.randint(-200, 200)
    turtle.goto(x, y)
    turtle.pendown()

    turtle.color(random.choice(couleurs))
    taille = random.randint(20, 400)
    random.choice(formes)(taille)

turtle.done()