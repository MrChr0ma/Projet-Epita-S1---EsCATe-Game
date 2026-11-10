import random as rd
import subprocess
import platform
import time

# Codes couleur ANSI
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
ORANGE = "\033[38;5;214m"
GRAY = "\033[90m"



plateau_1 =       [ ["  ","A","B","C","D","E","F","G","H","I","J","K"],
                    ["1 ",".",".",".",".",".","S",".",".",".",".","."],
                    ["2 ",".",".","W",".",".",".",".",".","W",".","."],
                    ["3 ",".",".",".",".","O","O","O",".",".",".","."],
                    ["4 ",".",".",".",".","O","O","O",".",".",".","."],
                    ["5 ","S",".",".",".",".",".",".",".",".",".","S"],
                    ["6 ",".",".",".",".",".",".",".",".",".",".","."],
                    ["7 ",".",".",".",".",".",".",".",".",".",".","."],
                    ["8 ",".",".",".",".",".","C",".",".",".",".","."],
                    ["9 ",".",".",".",".","C","C","C",".",".",".","."],
                    ["10",".",".",".","C","C","C","C","C",".",".","."],
                    ["11",".",".",".","C","C","C","C","C",".",".","."]]

plateau_2 =       [ ["  ","A","B","C","D","E","F","G","H","I","J","K"],
                    ["1 ",".",".",".",".",".","S",".",".",".",".","."],
                    ["2 ",".",".","W",".",".",".",".",".","W",".","."],
                    ["3 ",".",".",".",".","O","O","O",".",".",".","."],
                    ["4 ",".",".",".",".","O","O","O",".",".",".","."],
                    ["5 ","S",".",".",".",".",".",".",".",".",".","S"],
                    ["6 ",".",".",".",".",".",".",".",".",".",".","."],
                    ["7 ",".",".",".",".",".",".",".",".",".",".","."],
                    ["8 ",".",".",".",".",".","C",".",".",".",".","."],
                    ["9 ",".",".",".",".","C","C","C",".",".",".","."],
                    ["10",".",".",".","C","C","C","C","C",".",".","."],
                    ["11",".",".",".","C","C","C","C","C",".",".","."]]
chat = [(11,4),(11,5),(11,6),(11,7),(11,8),(10,4),(10,5),(10,6),(10,7),(10,8),(9,5),(9,6),(9,7),(8,6)]
#chat  = [(2,5),(2,10)]
gardiens = [(2,3),(2,9)]
sortie = [(1,6),(5,1),(5,11)]
robot = []
bassin = [(3,5),(3,6),(3,7),(4,5),(4,6),(4,7)]
portail = []
score_A ,score_B = 0,0
chat_immobile=[]
filet_restant=2
pos_filet=[]
filet_pose_au_tour = {}  
tour_actuel = 0
J1 , J2 = "" , ""

def print_plateau(plateau):
    global J1,J2,score_A,score_B
    for i,ligne in enumerate(plateau):
        for j,case in enumerate(ligne):
            if i == 0 or j == 0:  # En-têtes (lettres et numéros)
                print(f"{BLUE}{case}{RESET}", end=" ")
            elif case == 'C':
                print(f"{BLUE}C{RESET}", end=" ")
            elif case == "W":
                print(f"{RED}W{RESET}", end=" ")
            elif case == "R":
                print(f"{GRAY}R{RESET}", end=" ")
            elif case == "O":
                print(f"{CYAN}O{RESET}", end=" ")
            elif case == "S":
                print(f"{GREEN}S{RESET}", end=" ")
            elif case == "T":
                print(f"{MAGENTA}T{RESET}", end=" ")
            elif case == ".":
                print(".", end=" ")
            else:
                print(case,end = " ")
            if j == 11:
                if i == 0:
                    print(" "*5+f"LEGENDS : ",end = " ")
                elif i == 2 :
                    print(" "*7+f"CHAT : {BLUE}C{RESET}",end = " ")
                elif i == 3 :
                    print(" "*7+f"GARDIEN : {RED}W{RESET}",end = " ")
                elif i == 4 :
                    print(" "*7+f"PORTAIL : {MAGENTA}T{RESET}",end = " ")
                elif i == 6 :
                    print(" "*7+f"BASSIN : {CYAN}O{RESET}",end = " ")
                elif i == 5 :
                    print(" "*7+f"SORTIE : {GREEN}S{RESET}",end = " ")
                elif i == 7 :
                    print(" "*7+f"ROBOT : {GRAY}R{RESET}",end = " ")
                elif i == 9 :
                    print(" "*5+f"SCORE : {J1} : {score_A}",end = " ")
                elif i == 10:
                    print(" "*13+f"{J2} : {score_B}",end = " ")
        print("")               
