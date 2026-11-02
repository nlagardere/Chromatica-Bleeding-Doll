import pygame
from outils_jeu import *


LARGEUR = 900
HAUTEUR = 700

fenetre = creer_fenetre(LARGEUR, HAUTEUR, "Chromatica : Bleeding Doll")

# Couleurs 🎨
noir = (15, 10, 15)
blanc = (245, 245, 245)
gris = (210, 175, 175)
rouge = (140, 10, 30)
rose = (230, 20, 75)

image_fond = pygame.image.load("open_screen.png")
image_fond = pygame.transform.scale(image_fond, (LARGEUR, HAUTEUR))

fin = False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

    fenetre.fill(noir)
    fenetre.blit(image_fond, (0, 0))
    pygame.display.flip()

pygame.quit()
