import pygame
from outils_jeu import *

LARGEUR = 1000
HAUTEUR = 1000
fenetre = creer_fenetre(LARGEUR, HAUTEUR, "Chromatica : Bleeding Doll")

fin = False
while fin == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

    pygame.display.flip()

pygame.quit()
