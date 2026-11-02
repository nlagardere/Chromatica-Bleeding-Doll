import pygame
from outils_jeu import *

LARGEUR = 1024
HAUTEUR = 768
fenetre = creer_fenetre(LARGEUR, HAUTEUR, "Chromatica : Bleeding Doll")

fin = False
while fin == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

    pygame.display.flip()

pygame.quit()