def clear_terminal():
        if platform.system() == "Windows":
            subprocess.run('cls', shell=True)
        else:
            subprocess.run('clear', shell=True)   
#implemente les filets
def nettoyer_filets(plateau, pos_filet):
    """Enleve les filets places sur des cases vides apres 1 tour"""
    filets_a_retirer = []
    
    for (x, y) in pos_filet:
        # vérifier directement si c'est un F
        if plateau[x][y] == "F":
            if (x, y) in filet_pose_au_tour and (tour_actuel - filet_pose_au_tour[(x, y)]) >= 1:
                if (x,y) in chat:
                    plateau[x][y] = "C"
                else:
                    plateau[x][y] = "."
                filets_a_retirer.append((x, y))
                del filet_pose_au_tour[(x, y)]
    
    #retirer les positions de filets nettoyes
    for pos in filets_a_retirer:
        pos_filet.remove(pos)
def poser_filet(x, y, plateau, chat):
    global filet_restant, pos_filet, filet_pose_au_tour, tour_actuel,chat_immobile

    if plateau[x][y] == ".":
        plateau[x][y] = "F"
        pos_filet.append((x, y))
        filet_pose_au_tour[(x, y)] = tour_actuel
        filet_restant -= 1
        return True

    elif plateau[x][y] == "C" or plateau[x][y] == f"{BLUE}C{RESET}":
        pos_filet.append((x, y))
        if (x, y) in chat:
            chat_immobile.append((x, y))
            print("Chat immobilisé pour 1 tour")
            plateau[x][y] = "F"
        filet_pose_au_tour[(x, y)] = tour_actuel
        filet_restant -= 1
        return True

    else:
        print("Case déjà occupée. Choisissez une case libre ou avec un chat")
        return False
def demander_case_filet():
    while True:
        placement = input("Sur quelle case souhaitez vous placer le filet : ").strip().upper()
        if placement == "":
            return None

        try:
            return conversion(placement)
        except (ValueError, IndexError, KeyError):
            print("Format invalide. Exemple : A6, D11, 2A...")
def filet(plateau, chat):
    global filet_restant

    if filet_restant == 0:
        print("Vous avez utilisé vos 2 filets")
        return

    print("\n== PLACEMENT DES FILETS ===")
    print(f"Filets restants : {filet_restant}")
    print("Appuyer sur Entrée si vous ne souhaitez pas poser de filet")

    while filet_restant > 0:
        case = demander_case_filet()

        if case is None:
            print("Aucun filet joué ce tour")
            break

        x, y = case
        if poser_filet(x, y, plateau, chat):
            clear_terminal()
            print_plateau(plateau)
            print(f"Filets restants : {filet_restant}")

            if filet_restant > 0:
                suivant = input("Voulez vous placer un autre filet ? Y/N : ").strip().upper()
                if suivant not in ["Y", "YES"]:
                    break

    print("Fin placement des filets")     
#verifie que l'utilisateur bouge 7 chats ou moins si moins de 7 chats
#demande le chat à bouger et la case choisi
#appelle what_square() pour savoir si la case est valide
#si elle est valide effectuer le mouvement
#et demande un autre chat etc...
#!ATTENTION prendre en compte les sorties (si le chat sort le retirer de la liste_chat et ajouter 1 au score)


def error(msg):
    """Affiche un message d'erreur formaté"""
    print("\n" + f"{RED}!{RESET}"*50)
    print(f"{RED} ERREUR : {msg}{RESET}")
    print(f"{RED}!{RESET}"*50 + "\n")


def afficher_chats_possibles(chats_non_deplaces, plateau, what_square):
    """Affiche les chats disponibles et retourne la liste"""
    print("Chats pouvant être déplacés :")
    disponibles = []
    
    for c in chats_non_deplaces:
        if what_square(c, "C", plateau):
            ligne, col = c
            lettre = plateau[0][col]
            print(f"  - {lettre}{ligne}")
            disponibles.append(c)
    
    if not disponibles:
        print("  Aucun chat disponible pour déplacement.")
    
    return disponibles


