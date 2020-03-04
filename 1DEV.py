import pygame
import traceback
from pygame.locals import *
from math import *
import time
import random
from copy import deepcopy

pygame.init()
      
#generation des niveaux aleatoirement avec des probas différentes
def GenerateLevel():
      list=["niveaux/niveau1.txt", "niveaux/niveau2.txt", "niveaux/niveau3.txt", "niveaux/niveau4.txt", "niveaux/niveau5.txt", "niveaux/niveau6.txt", "niveaux/niveau7.txt", "niveaux/niveau8.txt", "niveaux/niveau9.txt", "niveaux/niveau10.txt"]

      #Listes probabilités des types de blocs

      elements_level_1= ['1','2','3', '3', '3', '3', '3', '3', '3', '4', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5','3', '3', '3', '3', '3', '3', '3', '4', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5']

      elements_level_2= ['1', '1', '2', '2', '3', '3', '3', '3', '3', '3', '3', '4', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5', '6', '6', '6', '6']

      elements_level_3= ['1', '4', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5']

      elements_level_4= ['1', '1', '2', '2', '2', '2', '5', '5', '5', '5', '5','5', '5', '5', '5', '5', '6', '6', '6', '6', '6', '6', '6', '6', '7', '7', '8', '8']

      elements_level_5= ['1', '2', '3', '3', '3', '3', '3', '3', '3', '4', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7','7', '7', '8', '8', '8', '8']

      elements_level_6= ['2', '2', '3', '3', '3', '3', '3', '3', '3','3', '4', '4', '4', '4', '4', '4','4','4','4', '5', '5', '5', '5', '5','5','5','5', '6', '6', '6', '6', '6', '6', '6', '6']

      elements_level_7= ['1', '7', '7', '7', '7', '7','7','7','7','7','8','8','8','8','8','8','8','8','8']

      elements_level_8= ['1', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '3', '3', '3', '6', '6', '6', '6', '6', '6', '6', '7', '7', '8', '8']

      elements_level_9= ['1', '2', '2', '2', '2', '7', '7', '7', '7', '7', '7', '7', '7', '7', '8', '8', '8', '8', '8', '8', '8', '8' ,'8', '7', '7', '8', '8']

      elements_level_10= ['2', '2', '3', '3', '3', '3', '3', '3', '3', '4', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '8', '8']

      for j in range(0,10):
            level = open(list[j], "w")
            level.write("00000000\n")
            level.write("00000000\n")
            level.write("00000000\n")
            level.write("00000000\n")
            for i in range(100):
                  for y in range(7):
                        if j ==0:
                              level.write(random.choice(elements_level_1))
                        elif j ==1:
                              level.write(random.choice(elements_level_2))
                        elif j ==2:
                              level.write(random.choice(elements_level_3))
                        elif j ==3:
                              level.write(random.choice(elements_level_4))
                        elif j ==4:
                              level.write(random.choice(elements_level_5))
                        elif j ==5:
                              level.write(random.choice(elements_level_6))
                        elif j ==6:
                              level.write(random.choice(elements_level_7))
                        elif j ==7:
                              level.write(random.choice(elements_level_8))
                        elif j ==8:
                              level.write(random.choice(elements_level_9))
                        elif j == 9:
                              level.write(random.choice(elements_level_10))
                  level.write("0")
                  level.write("\n")
            level.write("00000000\n")
            level.write("00000000\n")
            level.write("00000000\n")
            level.write("00000000\n")
            level.write("00000000\n")
            level.write("00000000\n")
            level.write("00000000\n")
            level.write("00000000\n")
            
#fonction qui permet d'entrer et d'afficher un pseudo
def Inputer(monInput,maj,continuer,saisieDuPseudo,reinitialiser,score):

      for event in pygame.event.get():
            if event.type == QUIT:
                  continuer = 0
                  pygame.quit()
            if event.type == KEYUP:
                  if event.key == K_ESCAPE:
                        continuer = 0
                        
                  #suppression de caractere
                  elif event.key == K_BACKSPACE:
                        monInput = monInput[0:-1]

                  #majuscules
                  elif event.key == K_RSHIFT or event.key == K_LSHIFT:
                        if maj == 0:
                              maj = 1
                        elif maj == 1:
                              maj = 0

                  #sortir de la boucle d'entree du pseudo 
                  elif event.key == K_RETURN:
                        NewScore(score, monInput)
                        saisieDuPseudo = False
                        reinitialiser = True

                  if len(monInput) <= 20: #taille max du pseudo
                        
                        if event.key == K_q:
                              if maj == 1:      
                                    monInput += 'A'
                              else : monInput += 'a'

                        elif event.key == K_b:
                              if maj == 1:      
                                    monInput += 'B'
                              else : monInput += 'b'

                        elif event.key == K_c:
                              if maj == 1:      
                                    monInput += 'C'
                              else : monInput += 'c'

                        elif event.key == K_d:
                              if maj == 1:      
                                    monInput += 'D'
                              else : monInput += 'd'

                        elif event.key == K_e:
                              if maj == 1:      
                                    monInput += 'E'
                              else : monInput += 'e'

                        elif event.key == K_f:
                              if maj == 1:      
                                    monInput += 'F'
                              else : monInput += 'f'

                        elif event.key == K_g:
                              if maj == 1:      
                                    monInput += 'G'
                              else : monInput += 'g'

                        elif event.key == K_h:
                              if maj == 1:      
                                    monInput += 'H'
                              else : monInput += 'h'

                        elif event.key == K_i:
                              if maj == 1:      
                                    monInput += 'I'
                              else : monInput += 'i'

                        elif event.key == K_j:
                              if maj == 1:      
                                    monInput += 'J'
                              else : monInput += 'j'

                        elif event.key == K_k:
                              if maj == 1:      
                                    monInput += 'K'
                              else : monInput += 'k'

                        elif event.key == K_l:
                              if maj == 1:      
                                    monInput += 'L'
                              else : monInput += 'l'

                        elif event.key == K_SEMICOLON:
                              if maj == 1:      
                                    monInput += 'M'
                              else : monInput += 'm'

                        elif event.key == K_n:
                              if maj == 1:      
                                    monInput += 'N'
                              else : monInput += 'n'

                        elif event.key == K_o:
                              if maj == 1:      
                                    monInput += 'O'
                              else : monInput += 'o'

                        elif event.key == K_p:
                              if maj == 1:      
                                    monInput += 'P'
                              else : monInput += 'p'

                        elif event.key == K_a:
                              if maj == 1:      
                                    monInput += 'Q'
                              else : monInput += 'q'

                        elif event.key == K_r:
                              if maj == 1:      
                                    monInput += 'R'
                              else : monInput += 'r'

                        elif event.key == K_s:
                              if maj == 1:      
                                    monInput += 'S'
                              else : monInput += 's'

                        elif event.key == K_t:
                              if maj == 1:      
                                    monInput += 'T'
                              else : monInput += 't'

                        elif event.key == K_u:
                              if maj == 1:      
                                    monInput += 'U'
                              else : monInput += 'u'

                        elif event.key == K_v:
                              if maj == 1:      
                                    monInput += 'V'
                              else : monInput += 'v'

                        elif event.key == K_z:
                              if maj == 1:      
                                    monInput += 'W'
                              else : monInput += 'w'

                        elif event.key == K_x:
                              if maj == 1:      
                                    monInput += 'X'
                              else : monInput += 'x'

                        elif event.key == K_y:
                              if maj == 1:      
                                    monInput += 'Y'
                              else : monInput += 'y'

                        elif event.key == K_w:
                              if maj == 1:      
                                    monInput += 'Z'
                              else : monInput += 'z'

      monInputGraph = font2.render(("Votre nom est :  " + monInput),1,(255,255,255))
      disp_score = font2.render(("Score :  " + str(score)),1,(255,255,255))
      fenetre.blit(monInputGraph,(480,500))
      fenetre.blit(disp_score,(500, 350))
      return monInput,maj,continuer,saisieDuPseudo, reinitialiser

#fonction de lecture des fichiers textes
def lecture(niveau):
    with open(niveau, "r") as fichier:
        structure_niveau = []
        #On parcourt les lignes du fichier
        for ligne in fichier:
            ligne_niveau = []
            #On parcourt les sprites (caracteres) contenus dans le fichier
            for sprite in ligne:
                #On ignore les "\n" de fin de ligne
                if sprite != '\n':
                    #On ajoute le sprite à la liste de la ligne
                    ligne_niveau.append(int(sprite))
            #On ajoute la ligne à la liste du niveau
            structure_niveau.append(ligne_niveau)
        return(structure_niveau)

#affichage des blocs selon la liste creee
def affichage(structure_niveau):
      for y in range(len(structure_niveau)):
            if niveau == "niveaux/niveau1.txt" and level == 0:
                  fenetre.blit(terre,(0,y*100+hauteur+400))
            else:
                  fenetre.blit(terre,(0,y*100+hauteur-400))
      for y in range(len(structure_niveau)):
            for x in range(len(structure_niveau[0])):
                  if structure_niveau[y][x]==00:
                        deplacement=True
                  elif structure_niveau[y][x]==1:
                        fenetre.blit(oxygene,(x*100,y*100+hauteur))
                  elif structure_niveau[y][x]==2:
                        fenetre.blit(tnt,(x*100,y*100+hauteur))
                  elif structure_niveau[y][x]==3:
                        fenetre.blit(rouge,(x*100,y*100+hauteur))
                  elif structure_niveau[y][x]==4:
                        fenetre.blit(bleu,(x*100,y*100+hauteur))
                  elif structure_niveau[y][x]==5:
                        fenetre.blit(vert,(x*100,y*100+hauteur))
                  elif structure_niveau[y][x]==6:
                        fenetre.blit(jaune,(x*100,y*100+hauteur))
                  elif structure_niveau[y][x]==7:
                        fenetre.blit(blanche,(x*100,y*100+hauteur))
                  elif structure_niveau[y][x]==8:
                        fenetre.blit(brune,(x*100,y*100+hauteur))
                  elif structure_niveau[y][x]==9:
                        fenetre.blit(tnt1,(x*100,y*100+hauteur))
                  elif structure_niveau[y][x]==10:
                        fenetre.blit(tnt2,(x*100,y*100+hauteur))
                  elif structure_niveau[y][x]==11:
                        fenetre.blit(tnt3,(x*100,y*100+hauteur))
                  elif structure_niveau[y][x]==12:
                        fenetre.blit(tnt4,(x*100,y*100+hauteur))
 
#recuperation de la position du personnage dans notre "niveau" (coordonnees dans liste "niveau")
def collision(structure_niveau, persoX, persoY, hauteur):
    Droite = persoX + 83
    Gauche = persoX + 17
    Haut = hauteur - 500 + 66
    Bas = hauteur - 500 + 99
    
    CasePersoX = (persoX+50)//100
    CasePersoY = -((hauteur - 400) //100) + -1
    PersoDroite = Droite//100
    PersoGauche = Gauche//100
    PersoHaut = -(Haut//100) - 1
    PersoBas = -(Bas//100) - 1

    return CasePersoX, CasePersoY, PersoDroite, PersoGauche, PersoHaut, PersoBas

#gestion du temps
def theTimer(start,temps,saveTemps,secondes,minutes,timer):
    now = time.time()
    temps = int(now-start)
    
    if temps!=saveTemps:
          secondes += 1
          if secondes == 60:
                secondes=0
                minutes += 1
          timer = font.render(("Timer     " + str(minutes) + "min " + str(secondes) + "sec"),1,(255,255,255))
    saveTemps = temps
    return temps,saveTemps,secondes,minutes,timer

#destruction de tout les blocs d'une même couleur cote a cote
def detruireAutour(structure_niveau,monBlocX,monBlocY,couleur,score):
      if couleur != 0 and couleur !=1 and couleur !=2 :
        
            if structure_niveau[monBlocY-1][monBlocX] == couleur and monBlocY-1 != -1:
                  structure_niveau[monBlocY-1][monBlocX] = 0
                  score += 10
                  structure_niveau, score = detruireAutour(structure_niveau,monBlocX,monBlocY-1,couleur,score)
            if structure_niveau[monBlocY+1][monBlocX] == couleur and monBlocY+1 != 105:
                  structure_niveau[monBlocY+1][monBlocX] = 0
                  score += 10
                  structure_niveau, score = detruireAutour(structure_niveau,monBlocX,monBlocY+1,couleur,score)
            if structure_niveau[monBlocY][monBlocX+1] == couleur and monBlocX+1 != 7:
                  structure_niveau[monBlocY][monBlocX+1] = 0
                  score += 10
                  structure_niveau, score = detruireAutour(structure_niveau,monBlocX+1,monBlocY,couleur,score)
            if structure_niveau[monBlocY][monBlocX-1] == couleur and monBlocX-1 != -1:
                  structure_niveau[monBlocY][monBlocX-1] = 0
                  score += 10
                  structure_niveau, score = detruireAutour(structure_niveau,monBlocX-1,monBlocY,couleur,score)
      return structure_niveau, score

#detection du nombre de blocs fusionnes
def detecterAutour(structure_niveau,monBlocX,monBlocY,couleur,nbrBlocs):
      if couleur != 0 and couleur !=1 and couleur !=2 :

            if structure_niveau[monBlocY-1][monBlocX] == couleur and monBlocY-1 != -1:
                  structure_niveau[monBlocY-1][monBlocX] = 0
                  nbrBlocs += 1
                  nbrBlocs = detecterAutour(structure_niveau,monBlocX,monBlocY-1,couleur,nbrBlocs)
            if structure_niveau[monBlocY+1][monBlocX] == couleur and monBlocY+1 != 105:
                  structure_niveau[monBlocY+1][monBlocX] = 0
                  nbrBlocs += 1
                  nbrBlocs = detecterAutour(structure_niveau,monBlocX,monBlocY+1,couleur,nbrBlocs)
            if structure_niveau[monBlocY][monBlocX+1] == couleur and monBlocX+1 != 7:
                  structure_niveau[monBlocY][monBlocX+1] = 0
                  nbrBlocs += 1
                  nbrBlocs = detecterAutour(structure_niveau,monBlocX+1,monBlocY,couleur,nbrBlocs)
            if structure_niveau[monBlocY][monBlocX-1] == couleur and monBlocX-1 != -1:
                  structure_niveau[monBlocY][monBlocX-1] = 0
                  nbrBlocs += 1
                  nbrBlocs = detecterAutour(structure_niveau,monBlocX-1,monBlocY,couleur,nbrBlocs)
                  
      return nbrBlocs

#systeme de vies
def lesVies(coeurRouge,coeurGris,nbrVie, font, musique, game, fin):
    if nbrVie == 3:
        fenetre.blit(coeurRouge,(800,270))
        fenetre.blit(coeurRouge,(850,270))
        fenetre.blit(coeurRouge,(900,270))
    elif nbrVie == 2:
        fenetre.blit(coeurRouge,(800,270))
        fenetre.blit(coeurRouge,(850,270))
        fenetre.blit(coeurGris,(900,270))
    elif nbrVie == 1:
        fenetre.blit(coeurRouge,(800,270))
        fenetre.blit(coeurGris,(850,270))
        fenetre.blit(coeurGris,(900,270))
    elif nbrVie == 0:
        barreVie = font.render("0%",1,(0,0,0))
        pygame.draw.circle(fenetre, (114,103,103), (875,450), 85)
        pygame.draw.circle(fenetre, (0,0,0), (875,450), 85, 5)
        pygame.draw.circle(fenetre, (143,22,22), (875,450), 0)
        fenetre.blit(barreVie,(860,445))
        fenetre.blit(coeurGris,(800,270))
        fenetre.blit(coeurGris,(850,270))
        fenetre.blit(coeurGris,(900,270))
        pygame.display.flip()
        roblox.play()
        pygame.time.delay(500)
        pygame.mixer.music.stop()
        musique = False
        game = False
        fin = True

    return musique, game, fin

#fonction d'affichage des éléments du hud 
def affichageBarreDeVie(barreVie, nbrVie, vie, saveSecondes, secondes, horloge, timer):
    if vie > 100:
        vie = 100
    if saveSecondes != secondes:
        saveSecondes = secondes
        vie-=1
        
    barreVie = font.render((str(vie) + "%"),1,(0,0,0))
    afficherProfondeur = font.render(("Profondeur :  "+str(CasePersoY-3+103*level)),1,(255,255,255))
    afficherScore = font.render(("Score :  "+str(score)),1,(255,255,255))
    fenetre.blit(journal,(750,500))
    fenetre.blit(timer,(800,100))
    fenetre.blit(horloge[secondes],(1000,50))
    fenetre.blit(cadre,(950,0))
    fenetre.blit(afficherProfondeur, (800,200))
    fenetre.blit(afficherScore, (800,150))
    
    if vie >=0:
        pygame.draw.circle(fenetre, (114,103,103), (875,450), 85)
        pygame.draw.circle(fenetre, (0,0,0), (875,450), 85, 5)
        pygame.draw.circle(fenetre, (143,22,22), (875,450), (round(vie*0.8)))
        fenetre.blit(barreVie,(860,445))
    else:
        nbrVie -= 1
        sonMort.play()
        vie = 100

    return barreVie, nbrVie, vie, saveSecondes

#ajoute le nouveau score au fichier score.txt
def NewScore(score, pseudo): 
    scoretxt = open("score.txt", "a")
    scoretxt.write(";")
    scoretxt.write(str(pseudo))
    scoretxt.write(";")
    scoretxt.write(str(score))

#on recupere les scores sous forme de dictionnaire
def Scorelist():
    scoretxt = open("score.txt", "r")
    liste = scoretxt.readline().split(";")
    dic = {}
    for i in range(0, len(liste), 2):
        dic[liste[i]] = int(liste[i+1])
    dic = sorted(dic.items(), reverse=True, key=lambda t: t[1])
    return dic

#fonction des meilleurs scores
def AfficherScore(dic):
    font_score = pygame.font.Font(None, 40)
    j1 = font_score.render(("1 . " + str(dic[0][0]) + " : " + str(dic[0][1])), 1, (0, 0, 0))
    j2 = font_score.render(("2 . " + str(dic[1][0]) + " : " + str(dic[1][1])), 1, (0, 0, 0))
    j3 = font_score.render(("3 . " + str(dic[2][0]) + " : " + str(dic[2][1])), 1, (0, 0, 0))
    j4 = font_score.render(("4 . " + str(dic[3][0]) + " : " + str(dic[3][1])), 1, (0, 0, 0))
    j5 = font_score.render(("5 . " + str(dic[4][0]) + " : " + str(dic[4][1])), 1, (0, 0, 0))
    j6 = font_score.render(("6 . " + str(dic[5][0]) + " : " + str(dic[5][1])), 1, (0, 0, 0))
    j7 = font_score.render(("7 . " + str(dic[6][0]) + " : " + str(dic[6][1])), 1, (0, 0, 0))
    j8 = font_score.render(("8 . " + str(dic[7][0]) + " : " + str(dic[7][1])), 1, (0, 0, 0))
    j9 = font_score.render(("9 . " + str(dic[8][0]) + " : " + str(dic[8][1])), 1, (0, 0, 0))
    j10 = font_score.render(("10 . " + str(dic[9][0]) + " : " + str(dic[9][1])), 1, (0, 0, 0))
    fenetre.blit(j1, (250, 220))
    fenetre.blit(j2, (250, 270))
    fenetre.blit(j3, (250, 320))
    fenetre.blit(j4, (250, 370))
    fenetre.blit(j5, (250, 420))
    fenetre.blit(j6, (250, 470))
    fenetre.blit(j7, (250, 520))
    fenetre.blit(j8, (250, 570))
    fenetre.blit(j9, (250, 620))
    fenetre.blit(j10, (235, 670))

  
try:
      #paramètres de la fenetre
      fenetre = pygame.display.set_mode((1200,800))
      pygame.display.set_caption("Mr.Driller")
      pygame.time.Clock().tick(60)
      pygame.key.set_repeat(1,15)
      font=pygame.font.Font(None, 24)
      font2=pygame.font.Font(None, 50)


      #images du perso
      droite = []
      gauche = []

      for i in range(3):
            droite.append(pygame.image.load("perso/droite1.png").convert_alpha())
      for i in range(3):
            droite.append(pygame.image.load("perso/droite2.png").convert_alpha())
      for i in range(3):
            droite.append(pygame.image.load("perso/droite3.png").convert_alpha())
      for i in range(3):
            droite.append(pygame.image.load("perso/droite4.png").convert_alpha())
      for i in range(3):
            gauche.append(pygame.image.load("perso/gauche1.png").convert_alpha())
      for i in range(3):
            gauche.append(pygame.image.load("perso/gauche2.png").convert_alpha())
      for i in range(3):
            gauche.append(pygame.image.load("perso/gauche3.png").convert_alpha())
      for i in range(3):
            gauche.append(pygame.image.load("perso/gauche4.png").convert_alpha())

      basDroite = pygame.image.load("perso/basDroite.png").convert_alpha()
      basGauche = pygame.image.load("perso/basGauche.png").convert_alpha()
      haut = pygame.image.load("perso/haut.png").convert_alpha()

      #blocs
      oxygene = pygame.image.load("blocs/oxygene.png").convert_alpha()
      bleu = pygame.image.load("blocs/blocBleu.png").convert_alpha()
      rouge = pygame.image.load("blocs/blocRouge.png").convert_alpha()
      vert = pygame.image.load("blocs/blocVert.png").convert_alpha()
      jaune = pygame.image.load("blocs/blocJaune.png").convert_alpha()
      brune = pygame.image.load("blocs/caisseBrune.png").convert_alpha()
      blanche = pygame.image.load("blocs/caisseBlanche.png").convert_alpha()
      tnt = pygame.image.load("blocs/tnt.png").convert_alpha()
      tnt1 = pygame.image.load("blocs/tnt1.png").convert_alpha()
      tnt2 = pygame.image.load("blocs/tnt2.png").convert_alpha()
      tnt3 = pygame.image.load("blocs/tnt3.png").convert_alpha()
      tnt4 = pygame.image.load("blocs/tnt4.png").convert_alpha()
      terre = pygame.image.load("blocs/terre.png").convert_alpha()

      #menu, pause et fin
      how = pygame.image.load("menu/how.png").convert_alpha()
      defaite = pygame.image.load("menu/defaite.png").convert_alpha()
      victory = pygame.image.load("menu/win.png").convert_alpha()
      imagePause = pygame.image.load("menu/pause.png").convert_alpha()
      fondPause = pygame.image.load("menu/fondPause.png").convert_alpha()
      topscore = pygame.image.load("menu/top-score.png")
      fondBois = pygame.image.load("menu/fondbois.jpg")
      fond_menu = pygame.image.load("menu/fond_menu.jpg")
      bouton_play = pygame.image.load("menu/bouton_play.png")
      bouton_play_clic = pygame.image.load("menu/bouton_play_clic.png")
      bouton_how = pygame.image.load("menu/bouton_how.png")
      bouton_how_clic = pygame.image.load("menu/bouton_how_clic.png")
      bouton_score = pygame.image.load("menu/bouton_score.png")
      bouton_score_clic = pygame.image.load("menu/bouton_score_clic.png")
      journal = pygame.image.load("hud/journal.png")

      #images des coeurs
      coeurGris = pygame.image.load("hud/coeurGris.png").convert_alpha()
      coeurRouge = pygame.image.load("hud/coeurRouge.png").convert_alpha()

      #images du timer
      horloge = []
      horloge.append(pygame.image.load("horloge/1.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/2.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/3.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/4.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/5.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/6.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/7.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/8.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/9.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/10.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/11.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/12.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/13.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/14.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/15.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/16.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/17.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/18.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/19.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/20.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/21.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/22.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/23.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/24.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/25.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/26.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/27.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/28.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/29.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/30.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/31.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/32.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/33.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/34.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/35.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/36.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/37.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/38.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/39.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/40.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/41.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/42.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/43.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/44.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/45.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/46.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/47.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/48.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/49.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/50.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/51.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/52.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/53.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/54.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/55.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/56.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/57.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/58.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/59.png").convert_alpha())
      horloge.append(pygame.image.load("horloge/60.png").convert_alpha())

      cadre = pygame.image.load("hud/cadre.png")

      #musique et sons
      pygame.mixer.music.set_volume(0.1)
      roblox = pygame.mixer.Sound("sons/roblox.wav")
      sonBloc = pygame.mixer.Sound("sons/sonBloc.wav")
      sonMort = pygame.mixer.Sound("sons/classic_hurt.wav")

      reinitialiser = True
      #variable de la boucle de jeu
      continuer = 1

      #depart de la boucle de jeu
      while continuer:

            #boucle d'initialisation/reinitialisation
            if reinitialiser:
                  for event in pygame.event.get():
                        if event.type == QUIT:
                              continuer = 0
                          
                        if event.type == KEYUP:
                              if event.key == K_ESCAPE:
                                    continuer = 0

                  #variables du niveau
                  level = 0
                  GenerateLevel()
                  niveau = "niveaux/niveau1.txt"
                              
                  #variables du personnage
                  persoX = 300
                  persoY = 400
                  direction = 1
                  bas = 1
                  hauteur = 400
                  tombe = True
                  D=0
                  G=0

                  score = -61


                  #variables barre de vie
                  vie = 100
                  barreVie = font.render((str(vie) + "%"),1,(200,0,0))
                  nbrVie = 3

                  #variables du timer
                  start = time.time()
                  temps = 0
                  saveTemps = -1
                  secondes = 0
                  saveSecondes = 0
                  minutes = 0
                  saveTempsCubes = 0
                  timer = font.render(("Timer     " + str(minutes) + "min " + str(secondes) + "sec"),1,(255,255,255))

                  #on appelle une première fois les fonctions pour initialiser les variables
                  structure_niveau = lecture(niveau)
                  CasePersoX, CasePersoY, PersoDroite, PersoGauche, PersoHaut, PersoBas = collision(structure_niveau, persoX, persoY, hauteur)

                  #variables de saisie
                  monInput = ''
                  maj = 0
                  entrerPseudo = True

                  musique = False

                  howTo = 0
                  fenetreScore = 0

                  #variables des differentes boucles
                  menu = False
                  game = False
                  fin = False
                  pause = False
                  saisieDuPseudo = False
                  victoire = False
                  reinitialiser = False
                  menu = True

                  fondBlit = 0

                  dic = Scorelist()

                  

            elif menu:

                  #lancement de la musique du menu
                  if not musique:
                        pygame.mixer.music.load("sons/menu.mp3")
                        pygame.mixer.music.play()
                        musique = True

                  fenetre.blit(fond_menu, (0, 0))
                  x, y = pygame.mouse.get_pos()

                  #bouton "jouer"
                  if 80 < x < 341 and 200 < y < 300 and howTo == 0 and fenetreScore == 0:
                        fenetre.blit(bouton_play_clic, (80, 200))
                  else:
                        fenetre.blit(bouton_play, (80, 200))

                  #bouton "comment jouer"
                  if 80 < x < 554 and 350 < y < 450:
                        fenetre.blit(bouton_how_clic, (80, 350))
                  else:
                        fenetre.blit(bouton_how, (80, 350))
                      
                  # bouton scores
                  if 80 < x < 680 and 530 < y < 620:
                        fenetre.blit(bouton_score_clic, (80, 530))
                  else:
                        fenetre.blit(bouton_score, (80, 530))

                  if howTo == 1 and fenetreScore == 0:
                        fenetre.blit(how,(0,0))

                  if fenetreScore == 1 and howTo == 0:
                        fenetre.blit(topscore,(0,0))
                        AfficherScore(dic)

                  for event in pygame.event.get():

                        if event.type == QUIT:
                              continuer = 0
                              pygame.quit()

                        if event.type == KEYUP:

                              if event.key == K_ESCAPE:
                                    continuer = 0

                        if event.type == MOUSEBUTTONDOWN:
                              x, y = pygame.mouse.get_pos()
                              if 80<x<341 and 200<y<300:
                                    menu = False
                                    game = True
                                    musique = False
                                    pygame.mixer.music.stop()
                              elif 80<x<554 and 350<y<450:
                                    howTo = 1
                              elif howTo == 1 and 1041<x<1111 and 75<y<143:
                                    howTo = 0
                              elif 80 < x < 700 and 530 < y < 610:
                                    fenetreScore = 1
                              elif fenetreScore == 1 and 1041 < x < 1111 and 75 < y < 143:
                                    fenetreScore = 0

                  pygame.display.flip()

            #boucle de jeu
            elif game:

                  #lancement de la musique du jeu
                  if not musique:
                        pygame.mixer.music.load("sons/jeu.mp3")
                        pygame.mixer.music.play()
                        musique = True
                  
                  #gestion des evenements : touches du clavier/souris/croix
                  for event in pygame.event.get():

                        if event.type == QUIT:
                              continuer = 0
                          
                        if event.type == KEYUP:
                          
                              if event.key == K_ESCAPE:
                                    continuer = 0
                              elif event.key == K_p:
                                    game = False
                                    pause = True
                              
                        if event.type == KEYDOWN:
              
                              if event.key == K_RIGHT or event.key == K_d:
                                    bas = 1
                                    D+=1
                                    if D == 11:
                                          D = 0
                                    G = 0
                                    persoX += 5
                                    if persoX+100 >= 700:
                                          persoX = 599
                                    direction = 1
                                    if structure_niveau[PersoHaut][PersoDroite] == 1 or structure_niveau[PersoBas][PersoDroite] == 1:
                                          structure_niveau[CasePersoY][PersoDroite] = 0
                                          vie+=20
                                          score += 500
                                    elif structure_niveau[PersoHaut][PersoDroite] != 0 or structure_niveau[PersoBas][PersoDroite] != 0:
                                          persoX -= 5
                                  
                              elif event.key == K_LEFT or event.key == K_a:
                                    bas = 2
                                    G+=1
                                    if G == 11:
                                          G = 0
                                    D = 0
                                    persoX -= 5
                                    if persoX <= 0:
                                          persoX = 0
                                    direction = 2
                                    if structure_niveau[PersoHaut][PersoGauche] == 1 or structure_niveau[PersoBas][PersoGauche] == 1:
                                          structure_niveau[CasePersoY][PersoGauche] = 0
                                          vie+=20
                                          score += 500
                                    if structure_niveau[PersoHaut][PersoGauche] != 0 or structure_niveau[PersoBas][PersoGauche] != 0:
                                          persoX += 5
                              
                              elif event.key == K_DOWN or event.key == K_s:
                                    direction = 3

                              elif event.key == K_UP or event.key == K_w:
                                    direction = 4
                                    
                              #destruction des blocs en appuyant sur espace      
                              elif event.key == K_SPACE and not tombe:
                                    pygame.time.delay(50)
                                    sonBloc.play()
                                    if direction == 4:
                                          if structure_niveau[CasePersoY-1][CasePersoX] != 1:
                                                if structure_niveau[CasePersoY-1][CasePersoX] == 2:
                                                      structure_niveau[CasePersoY-1][CasePersoX] = 9
                                                elif structure_niveau[CasePersoY-1][CasePersoX] == 9:
                                                      structure_niveau[CasePersoY-1][CasePersoX] = 10
                                                elif structure_niveau[CasePersoY-1][CasePersoX] == 10:
                                                      structure_niveau[CasePersoY-1][CasePersoX] = 11
                                                elif structure_niveau[CasePersoY-1][CasePersoX] == 11:
                                                      structure_niveau[CasePersoY-1][CasePersoX] = 12
                                                elif structure_niveau[CasePersoY-1][CasePersoX] == 12:
                                                      structure_niveau[CasePersoY-1][CasePersoX] = 0
                                                      vie-=20
                                                      score-=500
                                                elif structure_niveau[CasePersoY-1][CasePersoX] == 7:
                                                      structure_niveau[CasePersoY-1][CasePersoX] = 0
                                                      score += 5
                                                elif structure_niveau[CasePersoY-1][CasePersoX] == 8:
                                                      pygame.time.delay(1000)
                                                      score += 5
                                                      structure_niveau[CasePersoY-1][CasePersoX] = 0
                                                else:
                                                      couleur = structure_niveau[CasePersoY-1][CasePersoX]
                                                      structure_niveau[CasePersoY-1][CasePersoX] = 0
                                                      score += 10
                                                      monBlocX = CasePersoX
                                                      monBlocY = CasePersoY-1
                                                      structure_niveau, score = detruireAutour(structure_niveau,monBlocX,monBlocY,couleur,score)
                                    elif direction == 3:
                                          if structure_niveau[CasePersoY+1][CasePersoX] != 1:
                                                if structure_niveau[CasePersoY+1][CasePersoX] == 2:
                                                      structure_niveau[CasePersoY+1][CasePersoX] = 9
                                                elif structure_niveau[CasePersoY+1][CasePersoX] == 9:
                                                      structure_niveau[CasePersoY+1][CasePersoX] = 10
                                                elif structure_niveau[CasePersoY+1][CasePersoX] == 10:
                                                      structure_niveau[CasePersoY+1][CasePersoX] = 11
                                                elif structure_niveau[CasePersoY+1][CasePersoX] == 11:
                                                      structure_niveau[CasePersoY+1][CasePersoX] = 12
                                                elif structure_niveau[CasePersoY+1][CasePersoX] == 12:
                                                      structure_niveau[CasePersoY+1][CasePersoX] = 0
                                                      vie-=20
                                                      score-=500
                                                elif structure_niveau[CasePersoY+1][CasePersoX] == 7:
                                                      structure_niveau[CasePersoY+1][CasePersoX] = 0
                                                      score += 5
                                                elif structure_niveau[CasePersoY+1][CasePersoX] == 8:
                                                      pygame.time.delay(1000)
                                                      score += 5
                                                      structure_niveau[CasePersoY+1][CasePersoX] = 0
                                                else:
                                                      couleur = structure_niveau[CasePersoY+1][CasePersoX]
                                                      structure_niveau[CasePersoY+1][CasePersoX] = 0
                                                      score += 10
                                                      monBlocX = CasePersoX
                                                      monBlocY = CasePersoY+1
                                                      structure_niveau, score = detruireAutour(structure_niveau,monBlocX,monBlocY,couleur,score)
                                    elif direction == 2 and CasePersoX !=0 :
                                          if structure_niveau[CasePersoY][CasePersoX-1] != 1:
                                                if structure_niveau[CasePersoY][CasePersoX-1] == 2:
                                                      structure_niveau[CasePersoY][CasePersoX-1] = 9
                                                elif structure_niveau[CasePersoY][CasePersoX-1] == 9:
                                                      structure_niveau[CasePersoY][CasePersoX-1] = 10
                                                elif structure_niveau[CasePersoY][CasePersoX-1] == 10:
                                                      structure_niveau[CasePersoY][CasePersoX-1] = 11
                                                elif structure_niveau[CasePersoY][CasePersoX-1] == 11:
                                                      structure_niveau[CasePersoY][CasePersoX-1] = 12
                                                elif structure_niveau[CasePersoY][CasePersoX-1] == 12:
                                                      structure_niveau[CasePersoY][CasePersoX-1] = 0
                                                      vie-=20
                                                      score-=500
                                                elif structure_niveau[CasePersoY][CasePersoX-1] == 7:
                                                      structure_niveau[CasePersoY][CasePersoX-1] = 0
                                                      score += 5
                                                elif structure_niveau[CasePersoY][CasePersoX-1] == 8:
                                                      pygame.time.delay(1000)
                                                      score += 5
                                                      structure_niveau[CasePersoY][CasePersoX-1] = 0
                                                else:
                                                      couleur = structure_niveau[CasePersoY][CasePersoX-1]
                                                      structure_niveau[CasePersoY][CasePersoX-1] = 0
                                                      score += 10
                                                      monBlocX = CasePersoX-1
                                                      monBlocY = CasePersoY
                                                      structure_niveau, score = detruireAutour(structure_niveau,monBlocX,monBlocY,couleur,score)
                                    elif direction == 1 and CasePersoX != 6:
                                          if structure_niveau[CasePersoY][CasePersoX+1] != 1:
                                                if structure_niveau[CasePersoY][CasePersoX+1] == 2:
                                                      structure_niveau[CasePersoY][CasePersoX+1] = 9
                                                elif structure_niveau[CasePersoY][CasePersoX+1] == 9:
                                                      structure_niveau[CasePersoY][CasePersoX+1] = 10
                                                elif structure_niveau[CasePersoY][CasePersoX+1] == 10:
                                                      structure_niveau[CasePersoY][CasePersoX+1] = 11
                                                elif structure_niveau[CasePersoY][CasePersoX+1] == 11:
                                                      structure_niveau[CasePersoY][CasePersoX+1] = 12
                                                elif structure_niveau[CasePersoY][CasePersoX+1] == 12:
                                                      structure_niveau[CasePersoY][CasePersoX+1] = 0
                                                      vie-=20
                                                      score-=500
                                                elif structure_niveau[CasePersoY][CasePersoX+1] == 7:
                                                      structure_niveau[CasePersoY][CasePersoX+1] = 0
                                                      score += 5
                                                elif structure_niveau[CasePersoY][CasePersoX+1] == 8:
                                                      pygame.time.delay(1000)
                                                      score += 5
                                                      structure_niveau[CasePersoY][CasePersoX+1] = 0
                                                else:
                                                      couleur = structure_niveau[CasePersoY][CasePersoX+1]
                                                      structure_niveau[CasePersoY][CasePersoX+1] = 0
                                                      score += 10
                                                      monBlocX = CasePersoX+1
                                                      monBlocY = CasePersoY
                                                      structure_niveau, score = detruireAutour(structure_niveau,monBlocX,monBlocY,couleur,score)               

                  #fond bleu
                  fenetre.fill((163,223,243))
                  fenetre.blit(fondBois,(700,0))
                  
                  #trait qui separe jeu et hud
                  limiteD = pygame.draw.line(fenetre,(255,255,255),(700,0),(700,800),1)

                  #appel des fonctions
                  CasePersoX, CasePersoY, PersoDroite, PersoGauche, PersoHaut, PersoBas = collision(structure_niveau, persoX, persoY, hauteur)
                  affichage(structure_niveau)

                  #gravite
                  if CasePersoY+1 >= 105: #changement de niveau
                        direction = 3
                        hauteur -= 5
                        score+=5000
                        tombe = True
                        CasePersoY = 0
                        level += 1
                        hauteur = 400
                        game = False
                        changementNiveau = True
                  elif structure_niveau[CasePersoY+1][CasePersoX] == 0:
                        direction = 3
                        hauteur -= 5
                        score+=1
                        tombe = True
                  elif structure_niveau[CasePersoY+1][CasePersoX] == 1:
                        structure_niveau[CasePersoY+1][CasePersoX] = 0
                        vie+=20
                        score+=500
                  else :
                        tombe = False

                  #chute des blocs
                  if saveTempsCubes+0.7 < (time.time()-start):
                        saveTempsCubes = time.time()-start
                        
                        for y in range(len(structure_niveau)-1,0,-1):
                              for x in range(len(structure_niveau[0])-1,-1,-1):
                                    if structure_niveau[y][x] == 0 and y != 104 and x != 7 and structure_niveau[y-1][x] == 1:
                                          structure_niveau[y][x] = structure_niveau[y-1][x]
                                          structure_niveau[y-1][x] = 0
                                    if structure_niveau[y][x] == 0 and y != 104 and x != 7 and (not structure_niveau[y-1][x] == structure_niveau[y-1][x-1] or structure_niveau[y][x-1] == 0) and (not structure_niveau[y-1][x] == structure_niveau[y-1][x+1] or structure_niveau[y][x+1] == 0): 
                                          structure_niveau[y][x] = structure_niveau[y-1][x]
                                          structure_niveau[y-1][x] = 0
                                    elif structure_niveau[y][x] == 0 and y != 104 and x != 7 and (structure_niveau[y-1][x] == structure_niveau[y-1][x-1] or structure_niveau[y-1][x] == structure_niveau[y-1][x+1] or structure_niveau[y-1][x] == structure_niveau[y][x] or structure_niveau[y-1] == structure_niveau[y-2]):
                                          nbrBlocs = 1
                                          copieStructure = deepcopy(structure_niveau)
                                          nbrBlocs = detecterAutour(copieStructure,x,(y-1),(structure_niveau[y-1][x]),nbrBlocs)
                                          if nbrBlocs >= 4:
                                                couleur = structure_niveau[y-1][x]
                                                structure_niveau[y-1][x] = 0
                                                structure_niveau, score = detruireAutour(structure_niveau,x,(y-1),couleur,score)

                              if structure_niveau[CasePersoY][CasePersoX] != 0 and structure_niveau[CasePersoY][CasePersoX] != 1:
                                    vie -= 100
                                    score -= 1000
                                    for i in range(CasePersoY):
                                          structure_niveau[CasePersoY-i][CasePersoX]=0
                                          structure_niveau[CasePersoY-i][CasePersoX+1]=0
                                          structure_niveau[CasePersoY-i][CasePersoX-1]=0
    
                  #mouvements du perso  
                  if direction == 1:
                        fenetre.blit(droite[D],(persoX,persoY))
                  elif direction == 2:
                        fenetre.blit(gauche[G],(persoX,persoY))
                  elif direction == 3:
                        if bas == 1:
                              fenetre.blit(basDroite,(persoX,persoY))
                        elif bas == 2:
                              fenetre.blit(basGauche,(persoX,persoY))
                  elif direction == 4:
                        fenetre.blit(haut,(persoX,persoY))
                  if score < 0 or (CasePersoY-3+103*level) == 0:
                        score = 0

                  #appel des fonction pour le hud (coeurs, barre de vie et timer)
                  barreVie, nbrVie, vie, saveSecondes = affichageBarreDeVie(barreVie, nbrVie, vie, saveSecondes, secondes, horloge, timer)

                  temps,saveTemps,secondes,minutes,timer = theTimer(start,temps,saveTemps,secondes,minutes,timer)
                  
                  musique, game, fin = lesVies(coeurRouge,coeurGris,nbrVie, font, musique, game, fin)
                  
            #boucle de defaite   
            elif fin:
                  for event in pygame.event.get():

                        if event.type == QUIT:
                              continuer = 0
                          
                        if event.type == KEYUP:
                          
                              if event.key == K_ESCAPE:
                                    continuer = 0
                
                  fenetre.blit(defaite, (0,0))
                  pygame.display.flip()

                  pygame.time.delay(8000)
                  fin = False
                  saisieDuPseudo = True

            #boucle de victoire
            elif victoire:
                  for event in pygame.event.get():

                        if event.type == QUIT:
                              continuer = 0
                          
                        if event.type == KEYUP:
                          
                              if event.key == K_ESCAPE:
                                    continuer = 0
                
                  fenetre.blit(victory, (0,0))
                  pygame.display.flip()

                  pygame.time.delay(8000)
                  victoire = False
                  saisieDuPseudo = True

            #boucle de saisie du pseudo pour les meilleurs scores
            elif saisieDuPseudo: 
                  fenetre.fill((0,0,0))       
                  monInput, maj, continuer, saisieDuPseudo, reinitialiser = Inputer(monInput,maj,continuer,saisieDuPseudo,reinitialiser,score)
                  
            #boucle de pause
            elif pause:
                  for event in pygame.event.get():

                        if event.type == QUIT:
                              continuer = 0
                          
                        if event.type == KEYUP:
                          
                              if event.key == K_ESCAPE:
                                    continuer = 0

                              elif event.key == K_p:
                                    game = True
                                    pause = False
                                    fondBlit = 0

                  fenetre.blit(imagePause, (0,0))

                  if fondBlit < 8:
                        fenetre.blit(fondPause, (0,0))
                        fondBlit += 1

            elif changementNiveau:
                  for event in pygame.event.get():

                        if event.type == QUIT:
                              continuer = 0
                          
                        if event.type == KEYUP:
                          
                              if event.key == K_ESCAPE:
                                    continuer = 0
                                    

                  if level == 1:
                        niveau = "niveaux/niveau2.txt"
                        score += 3000
                  elif level == 2:
                        niveau = "niveaux/niveau3.txt"
                        score += 3000
                  elif level == 3:
                        niveau = "niveaux/niveau4.txt"
                        score += 3000
                  elif level == 4:
                        niveau = "niveaux/niveau5.txt"
                        score += 3000
                  elif level == 5:
                        niveau = "niveaux/niveau6.txt"
                        score += 3000
                  elif level == 6:
                        niveau = "niveaux/niveau7.txt"
                        score += 3000
                  elif level == 7:
                        niveau = "niveaux/niveau8.txt"
                        score += 3000
                  elif level == 8:
                        niveau = "niveaux/niveau9.txt"
                        score += 3000
                  elif level == 9:
                        niveau = "niveaux/niveau10.txt"
                        score += 3000
                  elif level == 10:
                        score += 3000
                        changementNiveau = False
                        victoire = True

                  structure_niveau = lecture(niveau)
                  score += 1000
                  changementNiveau = False
                  game = True


            #actualisation de la fenetre
            pygame.display.flip()
            pygame.time.delay(10)   
                
        
            
except:    
    traceback.print_exc()    
finally:
    pygame.quit()
    exit()
