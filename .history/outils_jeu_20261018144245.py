"""
outils_jeu.py

Regroupe toutes les fonctions "boite noire" utilisees dans les projets guides
(aventure interactive et enquete point and click) : vous n'avez pas besoin de
comprendre le code de ce fichier.

Pour les utiliser, placez ce fichier dans le meme dossier que votre programme,
puis ecrivez en haut de votre fichier :

    from outils_jeu import *

Vous pourrez ensuite appeler directement creer_fenetre(), afficher_texte(),
dessiner_bouton(), zone_cliquable(), etc.
"""

import pygame
import time

# Ces variables sont remplies automatiquement par creer_fenetre() : vous n'avez
# pas besoin d'y toucher.
_fenetre = None
_largeur = None
_font_texte = None
_font_nom = None
_dialogue_en_cours = None
_dialogue_debut = 0
_images_redimensionnees = {}

ACCENT = (217, 161, 91)
FOND_BOITE = (18, 14, 32)
COULEUR_TEXTE = (244, 236, 216)


def creer_fenetre(largeur, hauteur, titre):
    """
    Cree la fenetre du jeu. A appeler une seule fois, tout au debut de votre
    programme, a la place de pygame.init() + pygame.display.set_mode(...).

    Parametres :
    -----------
        largeur, hauteur (int) : la taille de la fenetre en pixels.
        titre (str) : le titre affiche dans la barre de la fenetre.

    Retourne :
    -------
        fenetre (Surface) : la fenetre du jeu, sur laquelle vous pouvez dessiner
                             avec fenetre.blit(...) et fenetre.fill(...).
    """
    global _fenetre, _largeur, _font_texte, _font_nom
    pygame.init()
    _fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption(titre)
    _largeur = largeur
    _font_texte = pygame.font.Font(None, 22)
    _font_nom = pygame.font.Font(None, 26)
    return _fenetre


def afficher_texte(texte, x, y, couleur, police=None):
    """
    Affiche du texte a partir d'une position (x, y), avec un retour a la ligne
    automatique si le texte est plus long que la largeur de la fenetre.

    Parametres :
    -----------
        texte (str) : le texte a afficher.
        x, y (int) : la position d'affichage.
        couleur (tuple) : la couleur du texte, sous forme (R, G, B).
        police (Font) : (facultatif) la police a utiliser, creee par exemple avec
                         pygame.font.SysFont("arial", 40) ou
                         pygame.font.Font("ma_police.ttf", 40).
                         Si on ne la precise pas, une police par defaut est utilisee.
    """
    if police is None:
        police = _font_texte

    mots = texte.split(" ")
    ligne_actuelle = ""
    y_offset = 0
    for mot in mots:
        if police.size(ligne_actuelle + mot)[0] <= _largeur - x:
            ligne_actuelle += mot + " "
        else:
            _fenetre.blit(police.render(ligne_actuelle.strip(), True, couleur), (x, y + y_offset))
            ligne_actuelle = mot + " "
            y_offset += police.get_height()
    if ligne_actuelle:
        _fenetre.blit(police.render(ligne_actuelle.strip(), True, couleur), (x, y + y_offset))