def afficher_destinations_possibles(cases_possibles, plateau, portail, sorties):
    """Affiche les destinations possibles avec leurs types"""
    print("Déplacements possibles (tapez 'RETOUR' ou 'BACK' pour changer de chat) :")
    
    for ligne_case, col_case in cases_possibles:
        lettre_case = plateau[0][col_case]
        msg = f"  - {lettre_case}{ligne_case}"
        
        if (ligne_case, col_case) in portail:
            msg += " (PORTAIL)"
        elif (ligne_case, col_case) in sorties:
            msg += " (SORTIE)"
        
        print(msg)


def gerer_visuel_plateau(plateau, cases_possibles, chat_pos, portail, action="colorer"):
    """Colore ou restaure les cases du plateau"""
    ligne_chat, col_chat = chat_pos
    
    if action == "colorer":
        plateau[ligne_chat][col_chat] = f"{GREEN}C{RESET}"
        for x, y in cases_possibles:
            contenu = plateau[x][y]
            if contenu == ".":
                plateau[x][y] = f"{YELLOW}*{RESET}"
            elif contenu in ["T", "S"]:
                plateau[x][y] = f"{YELLOW}{contenu}{RESET}"
    else:  # restaurer
        plateau[ligne_chat][col_chat] = "T" if chat_pos in portail else "C"
        for x, y in cases_possibles:
            contenu = plateau[x][y]
            if f"{YELLOW}" in contenu:
                if "T" in contenu:
                    plateau[x][y] = "T"
                elif "S" in contenu:
                    plateau[x][y] = "S"
                else:
                    plateau[x][y] = "."


def deplacement_un_chat(chat, plateau, chats_non_deplaces, conversion, 
                       what_square, portail, sorties, score, num, total):
    """Gère le déplacement complet d'un chat"""
    
    while True:
        clear_terminal()
        print_plateau(plateau)
        print(f"\n--- Déplacement {num}/{total} ---")
        
        # Afficher et choisir le chat
        disponibles = afficher_chats_possibles(chats_non_deplaces, plateau, what_square)
        if not disponibles:
            return None, score, True
        
        # Saisie du chat
        while True:
            choix_input = input("Choisir le chat à déplacer (ex: D11, F8): ").strip().upper()
            try:
                ligne_choix, col_choix = conversion(choix_input)
                if (ligne_choix, col_choix) in disponibles:
                    chat_pos = (ligne_choix, col_choix)
                    break
                else:
                    error("Ce chat n'existe pas ou a déjà été déplacé.")
            except (ValueError, IndexError, KeyError):
                error("Format invalide. Exemple : A6, D11, 2A...")
        
        # Vérifier les cases possibles
        cases_possibles = what_square(chat_pos, "C", plateau)
        if not cases_possibles:
            clear_terminal()
            print_plateau(plateau)
            error("Aucun déplacement possible pour ce chat.")
            input("Appuyez sur Entrée pour continuer...")
            continue
        
        # Colorer et afficher le plateau
        gerer_visuel_plateau(plateau, cases_possibles, chat_pos, portail, "colorer")
        clear_terminal()
        print_plateau(plateau)
        afficher_destinations_possibles(cases_possibles, plateau, portail, sorties)
        
        # Choix de la destination
        while True:
            destination_input = input("\nDestination (A2, B3, 2A, ...) : ").strip().upper()
            
            if destination_input in ["RETOUR", "BACK"]:
                gerer_visuel_plateau(plateau, cases_possibles, chat_pos, portail, "restaurer")
                break
            
            try:
                destination = conversion(destination_input)
                
                if destination not in cases_possibles:
                    clear_terminal()
                    print_plateau(plateau)
                    error("Déplacement invalide, choisissez une case affichée.")
                    afficher_destinations_possibles(cases_possibles, plateau, portail, sorties)
                    continue
                
                gerer_visuel_plateau(plateau, cases_possibles, chat_pos, portail, "restaurer")
                
                # Exécution du déplacement
                ligne_chat, col_chat = chat_pos
                
                # Cas sortie
                if destination in sorties:
                    plateau[ligne_chat][col_chat] = "T" if chat_pos in portail else "."
                    chat.remove(chat_pos)
                    score += 1
                    print(f"\nLe chat s'évade par la sortie {destination_input} !")
                    clear_terminal()
                    print_plateau(plateau)
                    print(f"Score : {score} chat évadé(s)\n")
                    return None, score, True
                
                # Cas portail
                elif plateau[destination[0]][destination[1]] == "T":
                    index_portail = portail.index(destination)
                    portail_libre = 1 - index_portail
                    px, py = portail[portail_libre]
                    
                    plateau[ligne_chat][col_chat] = "T" if chat_pos in portail else "."
                    plateau[px][py] = f"{GREEN}C{RESET}"
                    
                    idx = chat.index(chat_pos)
                    chat[idx] = (px, py)
                    nouvelle_pos = (px, py)
                
                # Cas normal
                else:
                    plateau[ligne_chat][col_chat] = "T" if chat_pos in portail else "."
                    plateau[destination[0]][destination[1]] = f"{GREEN}C{RESET}"
                    
                    idx = chat.index(chat_pos)
                    chat[idx] = destination
                    nouvelle_pos = destination
                
                clear_terminal()
                print_plateau(plateau)
                return nouvelle_pos, score, True
                
            except (ValueError, IndexError, KeyError):
                error("Format invalide. Exemple : A2, B3, 2A...")


