
import pygame
from outils_jeu import *
import random

largeur = 1280
hauteur = 720
scene = "menu"
fenetre = creer_fenetre(largeur, hauteur, "Chromatica : Bleeding Doll")
compteur_temps = 0 

noir = (15, 10, 15)
blanc = (245, 245, 245)
gris = (210, 175, 175)
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

btn_x = 600
btn_y = 350
score_concert = 0

def desactiver(func):
  def wrapper(*args, **kwargs):
    return None

  return wrapper  

fin = False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

    fenetre.fill(noir)

    if scene == "menu":
        fenetre.blit(image_fond, (0, 0))
        demarrer = dessiner_bouton("Jouer", 230, 420, 200, 50, gris, blanc, noir, arrondi=10, couleur_tour=rose, epaisseur_tour=3)
        compteur_temps += 1
        if (compteur_temps//180)%2== 0:
            alpha_banner = dessiner_bouton("Version Alpha incomplète. Les boutons doivent être double cliqués.", 0, 650, 1280, 40, rose, blanc, noir, arrondi=0, couleur_tour=blanc, epaisseur_tour=1)
        else:
            alpha_banner = dessiner_bouton("Version Alpha incomplète. Les boutons doivent être double cliqués.", 0, 650, 1280, 40 ,blanc ,rose, noir, arrondi=0, couleur_tour=blanc, epaisseur_tour=1)

        if demarrer == True:
            scene = "choix_musique"
            pygame.mixer.music.stop()
            son_clic.play()
            pygame.mixer.music.load("crowd.mp3")
            pygame.mixer.music.play(-1)
            compteur_temps = 0
        
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
        afficher_texte("Un beat iconique, et dévastateur.", 80, 560, blanc, police_sous_titre)

        afficher_texte("Équipe & Scène :", 760, 140, rose, police)
        afficher_texte("Foule : 80 000 fans déchaînés", 760, 200, blanc, police_sous_titre)
        afficher_texte("Éclairage & Lasers : Prêts", 760, 250, blanc, police_sous_titre)
        afficher_texte("Pyrotechnie : Armée", 760, 300, blanc, police_sous_titre)
        afficher_texte("Retours son & System : OK", 760, 350, blanc, police_sous_titre)
        afficher_texte("Tenues & Maquillage : Chromatica", 760, 400, blanc, police_sous_titre)
        afficher_texte("Danseurs : En place", 760, 450, blanc, police_sous_titre)
        afficher_texte("STATUT : En attente du morceau...", 760, 530, rose, police_sous_titre)

        if morceau_1:
            son_clic.play()
            pygame.mixer.music.stop()
            scene = "bad_romance"
            score_concert = 0
            compteur_temps = 0
            pygame.mixer.music.load("bad_romance.mp3")
            pygame.mixer.music.play(-1)
        elif morceau_2:
            son_clic.play()
            pygame.mixer.music.stop()
            scene = "abracadabra"
            score_concert = 0
            compteur_temps = 0
            pygame.mixer.music.load("abracadabra.mp3")
            pygame.mixer.music.play(-1)
        elif morceau_3:
            son_clic.play()
            pygame.mixer.music.stop()
            scene = "just_dance"
            score_concert = 0
            compteur_temps = 0
            pygame.mixer.music.load("just_dance.mp3")
            pygame.mixer.music.play(-1)
        elif morceau_4:
            son_clic.play()
            pygame.mixer.music.stop()
            scene = "poker_face"
            score_concert = 0
            compteur_temps = 0
            pygame.mixer.music.load("poker_face.mp3")
            pygame.mixer.music.play(-1)

    elif scene == "bad_romance":
        fenetre.fill(noir)
        afficher_texte("Morceau : Bad Romance", 450, 30, rose, police_sous_titre)
        afficher_texte("Appuie sur le bouton pour enflammer le show !", 350, 80, blanc, police_sous_titre)
        afficher_texte(f"Score : " + str(score_concert), 50, 30, rose, police)

        compteur_temps += 1

        if dessiner_bouton("CLIQUE !", btn_x, btn_y, 140, 40, gris, blanc, noir, arrondi=8, couleur_tour=rose, epaisseur_tour=2):
            son_clic.play()
            score_concert += 1
            btn_x = random.randint(100, 1000)
            btn_y = random.randint(100, 550)

        if compteur_temps > 21540:
            scene = "score_final"

    elif scene == "abracadabra":
        fenetre.fill(noir)
        afficher_texte("Morceau : Abracadabra", 450, 30, rose, police_sous_titre)
        afficher_texte("Appuie sur le bouton pour enflammer le show !", 350, 80, blanc, police_sous_titre)
        afficher_texte(f"Score : " + str(score_concert), 50, 30, rose, police)
        compteur_temps += 1
        if compteur_temps > 4000:
            scene = "score_final"

        if dessiner_bouton("CLIQUE !", btn_x, btn_y, 140, 40, gris, blanc, noir, arrondi=8, couleur_tour=rose, epaisseur_tour=2):
            son_clic.play()
            score_concert += 1
            btn_x = random.randint(100, 1000)
            btn_y = random.randint(100, 550)

        if compteur_temps > 4000:
            scene = "score_final"

    elif scene == "just_dance":
        fenetre.fill(noir)
        afficher_texte("Morceau : Just Dance", 450, 30, rose, police_sous_titre)
        afficher_texte("Appuie sur le bouton pour enflammer le show !", 350, 80, blanc, police_sous_titre)
        afficher_texte(f"Score : " + str(score_concert), 50, 30, rose, police)

        compteur_temps += 1

        if dessiner_bouton("CLIQUE !", btn_x, btn_y, 140, 40, gris, blanc, noir, arrondi=8, couleur_tour=rose, epaisseur_tour=2):
            son_clic.play()
            score_concert += 1
            btn_x = random.randint(100, 1000)
            btn_y = random.randint(100, 550)


    elif scene == "poker_face":
        fenetre.fill(noir)
        afficher_texte("Morceau : Poker Face", 450, 30, rose, police_sous_titre)
        afficher_texte("Appuie sur le bouton pour enflammer le show !", 350, 80, blanc, police_sous_titre)
        afficher_texte(f"Score : " + str(score_concert), 50, 30, rose, police)

        compteur_temps += 1

        if dessiner_bouton("CLIQUE !", btn_x, btn_y, 140, 40, gris, blanc, noir, arrondi=8, couleur_tour=rose, epaisseur_tour=2):
            son_clic.play()
            score_concert += 1
            btn_x = random.randint(100, 1000)
            btn_y = random.randint(100, 550)
            
        if compteur_temps > 4000:
            scene = "score_final"

    elif scene == "score_final":
        afficher_texte("Fin du concert !", 500, 200, rose, police)
        afficher_texte(f"Ton score final est de : {score_concert}", 450, 280, blanc, police)

        btn_menu = dessiner_bouton("Retour au menu", 510, 400, 260, 50, gris, blanc, noir, arrondi=10, couleur_tour=rose, epaisseur_tour=3)
        
        if btn_menu:
            son_clic.play()
            scene = "menu"
            pygame.mixer.music.load("start_music.mp3")
            pygame.mixer.music.play(-1)

    pygame.display.flip()

pygame.quit()
