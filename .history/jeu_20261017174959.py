import pygame
from outils_jeu import *


LARGEUR = 1280
HAUTEUR = 720

fenetre = creer_fenetre(LARGEUR, HAUTEUR, "Chromatica : Bleeding Doll")

# Couleurs 🎨
noir = (15, 10, 15)
blanc = (245, 245, 245)
gris = (210, 175, 175)
rouge = (140, 10, 30)
rose = (230, 20, 75)

font = pygame.font.Font(font, 36)
image_fond = pygame.image.load("open_screen.png")
image_fond = pygame.transform.scale(image_fond, (LARGEUR, HAUTEUR))

fin = False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

    fenetre.fill(noir)
    fenetre.blit(image_fond, (0, 0))
    afficher_texte("Bienvenue dans l'aventure !", 50, 50, blanc)
    pygame.display.flip()

pygame.quit()