def recolorer_chats_deplaces(plateau, chats_deplaces):
    """Recolore les chats déplacés en bleu"""
    for x, y in chats_deplaces:
        plateau[x][y] = f"{BLUE}C{RESET}"


def move_chat(chat, plateau, score, conversion, what_square):
    """Gère le déplacement de 7 chats maximum"""
    sorties = [(1, 6), (5, 1), (5, 11)]
    
    if len(chat) == 0:
        print("Il n'y a plus de chats sur le plateau !")
        return score
    
    chats_bloques = sum(1 for filet in pos_filet if filet in chat)
    nb_chats_a_bouger = min(7, len(chat) - chats_bloques)
    
    print("\n=== PHASE CHATS ===")
    print(f"Vous devez déplacer {nb_chats_a_bouger} chat{'s' if nb_chats_a_bouger > 1 else ''}.")
    print(f"Chats disponibles: {len(chat)}")
    
    chats_deplaces = []
    
    for i in range(nb_chats_a_bouger):
        chats_non_deplaces = [c for c in chat 
                              if c not in chats_deplaces and c not in pos_filet]
        
        if not chats_non_deplaces:
            print("Tous les chats ont été déplacés !")
            break
        
        nouvelle_pos, score, _ = deplacement_un_chat(
            chat, plateau, chats_non_deplaces, conversion, 
            what_square, portail, sorties, score, i+1, nb_chats_a_bouger
        )
        
        if nouvelle_pos:
            chats_deplaces.append(nouvelle_pos)
    
    recolorer_chats_deplaces(plateau, chats_deplaces)
    
    clear_terminal()
    print("\n=== FIN PHASE CHATS ===")
    print(f"Score actuel : {score} chat{'s' if score > 1 else ''} évadé{'s' if score > 1 else ''}")
    
    return score



#calcul les cases disponibles pour sauter les robots quand on est les gardiens
def jump_robots(pos_gardien,case_init,plateau):
    x,y=case_init
    try:
        if plateau[x][y]== "." or plateau[x][y]== f"{BLUE}C{RESET}" :
            if (x,y)!=(0,3):
                return (x,y)
        elif plateau[x][y] == f"{MAGENTA}T{RESET}" or plateau[x][y] == "T":
            index_portail = portail.index((x,y))
            portail_libre = 1 - index_portail
            px , py = portail[portail_libre] # calcul la case d arrive du portail
            if plateau[px][py] == f"{MAGENTA}T{RESET}" or plateau[px][py] == f"{BLUE}C{RESET}" or plateau[px][py] == "T" or plateau[px][py] == "C": # verifie si la case est libre
                return (px,py)
        elif plateau[x][y]==f"{RED}R{RESET}" or plateau[x][y] == "R":
            x_gard,y_gard=pos_gardien
            x_diff=x-x_gard
            y_diff=y-y_gard
            prochaine_case=(x+x_diff,y+y_diff)
            return jump_robots(case_init,prochaine_case,plateau)
        else:
            return None
    except IndexError:
        return None
