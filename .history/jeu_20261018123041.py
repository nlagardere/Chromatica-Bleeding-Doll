import pygame
from outils_jeu import *

largeur = 1280
hauteur = 720
scene = "menu"
fenetre = creer_fenetre(largeur, hauteur, "Chromatica : Bleeding Doll")

noir = (15, 10, 15)
blanc = (245, 245, 245)
gris = (210, 175, 175)
rouge = (140, 10, 30)
rose = (230, 20, 75)

police = pygame.font.Font("font.ttf", 36)
police_sous_titre = pygame.font.Font("font.ttf", 20)

image_fond = pygame.image.load("open_screen.png")
image_fond = pygame.transform.scale(image_fond, (largeur, hauteur))

image_fond_choix_musique = pygame.image.load("choix_musique.jpg")
image_fond_choix_musique = pygame.transform.scale(image_fond_choix_musique, (largeur, hauteur))

son_clic = pygame.mixer.Sound("clic.wav")

pygame.mixer.music.load("start_music.mp3")
pygame.mixer.music.play(-1)

fin = False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

    fenetre.fill(noir)

    if scene == "menu":
        fenetre.blit(image_fond, (0, 0))
        demarrer = dessiner_bouton("Jouer", 230, 420, 200, 50, gris, blanc, noir, arrondi=10, couleur_tour=rose, epaisseur_tour=3)

        if demarrer == True:
            scene = "choix_musique"
            pygame.mixer.music.stop()
            son_clic.play()
            pygame.mixer.music.load("crowd.mp3")
            pygame.mixer.music.play(-1)
        
    elif scene == "choix_musique":
        fenetre.blit(image_fond_choix_musique, (0, 0))
        
        afficher_texte("Choisis la musique d'entrée :", 80, 50, rose, police)

        morceau_1 = dessiner_bouton("Bad Romance", 80, 140, 280, 50, gris, blanc, noir, arrondi=10, couleur_tour=rose, epaisseur_tour=3)
        afficher_texte("L'hymne ultime pour faire exploser le stade !", 80, 200, blanc, police_sous_titre)

        morceau_2 = dessiner_bouton("Abracadabra", 80, 260, 280, 50, gris, blanc, noir, arrondi=10, couleur_tour=rose, epaisseur_tour=3)
        afficher_texte("Sortilège pop & vibe mystique garantie.", 80, 320, blanc, police_sous_titre)

        morceau_3 = dessiner_bouton("Just Dance", 80, 380, 280, 50, gris, blanc, noir, arrondi=10, couleur_tour=rose, epaisseur_tour=3)
        afficher_texte("Le classique de 2008 pour enflammer le dancefloor !", 80, 440, blanc, police_sous_titre)

        morceau_4 = dessiner_bouton("Poker Face", 80, 500, 280, 50, gris, blanc, noir, arrondi=10, couleur_tour=rose, epaisseur_tour=3)
        afficher_texte("Un beat iconique, impassible et dévastateur.", 80, 560, blanc, police_sous_titre)

        if morceau_1:
            son_clic.play()
        elif morceau_2:
            son_clic.play()
        elif morceau_3:
            son_clic.play()
        elif morceau_4:
            son_clic.play()

    pygame.display.flip()

pygame.quit()