def input_text(x, y, largeur, hauteur, couleur_fond, couleur_texte, police=None, couleur_tour=None, arrondi=0, epaisseur_tour=2, longueur_max=None):
    """
    Gere la saisie de texte par l'utilisateur dans une zone de texte, jusqu'a
    ce qu'il appuie sur "Entree".

    Parametres :
    -----------
        x, y (int) : la position de la zone de texte.
        largeur, hauteur (int) : la taille de la zone de texte.
        couleur_fond, couleur_texte (tuple) : les couleurs (R, G, B).
        police (Font) : (facultatif) la police du texte saisi, creee par exemple
                         avec pygame.font.SysFont("arial", 24).
                         Sans elle, une police par defaut est utilisee.
        couleur_tour (tuple) : (facultatif) la couleur du contour de la zone de
                                texte, sous forme (R, G, B). Sans elle, pas de contour.
        arrondi (int) : (facultatif) le rayon des coins en pixels.
                         Avec 0 (par defaut), les coins sont droits.
        epaisseur_tour (int) : (facultatif) l'epaisseur du contour en pixels
                                (2 par defaut), si couleur_tour est precisee.
        longueur_max (int) : (facultatif) le nombre maximum de caracteres que
                              l'utilisateur peut taper. Sans limite par defaut.

    Retourne :
    -------
        texte (str) : le texte saisi par l'utilisateur.
    """
    if police is None:
        police = _font_texte
    actif = True
    texte = ""
    while actif:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    actif = False
                    return texte
                elif event.key == pygame.K_BACKSPACE:
                    texte = texte[:-1]
                elif longueur_max is None or len(texte) < longueur_max:
                    texte += event.unicode

        pygame.draw.rect(_fenetre, couleur_fond, (x, y, largeur, hauteur), border_radius=arrondi)
        if couleur_tour is not None:
            pygame.draw.rect(_fenetre, couleur_tour, (x, y, largeur, hauteur), width=epaisseur_tour, border_radius=arrondi)
        _fenetre.blit(police.render(texte, True, couleur_texte), (x + 10, y + (hauteur - police.get_height()) // 2))
        pygame.display.flip()



def dessiner_bouton(texte, x, y, largeur, hauteur, couleur1, couleur2,
                    couleurtexte, police=None, couleur_tour=None,
                    arrondi=0, epaisseur_tour=2):

    if police is None:
        police = _font_texte

    largeur_texte, hauteur_texte = police.size(texte)
    largeur_bouton = max(largeur, largeur_texte + 20)
    hauteur_bouton = max(hauteur, hauteur_texte + 10)

    souris = pygame.mouse.get_pos()
    survol = (
        x <= souris[0] <= x + largeur_bouton
        and y <= souris[1] <= y + hauteur_bouton
    )

    # Détecte uniquement un nouveau clic, pas le maintien du bouton.
    clique = False
    for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
        if event.button == 1 and survol:
            clique = True

    couleur = couleur2 if survol else couleur1

    pygame.draw.rect(
        _fenetre, couleur,
        (x, y, largeur_bouton, hauteur_bouton),
        border_radius=arrondi
    )

    if couleur_tour is not None:
        pygame.draw.rect(
            _fenetre, couleur_tour,
            (x, y, largeur_bouton, hauteur_bouton),
            width=epaisseur_tour,
            border_radius=arrondi
        )

    texte_surface = police.render(texte, True, couleurtexte)
    texte_rect = texte_surface.get_rect(
        center=(
            x + largeur_bouton // 2,
            y + hauteur_bouton // 2
        )
    )
    _fenetre.blit(texte_surface, texte_rect)

    return clique

def zone_cliquable(image, x, y):
    """
    Affiche une image et renvoie True le temps ou l'utilisateur clique dessus
    (sinon False). Meme principe que dessiner_bouton, mais avec une image a
    la place d'un rectangle de couleur + texte :

        if zone_cliquable(image_torche, 620, 380):
            torche_recuperee = True

    Parametres :
    -----------
        image (Surface) : l'image a afficher (chargee avec pygame.image.load).
        x, y (int) : la position d'affichage.

    Retourne :
    -------
        clique (bool) : True si l'utilisateur vient de cliquer sur l'image.
    """
    largeur, hauteur = image.get_size()
    souris = pygame.mouse.get_pos()
    clic = pygame.mouse.get_pressed()

    _fenetre.blit(image, (x, y))

    if x + largeur > souris[0] > x and y + hauteur > souris[1] > y:
        if clic[0] == 1:
            time.sleep(0.2)
            return True
    return False


def zone_invisible(x, y, largeur, hauteur):
    """
    Cree une zone rectangulaire invisible sur l'ecran et renvoie True le temps
    ou l'utilisateur clique dedans (sinon False). Elle ne dessine rien : elle
    sert a rendre cliquable un element du decor (une porte, une affiche, un
    meuble...) :

        if zone_invisible(520, 60, 180, 130):
            texte_dialogue = "Une affiche du concours de code."

    Parametres :
    -----------
        x, y (int) : la position du coin en haut a gauche de la zone.
        largeur, hauteur (int) : la taille de la zone en pixels.

    Retourne :
    -------
        clique (bool) : True si l'utilisateur vient de cliquer dans la zone.
    """
    souris = pygame.mouse.get_pos()
    clic = pygame.mouse.get_pressed()

    if x + largeur > souris[0] > x and y + hauteur > souris[1] > y:
        if clic[0] == 1:
            time.sleep(0.2)
            return True
    return False


def charger_sprites_parlant(prefixe, nb_frames):
    """
    Charge une serie d'images numerotees prefixe_0.png, prefixe_1.png, ...
    pour faire "parler" un personnage en alternant les frames.

    Parametres :
    -----------
        prefixe (str) : le debut du nom de fichier commun a toutes les frames.
        nb_frames (int) : le nombre d'images a charger.

    Retourne :
    -------
        frames (list) : la liste des images chargees, a passer telle quelle
                         a afficher_personnage_parlant.
    """
    frames = []
    for i in range(nb_frames):
        frames.append(pygame.image.load(f"{prefixe}_{i}.png"))
    return frames


def afficher_personnage_parlant(frames, x, y, temps_ecoule, vitesse_ms=350, taille=None):
    """
    Affiche un personnage en alternant automatiquement entre ses frames au
    fil du temps, pour donner l'impression qu'il parle.

    Parametres :
    -----------
        frames (list) : la liste d'images renvoyee par charger_sprites_parlant.
        x, y (int) : la position d'affichage.
        temps_ecoule (int) : pygame.time.get_ticks(), le temps ecoule depuis
                              le lancement du jeu, en millisecondes.
        vitesse_ms (int) : (facultatif) le temps entre deux changements de frame.
        taille (tuple) : (facultatif) la taille du personnage a l'ecran, sous
                          forme (largeur, hauteur) en pixels. Sans elle, le
                          personnage garde la taille de ses images.
    """
    index = (temps_ecoule // vitesse_ms) % len(frames)
    image = frames[index]
    if taille is not None:
        clef = (id(image), taille)
        if clef not in _images_redimensionnees:
            _images_redimensionnees[clef] = pygame.transform.scale(image, taille)
        image = _images_redimensionnees[clef]
    _fenetre.blit(image, (x, y))


def dessiner_boite_dialogue(nom, texte, x, y, largeur, hauteur, couleur_tour=None, couleur_fond=None, police=None, vitesse=40, couleur_texte=None):
    """
    Dessine une boite de dialogue avec le nom du personnage et son texte, en
    revenant a la ligne automatiquement si le texte est trop long.
    Le texte s'ecrit lettre apres lettre, comme si le personnage parlait : il
    recommence a s'ecrire des que le texte (ou le nom) change. Appelez cette
    fonction a chaque tour de la boucle du jeu.

    Parametres :
    -----------
        nom (str) : le nom du personnage qui parle.
        texte (str) : le texte a afficher.
        x, y, largeur, hauteur (int) : la position et la taille de la boite.
        couleur_tour (tuple) : (facultatif) la couleur du contour de la boite et
                                du nom, sous forme (R, G, B).
        couleur_fond (tuple) : (facultatif) la couleur de fond de la boite, sous
                                forme (R, G, B).
        police (Font) : (facultatif) la police du nom et du texte, creee par
                         exemple avec pygame.font.SysFont("arial", 24) ou
                         pygame.font.Font("ma_police.ttf", 24).
        vitesse (int) : (facultatif) le nombre de lettres affichees par seconde.
                         Avec 0, tout le texte apparait d'un seul coup.
        couleur_texte (tuple) : (facultatif) la couleur du texte, sous forme
                                 (R, G, B).
                         Si on ne precise pas ces cinq derniers parametres, des
                         valeurs par defaut sont utilisees.

    Retourne :
    -------
        termine (bool) : True si tout le texte est affiche, False s'il est
                          encore en train de s'ecrire.
    """
    global _dialogue_en_cours, _dialogue_debut
    if _dialogue_en_cours != (nom, texte):
        _dialogue_en_cours = (nom, texte)
        _dialogue_debut = pygame.time.get_ticks()
    if vitesse > 0:
        nb_lettres = int((pygame.time.get_ticks() - _dialogue_debut) * vitesse / 1000)
    else:
        nb_lettres = len(texte)

    if couleur_tour is None:
        couleur_tour = ACCENT
    if couleur_fond is None:
        couleur_fond = FOND_BOITE
    if couleur_texte is None:
        couleur_texte = COULEUR_TEXTE

    if police is None:
        police_nom = _font_nom
        police_texte = _font_texte
        debut_texte = 46
        interligne = 26
    else:
        police_nom = police
        police_texte = police
        debut_texte = 14 + police.get_height() + 12
        interligne = police.get_height() + 4

    boite = pygame.Surface((largeur, hauteur), pygame.SRCALPHA)
    pygame.draw.rect(boite, (*couleur_fond, 225), (0, 0, largeur, hauteur), border_radius=16)
    pygame.draw.rect(boite, couleur_tour, (0, 0, largeur, hauteur), width=2, border_radius=16)
    _fenetre.blit(boite, (x, y))

    _fenetre.blit(police_nom.render(nom, True, couleur_tour), (x + 24, y + 14))

    lignes = []
    ligne_actuelle = ""
    for mot in texte.split(" "):
        if police_texte.size(ligne_actuelle + mot)[0] <= largeur - 48:
            ligne_actuelle += mot + " "
        else:
            lignes.append(ligne_actuelle.strip())
            ligne_actuelle = mot + " "
    if ligne_actuelle:
        lignes.append(ligne_actuelle.strip())

    restantes = nb_lettres
    y_ligne = y + debut_texte
    for ligne in lignes:
        if restantes <= 0:
            break
        _fenetre.blit(police_texte.render(ligne[:restantes], True, couleur_texte), (x + 24, y_ligne))
        restantes -= len(ligne) + 1
        y_ligne += interligne

    return nb_lettres >= len(texte)
