import pygame
from outils_jeu import *

LARGEUR = 1920
HAUTEUR = 1080
fenetre = creer_fenetre(LARGEUR, HAUTEUR, "Chromatica : Bleeding Doll")
noir = (15, 10, 15)
blanc = (245, 245, 245)


fin = False
while fin == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

    pygame.display.flip()

pygame.quit()