#verifie que l'utilisateur bouge les 2 gardiens
#demande le gardiens à bouger et la case choisi
#appelle what_square() pour savoir si la case est valide
#si elle est valide effectuer le mouvement
#et demande le deuxieme gardien
#!ATTENTION prendre en compte les chat(si on le mange il faut le retirer de la liste)(et ils peuvent sauter par dessus les robot donc rajouter 1 de range)
def move_one_gardien(gardiens,chat,plateau,choice):
    ligne, col = gardiens[choice]
    lettre = plateau[0][col]
    gardien_coord = lettre+str(ligne)
    case_dispo = what_square(gardiens[choice],"W",plateau)
    for x, y in case_dispo:
        if plateau[x][y] == ".":
            plateau[x][y] = f"{RED}*{RESET}"
        elif plateau[x][y] == "C" or plateau[x][y] == f"{BLUE}C{RESET}":
            plateau[x][y] = f"{RED}C{RESET}"
        elif plateau[x][y] == "R":
            plateau[x][y] = f"{RED}R{RESET}"
        elif plateau[x][y] == "T":
            plateau[x][y] = f"{RED}T{RESET}"

    clear_terminal()
    print_plateau(plateau)
    print(f"\nCases disponibles pour le gardien {gardien_coord} :")
    for ligne, col in case_dispo:
        lettre = plateau[0][col]
        msg = f"  - {lettre}{ligne}"
        if (ligne,col) in chat:
            msg += " (CHAT)"
        elif (ligne,col) in portail:
            msg += " (PORTAIL)"
        elif (ligne,col) in robot:
            msg += " (ROBOT)"
        print(msg)

    while True:
                choose_case=input("Sur quelle case souhaitez vous déplacer ce gardien : ").strip().upper()

                try:
                    case = conversion(choose_case)
                    if case not in case_dispo:
                        print("La case que vous avez selectionné n'est pas valide. Veuillez choisir une des cases valides ci-dessus")
                    else:
                        break
                except (ValueError, IndexError, KeyError):
                    print("Format invalide. Exemple : A6, D11, 2A...")

    posx,posy=gardiens[choice]
    x,y=case

    if (x,y) in robot:
        case = jump_robots(gardiens[choice],case,plateau) #jump_robots(case,(x+i,y+j),plateau)
        x,y = case


    if (plateau[x][y] == f"{RED}C{RESET}"):
        if (x,y) in chat:
            chat.remove((x,y))
            if (x,y) in portail:
                    index_portail = portail.index((x,y))
                    portail_libre = 1 - index_portail
                    px , py = portail[portail_libre]
                    gardiens[choice] = (px,py)
                    plateau[x][y] = "T"   #x et y = coordonnées du gardien 1 choisi par l utilisateur et donc la case sur laquelle il va se deplacer
                    if (posx,posy) in portail :
                        plateau[posx][posy] = 'T' 
                    else :
                        plateau[posx][posy] = '.' #posx et posy = coordonnées du gardien 1 avant deplacement
                    plateau[px][py] = 'W' #px et py  = case apres avoir pris le portail de teleportation i.e. les cc de l autre portail
            else:
                gardiens[choice] = case
                if (posx,posy) in portail :
                    plateau[posx][posy] = 'T'
                else: 
                    plateau[posx][posy] = '.'
                plateau[x][y] = 'W'


    elif (x,y) in portail:
        index_portail = portail.index((x,y))
        portail_libre = 1 - index_portail
        px , py = portail[portail_libre] # case du deuxieme portail donc case d arrive apres teleportation
        if (px,py) in chat: # si il y a un chat sur l arrive on le mange
            chat.remove((px,py))
            gardiens[choice] = (px,py)
            if (posx,posy) in portail :
                plateau[posx][posy] = 'T'
            else: 
                plateau[posx][posy] = '.'
            plateau[px][py] = 'W'
        elif (px,py) not in gardiens: # si case libre
            gardiens[choice] = (px,py)
            if (posx,posy) in portail :
                plateau[posx][posy] = 'T'
            else: 
                plateau[posx][posy] = '.'
            plateau[px][py] = 'W'
    else:
        gardiens[choice]= case
        if (posx,posy) in portail :
            plateau[posx][posy] = 'T'
        else: 
            plateau[posx][posy] = '.'
        plateau[x][y] = 'W'

    for x, y in case_dispo:
        if plateau[x][y] == f"{RED}*{RESET}":
            plateau[x][y] = "."
        elif plateau[x][y] == f"{RED}C{RESET}":
            plateau[x][y] = "C"
        elif plateau[x][y] == f"{RED}R{RESET}":
            plateau[x][y] = "R"
        elif plateau[x][y] == f"{RED}T{RESET}":
            plateau[x][y] = "T"

    clear_terminal()
    print_plateau(plateau)

    return 
