import pygame
from outils_jeu import *

LARGEUR = 1280
HAUTEUR = 720
scene = "menu"
fenetre = creer_fenetre(LARGEUR, HAUTEUR, "Chromatica : Bleeding Doll")

noir = (15, 10, 15)
blanc = (245, 245, 245)
gris = (210, 175, 175)
rouge = (140, 10, 30)
rose = (230, 20, 75)

font = pygame.font.Font("font.ttf", 36)

# Chargement des images hors de la boucle 🖼️
image_fond = pygame.image.load("open_screen.png")
image_fond = pygame.transform.scale(image_fond, (LARGEUR, HAUTEUR))

image_fond_scene1 = pygame.image.load("scene1.jpg")
image_fond_scene1 = pygame.transform.scale(image_fond_scene1, (LARGEUR, HAUTEUR))

# Lancement de la musique du menu 🎶
pygame.mixer.music.load("start_music.mp3")
pygame.mixer.music.play(-1)

fin = False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

    fenetre.fill(noir)

    # --- GESTION DU MENU ---
    if scene == "menu":
        fenetre.blit(image_fond, (0, 0))
        start = dessiner_bouton("Jouer", 230, 420, 200, 50, gris, blanc, noir)

        if start == True:
            scene = "scene1"
            pygame.mixer.music.stop()


    elif scene == "scene1":
        fenetre.blit(image_fond_scene1, (0, 0))
        afficher_texte("Bienvenue dans l'aventure !", 450, 360, rose, font)

    pygame.display.flip()

pygame.quit()
