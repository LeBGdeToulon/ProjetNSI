import pygame
from pygame import *
from pygame.gfxdraw import *
from pygame.time import *
from random import *

def collision(liste, largeur_objet, Xperso, Yperso, direction):
    """ Calcule si il y a une collision avec un obstacle """
    contacte = False

    for coordliste in liste:
        if (coordliste[0] - Xperso) ** 2 + (coordliste[1] - Yperso) ** 2 < largeur_objet ** 2:
            contacte = True

    return contacte

def update():
    if niveau == 0: # Si on est à la page initiale
        fenetre.fill((0,0,0))
        fenetre.blit(imagefondmenu,(0,0))
        fenetre.blit(imagetitre,(300,200))
        box(fenetre,(560,490,80,60),(0,0,252))
        texte_jouer = police.render("Jouer",1,(255,255,255))
        fenetre.blit(texte_jouer,(570,500))

    if niveau == 1: # Si on est au premier niveau
        fenetre.blit(imagefond,(0,0))
        fenetre.blit(imagefond,(600,0))

        for pierre in pierres:
            fenetre.blit(imagepierre,(pierre[0], pierre[1]))
        
        fenetre.blit(imagediamant,coordonneestresor)

        if direction == "left":
            fenetre.blit(imagepersonnagegauche,(xperso,yperso))
        elif direction == "right":
            fenetre.blit(imagepersonnagedroite,(xperso,yperso))

        

    
        fenetre.blit(imagemenu, (0, 0))

    display.flip()


# Chargement de la page et des images
pygame.init()
largeur = 1200
hauteur = 600
fenetre = display.set_mode((largeur,hauteur))
display.set_caption("Projet jeu")
imagefond = image.load("PROJET_DELVIG_CHATELAIN/images/sol1.png")
imagepersonnagegauche = image.load("PROJET_DELVIG_CHATELAIN/images/Explorateurgauche.png").convert_alpha()
imagepersonnagedroite = image.load("PROJET_DELVIG_CHATELAIN/images/Explorateurdroite.png").convert_alpha()
imagepierre = image.load("PROJET_DELVIG_CHATELAIN/images/pierre.png").convert_alpha()
imagemenu = image.load("PROJET_DELVIG_CHATELAIN/images/logomenu.png").convert_alpha()
imagediamant = image.load("PROJET_DELVIG_CHATELAIN/images/diamant.png").convert_alpha()
imagefondmenu = image.load("PROJET_DELVIG_CHATELAIN/images/PixelIslands.png")
imagetitre = image.load("PROJET_DELVIG_CHATELAIN/images/JoemamaJones.png").convert_alpha()
police = pygame.font.SysFont("arial",30)

# Coordonnées du joueur
xperso = 300
yperso = 400
coordonneesperso = (xperso,yperso)
largeurpersonnage = 40
hauteurpersonnage = 57

# creer toutes les pierres puis les ajoutes dans une liste
nombrepierres = 10
largeurpierre = 55
pierres = []
for i in range(nombrepierres):
    pierres.append((randint(0, 1200), randint(0, 600)))

coordonneestresor = (randint(1,1135),randint(1,535))

# Paramètres de base
niveau = 0 # 0 : menu, 1 : niveau 1, 2 : un potentiel niveau plus dur
direction = ""
key.set_repeat(1,10)
continuer = True

while continuer:

    for event in pygame.event.get():
        
        if event.type == MOUSEBUTTONDOWN:
            clique = mouse.get_pos()
            if 560 < clique[0] < 640 and 490 < clique[1] < 550: # Si on clique sur la case bleue "jouer"
                niveau = 1

        if event.type == QUIT:
            continuer = False

    
        # mouvement du joueur
        if event.type == KEYDOWN: # Déplacements
            if event.key == K_UP and collision(pierres, largeurpierre, xperso, yperso, direction) == False:
                direction = "up"
                yperso -= 5
            if event.key == K_DOWN and collision(pierres, largeurpierre, xperso, yperso, direction) == False:
                direction = "down"
                yperso += 5
            if event.key == K_LEFT and collision(pierres, largeurpierre, xperso, yperso, direction) == False:
                direction = "left"
                xperso -= 5
            if event.key == K_RIGHT and collision(pierres, largeurpierre, xperso, yperso, direction) == False:
                direction = "right"
                xperso += 5

            if event.type == QUIT:
                continuer = False

    update()

pygame.quit()