def move_gardiens(gardiens,chat,plateau,score): # A Florentin
    '''
        Paramètres:
        - Gardiens: liste des positions des gardiens
        - Chat: liste des positions des chats
        - Plateau: grille de jeu

        Retourne:
        - Gardiens modifié
    '''
    print_plateau(plateau)
    filet(plateau,chat)
    print("\n=== PHASE GARDIENS ===")
    print("\nGardiens disponibles :")
    for i in range(len(gardiens)):
        ligne, col = gardiens[i]
        lettre = plateau[0][col]
        print(f"  Gardien {i} : {lettre}{ligne}")
    choice = input("Entrer le gardien que vous souhaitez déplacer 0 ou 1 : ")
    while choice not in ['1','0']:
        print("Entrez invalide vous devez rentrer 0 ou 1 en fonction du gardiens ci-dessus que vous souhaitez déplacer")
        choice=input("Entrer le gardien que vous souhaitez déplacer 0 ou 1 : ")
    choice = int(choice)
    first_choice=choice
    second_choice=1-first_choice

    move_one_gardien(gardiens,chat,plateau,first_choice)
    if len(chat) != 0 :
        move_one_gardien(gardiens,chat,plateau,second_choice)

    print("\n=== FIN PHASE GARDIENS ===")
    print(f" {14-len(chat)-score} chat{'s' if (14-len(chat)-score) > 1 else ''} capturé{'s' if (14-len(chat)-score) > 1 else ''}")
    return gardiens
#place les robots aleatoirement au debut
def robot_placement(plateau):
    global robot
    while len(robot) != 9:
        coordonnées = (rd.randint(1,11),rd.randint(1,11))
        if plateau[coordonnées[0]][coordonnées[1]] == "." :
            robot.append(coordonnées)
    for (x,y) in robot:
        plateau[x][y] = "R"
#calculer une proba de 1/3
#si 1 alors appeller what_square()
#effectuer un mvt aleatoire parmi ceux retourner par what_square()
def move_robot(robot,plateau): # A Enzo
    for x,y in robot :
        peut_bouger = rd.randint(1,3)
        if peut_bouger == 1 :
            case_dispo = what_square((x,y), "R",plateau)
            if len(case_dispo) != 0:
                nouvelle_coordonne_x, nouvelle_coordonne_y = rd.choice(case_dispo)
                plateau[x][y] = "."
                plateau[nouvelle_coordonne_x][nouvelle_coordonne_y] = "R"
                indice = robot.index((x,y))
                robot[indice] = (nouvelle_coordonne_x,nouvelle_coordonne_y)
    return 
# fonction conversion qui va recupérer les coordonnées entrées par l'utilisateur et les convertir en tuple (x,y) (case)
def conversion(case: str) -> tuple: #A Hector
    case = case.strip()
    lettre = ''
    nombre = ''
    for c in case:
        if c.isalpha():
            lettre += c
        elif c.isdigit():
            nombre += c
    if len(lettre) != 1 or len(nombre) == 0:
        raise ValueError("Format invalide : ex. A6 ou 6A")
    colonne = ord(lettre.upper()) - ord('A') + 1  
    ligne = int(nombre)                           
    return (ligne, colonne)
#La fonction prend en entrée la case de la piece etudié et son type : "C","W" ou "R" 
#Elle retourne la liste des cases diponibles pour un deplacement autour
#Elle est appelée dans les fonctions move_robot, move_chat et move_gardien
def what_square(case :tuple,types:str,plateau:list)->list: # A Gaël
    liste_case_disp = []
    x,y = case
    if types == "C":
        for i in range(-1 if x > 1 else 0,2 if x < 11 else 1):#verifie que le x reste dans le plateau
            for j in range(-1 if y > 1 else 0, 2 if y < 11 else 1):#verifie que le y reste dans le plateau
                if plateau[x+i][y+j] in (".","S"):
                    liste_case_disp.append((x+i,y+j))
                elif plateau[x+i][y+j] == "T":
                    index_portail = portail.index((x+i,y+j))
                    portail_libre = 1 - index_portail
                    px , py = portail[portail_libre]
                    if plateau[px][py] == "T":
                        liste_case_disp.append((x+i,y+j))  
    elif types == "W":
        for i in range(-1 if x > 1 else 0,2 if x < 11 else 1):
            for j in range(-1 if y > 1 else 0, 2 if y < 11 else 1):
                if plateau[x+i][y+j] in (".","C","R",f"{BLUE}C{RESET}"):
                    if plateau[x+i][y+j] == "R":
                        case_dispo=jump_robots(case,(x+i,y+j),plateau)
                        if case_dispo != None:
                            liste_case_disp.append((x+i,y+j))
                    else :
                        liste_case_disp.append((x+i,y+j))
                elif (x+i,y+j) in portail:
                    index_portail = portail.index((x+i,y+j))
                    portail_libre = 1 - index_portail
                    px , py = portail[portail_libre]
                    if (px,py) not in gardiens :
                        liste_case_disp.append((x+i,y+j))     
    elif types == "R":
        for i in (-1,1):
            if plateau[x+i if x+i != 12 else 0][y] == ".":
                liste_case_disp.append((x+i,y))
        for j in (-1,1):
            if plateau[x][y+j if y+j != 12 else 0] == ".":
                liste_case_disp.append((x,y+j))
    return liste_case_disp
def menu():
    print(f"{CYAN}╔═══════════════════════════════════╗{RESET}")
    print(f"{CYAN}║     BIENVENUE À ESCATE GAME       ║{RESET}")
    print(f"{CYAN}╚═══════════════════════════════════╝{RESET}\n")
    print("Entrer le nom du joueur 1 :")
    nom_j1 = str(input())
    print("Entrer le nom du joueur 2 :")
    nom_j2 = str(input())
    print(f"\n{YELLOW}1{RESET} : Lancer la partie")
    print(f"{YELLOW}2{RESET} : Règles du jeu")
    print("\nSélectionner 1 ou 2")
    nb = input()
    while nb not in ["1", "2"]:
        print("Sélection Invalide. Veuillez sélectionner 1 ou 2")
        nb = input()
    if nb == "2":
        clear_terminal()
        print(f"\n{GREEN}╔═══════════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{GREEN}║              RÈGLES DU JEU : ESCATE GAME                          ║{RESET}")
        print(f"{GREEN}╚═══════════════════════════════════════════════════════════════════╝{RESET}\n")
        
        print(f"{YELLOW}─── BUT DU JEU ───{RESET}")
        print("Deux manches avec inversion des rôles.")
        print(f"{GREEN}1 chat évadé = 1 point pour son joueur.{RESET}\n")
        
        print(f"{YELLOW}─── LÉGENDE DES SYMBOLES ───{RESET}")
        print(f"  {ORANGE}C{RESET} = Chat")
        print(f"  {RED}W{RESET} = Gardien (Warden)")
        print(f"  {GRAY}R{RESET} = Robot aspirateur")
        print(f"  {CYAN}O{RESET} = Bassin d'eau")
        print(f"  {GREEN}S{RESET} = Sortie")
        print(f"  {MAGENTA}T{RESET} = Téléporteur")
        print(f"  {BLUE}F{RESET} = Filet\n")
        
        print(f"{YELLOW}─── LES ACTEURS ET OBJETS ───{RESET}")
        print(f"{ORANGE}• CHATS (14){RESET} : Doivent atteindre une sortie {GREEN}(S){RESET}.")
        print(f"{RED}• GARDIENS (2){RESET} : Capturent les chats en allant sur leur case.")
        print(f"{GRAY}• ROBOTS (9){RESET} : Obstacles mobiles. 1/3 de chance de bouger (Horizontal/Vertical uniquement).")
        print(f"{BLUE}• FILETS (F){RESET} : Les gardiens en ont 2. Bloque une case ou immobilise un chat pendant 1 tour.")
        print(f"{MAGENTA}• TÉLÉPORTEURS (T){RESET} : Paire de cases liées. Apparaissent aléatoirement en debut de partie.\n")
        
        print(f"{YELLOW}─── MOUVEMENTS SPÉCIFIQUES ───{RESET}")
        print(f"{ORANGE}CHATS{RESET}/{RED}GARDIENS{RESET} : 1 case (Horizontal, Vertical, Diagonal).")
        print(f"{RED}SAUT{RESET} : Un gardien peut sauter par-dessus un robot vers la case opposée.")
        print(f"{MAGENTA}TÉLÉPORTATION{RESET} : 1 seul acteur (Chat ou Gardien) par tour. Teleporte sur l'autre portail {MAGENTA}T{RESET}.")
        print(f"   • Impossible d'utiliser si la case de sortie est occupée.\n")
        
        print(f"{YELLOW}─── ZONES DU PLATEAU (11x11) ───{RESET}")
        print(f"{GREEN}SORTIES (S){RESET} : (1, F), (5, A), (5, K). Un chat dessus s'évade et disparaît.")
        print(f"{CYAN}BASSIN (O){RESET} : 6 cases centrales infranchissables par tous.")
        print(f"DÉPART : Position toujours identiques à l'exeption des portails et des robots qui apparaissent aléatoirement en debut de partie.\n")
        
        print(f"{YELLOW}─── DÉROULEMENT D'UN TOUR ───{RESET}")
        print(f"{ORANGE}1. PHASE CHATS{RESET} : Déplacez 7 chats.")
        print(f"{RED}2. PHASE GARDIENS{RESET} : Déplacez les 2 gardiens + Action Filet.")
        print(f"{GRAY}3. PHASE ROBOTS{RESET} : Déplacement aléatoire (1/3 de chance par robot).\n")
        
        print(f"{YELLOW}─── FIN DE MANCHE ───{RESET}")
        print("Plus aucun chat sur le plateau (tous évadés ou capturés).\n")
        
        print(f"\n{YELLOW}╔═════════════════════════════════════════════════════════╗{RESET}")
        print(  f"{YELLOW}║       Appuyez sur ENTRÉE pour lancer la partie...       ║{RESET}")
        print(  f"{YELLOW}╚═════════════════════════════════════════════════════════╝{RESET}\n")
        input()

    return nom_j1 ,nom_j2
def place_portail(plateau,caseportail=None):
    """
    Place deux portails de téléportation 'T' sur des cases vides du plateau.
    """
    global portail
    cases_vides = []
    for i in range(1, len(plateau)):
        for j in range(1, len(plateau[i])):
            if plateau[i][j] == ".":
                cases_vides.append((i, j))
    if caseportail == None:
        portail1, portail2 = rd.sample(cases_vides, 2)
    else:
        portail1,portail2 = caseportail
    plateau[portail1[0]][portail1[1]] = "T"
    plateau[portail2[0]][portail2[1]] = "T"
    portail.append(portail1)
    portail.append(portail2)
    return portail1,portail2
def main():
    global chat,robot,gardiens,score_A,score_B,tour_actuel,pos_filet,filet_restant,filet_pose_au_tour,J1,J2
    J1 , J2 = menu()
    plateau = plateau_1
    robot_placement(plateau)
    caseportail = place_portail(plateau)
    print_plateau(plateau)
    filet_restant=2
    pos_filet=[]
    tour_actuel = 0
    filet_pose_au_tour = {}
    #game 1
    while len(chat) != 0:
        tour_actuel+=1
        move_chat(chat,plateau,score_A,conversion,what_square)
        if len(chat) == 0 :
            break
        move_gardiens(gardiens,chat,plateau,score_A)
        move_robot(robot,plateau)
        nettoyer_filets(plateau,pos_filet)
    #game 2
    print("partie2")
    time.sleep(10)
    plateau = plateau_2
    chat = [(11,4),(11,5),(11,6),(11,7),(11,8),(10,4),(10,5),(10,6),(10,7),(10,8),(9,5),(9,6),(9,7),(8,6)]
    gardiens = [(2,3),(2,9)]
    robot=[]
    filet_restant=2
    pos_filet=[]
    tour_actuel = 0
    filet_pose_au_tour = {}
    place_portail(plateau,caseportail)
    robot_placement(plateau)
    while len(chat) != 0:
        tour_actuel+=1
        move_chat(chat,plateau,score_B,conversion,what_square)
        if len(chat) == 0:
            break
        move_gardiens(gardiens,chat,plateau,score_B)
        move_robot(robot,plateau)
        nettoyer_filets(plateau,pos_filet)
    if score_A > score_B:
        print(f"{J1} a gagné")
    elif score_A < score_B:
        print(f"{J2} a gagné")
    else:
        print("EGALITE")
main()
