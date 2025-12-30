import random as rd
import subprocess
import platform

plateau_initial = [ ["  ","A","B","C","D","E","F","G","H","I","J","K"],
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
plateau = plateau_initial[:]
chat = [(11,4),(11,5),(11,6),(11,7),(11,8),(10,4),(10,5),(10,6),(10,7),(10,8),(9,5),(9,6),(9,7),(8,6)]
gardiens = [(2,3),(2,9)]
sortie = [(1,6),(5,1),(5,11)]
robot = []
bassin = [(3,5),(3,6),(3,7),(4,5),(4,6),(4,7)]
score_A ,score_B = 0,0

def print_plateau():
    for ligne in plateau:
        for case in ligne:
            print(case,end = " ")
        print("")               
def clear_terminal():
        if platform.system() == "Windows":
            subprocess.run('cls', shell=True)
        else:
            subprocess.run('clear', shell=True)           
#verifie que l'utilisateur bouge 7 chats ou moins si moins de 7 chats
#demande le chat à bouger et la case choisi
#appelle what_square() pour savoir si la case est valide
#si elle est valide effectuer le mouvement
#et demande un autre chat etc...
#!ATTENTION prendre en compte les sorties (si le chat sort le retirer de la liste_chat et ajouter 1 au score)
def move_chat(chat, plateau, score, conversion, what_square):
    """
    Gère le déplacement de 7 chats maximum
    
    Paramètres:
    - chat: liste des positions des chats [(ligne, colonne), ...]
    - plateau: grille avec en-têtes
    - score: score actuel du joueur chat
    - conversion: fonction qui convertit "A2" ou "2A" en (ligne, colonne)
    - what_square: fonction qui retourne les cases possibles pour un type de pièce
    
    Retourne:
    - chat modifié
    - score modifié
    """

    # ---------------------#
    #  Codes couleur ANSI  #
    # ---------------------#
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    # -------------------------------#
    #  Fonction d'affichage d'erreur #
    # -------------------------------#
    def error(msg):
        print("\n" + f"{RED}!{RESET}"*50)
        print(f"{RED} ERREUR : {msg}{RESET}")
        print(f"{RED}!{RESET}"*50 + "\n")

    sorties = [(1, 6), (5, 1), (5, 11)]
    nb_chats_a_bouger = min(7, len(chat))

    if len(chat) == 0:
        print("Il n'y a plus de chats sur le plateau !")
        return chat, score

    print("\n=== PHASE CHATS ===")
    print(f"Vous devez déplacer {nb_chats_a_bouger} chat{'s' if nb_chats_a_bouger > 1 else ''}.")
    print(f"Chats disponibles: {len(chat)}")
    chats_deplaces = []

    # -----------------------------------------------------#
    #              BOUCLE SUR LES 7 DÉPLACEMENTS           #
    # -----------------------------------------------------#
    for i in range(nb_chats_a_bouger):

        clear_terminal()
        print_plateau()
        print(f"\n--- Déplacement {i+1}/{nb_chats_a_bouger} ---")

        chats_non_deplaces = [c for c in chat if c not in chats_deplaces]

        if not chats_non_deplaces:
            print("Tous les chats ont été déplacés !")
            break

        deplacement_effectue = False
        
        while not deplacement_effectue:

            # --------------------#
            # Affichage des chats #
            # --------------------#
            print("Chats pouvant être déplacés :")
            disponibles = []
            for c in chats_non_deplaces:
                if what_square(c, "C",plateau):
                    ligne, col = c
                    lettre = plateau[0][col]
                    print(f"  - {lettre}{ligne}")
                    disponibles.append(c)
            if not disponibles:
                print("  Aucun chat disponible pour déplacement.")
                deplacement_effectue = True
                break

            # --------------#
            # Choix du chat #
            # --------------#
            while True:
                choix_input = input("Choisir le chat à déplacer (ex: D11, F8): ").strip().upper()

                try:
                    ligne_choix, col_choix = conversion(choix_input)
                    if (ligne_choix, col_choix) in chats_non_deplaces:
                        chat_a_bouger = (ligne_choix, col_choix)
                        break
                    else:
                        error("Ce chat n'existe pas ou a déjà été déplacé.")
                    
                except (ValueError, IndexError, KeyError):
                    error("Format invalide. Exemple : A6, D11, 2A...")

            ligne_chat, col_chat = chat_a_bouger
            # --------------------------------#
            # Colorer le chat dans le plateau #
            # --------------------------------#
            plateau[ligne_chat][col_chat] = f"{GREEN}C{RESET}"
            cases_possibles = what_square(chat_a_bouger, "C",plateau)

            if not cases_possibles:
                clear_terminal()
                print_plateau()
                error("Aucun déplacement possible pour ce chat.")
                plateau[ligne_chat][col_chat] = "C" 
                continue

            for case in cases_possibles:
                x, y = case
                if plateau[x][y] == ".":
                    plateau[x][y] = f"{YELLOW}*{RESET}"

            clear_terminal()
            print_plateau()

            # ---------------------------#
            # Affichage des déplacements #
            # ---------------------------#
            print("Déplacements possibles (tapez 'RETOUR' ou 'BACK' pour changer de chat) :")
            for case in cases_possibles:
                ligne_case, col_case = case
                lettre_case = plateau[0][col_case]
                msg = f"  - {lettre_case}{ligne_case}"
                if case in sorties:
                    msg += " (SORTIE)"
                print(msg)

            # ------------------------#
            # Choix de la destination #
            # ------------------------#
            while True:
                destination = input("\nDestination (A2, B3, 2A, ...) : ").strip().upper()

                if destination in ["RETOUR", "BACK"]:
                    plateau[ligne_chat][col_chat] = "C"
                    for x, y in cases_possibles:
                        if plateau[x][y] == f"{YELLOW}*{RESET}":
                            plateau[x][y] = "."
                    deplacement_effectue = False
                    clear_terminal()
                    print_plateau()
                    break

                try:
                    nouvelle_ligne, nouvelle_colonne = conversion(destination)

                    if (nouvelle_ligne, nouvelle_colonne) in cases_possibles:

                        for x, y in cases_possibles:
                            if plateau[x][y] == f"{YELLOW}*{RESET}":
                                plateau[x][y] = "."

                        # -------------------------#
                        # Cas sortie → chat évadé  #
                        # -------------------------#
                        if (nouvelle_ligne, nouvelle_colonne) in sorties:
                            print(f"\nLe chat s'évade par la sortie {destination} !")

                            plateau[ligne_chat][col_chat] = "."
                            chat.remove(chat_a_bouger)
                            score += 1

                            clear_terminal()
                            print_plateau()
                            print(f"Score : {score} chat évadé(s)\n")

                            deplacement_effectue = True
                            break

                        # -------------------#
                        # Déplacement normal #
                        # -------------------#
                        plateau[ligne_chat][col_chat] = "."
                        plateau[nouvelle_ligne][nouvelle_colonne] = f"{GREEN}C{RESET}"
                        idx = chat.index(chat_a_bouger)
                        chat[idx] = (nouvelle_ligne, nouvelle_colonne)

                        chats_deplaces.append((nouvelle_ligne, nouvelle_colonne))

                        clear_terminal()
                        print_plateau()
                        print(f"Chat déplacé vers {destination}\n")

                        deplacement_effectue = True
                        break

                    else:
                        clear_terminal()
                        print_plateau()
                        error("Déplacement invalide, choisissez une case affichée.")
                        for case in cases_possibles:
                            ligne_case, col_case = case
                            lettre_case = plateau[0][col_case]
                            msg = f"  - {lettre_case}{ligne_case}"
                            if case in sorties:
                                msg += " (SORTIE)"
                            print(msg)

                except (ValueError, IndexError, KeyError):
                    error("Format invalide. Exemple : A2, B3, 2A...")

            for x, y in cases_possibles:
                if plateau[x][y] == f"{YELLOW}*{RESET}":
                    plateau[x][y] = "."

    print("\n=== FIN PHASE CHATS ===")
    print(f"Score actuel : {score} chat{'s' if nb_chats_a_bouger > 1 else ''} évadé{'s' if nb_chats_a_bouger > 1 else ''}")

    return chat, score

#calcul les cases disponibles pour sauter les robots quand on est les gardiens
def jump_robots(pos_gardien,case_init,plateau):
    x,y=case_init
    try:
        if plateau[x][y]=='.' or plateau[x][y]=='C' :
            if (x,y)!=(0,3):
                return (x,y)
        elif plateau[x][y]=='R':
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

def move_gardiens(gardiens,chat,plateau): # A Florentin
    '''
        Paramètres:
        - Gardiens: liste des positions des gardiens
        - Chat: liste des positions des chats
        - Plateau: grille de jeu

        Retourne:
        - Gardiens modifié
    '''
    global chat_capture
    print_plateau()
    print("\n=== PHASE GARDIENS ===")
    print("\nGardiens disponibles :")
    for i in range(len(gardiens)):
        ligne, col = gardiens[i]
        lettre = plateau[0][col]
        print(f"  Gardien {i} : {lettre}{ligne}")
    choice=input("Entrer le gardien que vous souhaitez déplacer 0 ou 1 : ")
    while choice not in ['1','0']:
        print("Entrez invalide vous devez rentrer 0 ou 1 en fonction du gardiens ci-dessus que vous souhaitez déplacer")
        choice=input("Entrer le gardien que vous souhaitez déplacer 0 ou 1 : ")
    choice = int(choice)
    first_choice=choice
    second_choice=1-first_choice
    chat_capture=0
    ligne, col = gardiens[first_choice]
    lettre = plateau[0][col]
    gardien_coord = lettre+str(ligne)
    case_dispo = what_square(gardiens[first_choice],"W",plateau)
    clear_terminal()
    print_plateau()
    print(f"\nCases disponibles pour le gardien {gardien_coord} :")
    for ligne, col in case_dispo:
        lettre = plateau[0][col]
        print(f"  - {lettre}{ligne}")

    while True:
                choose_case=input("Sur quelle case souhaitez vous déplacer le premier gardien : ").strip().upper()

                try:
                    case = conversion(choose_case)
                    if case not in case_dispo:
                        print("La case que vous avez selectionné n'est pas valide. Veuillez choisir une des cases valides ci-dessus")
                    else:
                        break
                except (ValueError, IndexError, KeyError):
                    print("Format invalide. Exemple : A6, D11, 2A...")

    posx,posy=gardiens[first_choice]
    x,y=case

    if plateau[x][y]=="R":
        case=jump_robots(gardiens[first_choice],case,plateau)
        x,y=case
        if plateau[x][y]=="C":
            if (x,y) in chat:
                chat.remove((x,y))
                chat_capture+=1
        gardiens[first_choice]= case
        plateau[posx][posy] = '.'
        plateau[x][y] = 'W'
    elif plateau[x][y]=="C":
        if (x,y) in chat:
            chat.remove((x,y))
            chat_capture+=1
        gardiens[first_choice]= case
        plateau[posx][posy] = '.'
        plateau[x][y] = 'W'
    else:
        gardiens[first_choice]= case
        plateau[posx][posy] = '.'
        plateau[x][y] = 'W'
               
    clear_terminal()
    print_plateau()

    case_dispo = what_square(gardiens[second_choice],"W",plateau)
    clear_terminal()
    print_plateau()
    ligne, col = gardiens[second_choice]
    lettre = plateau[0][col]
    gardien_coord = lettre+str(ligne)
    print(f"\nCases disponibles pour le gardien {gardien_coord} :")
    for ligne, col in case_dispo:
        lettre = plateau[0][col]
        print(f"  - {lettre}{ligne}")

    while True:

        choose_case=input("Sur quelle case souhaitez vous déplacer le second gardien : ").strip().upper()
        try:
            case=conversion(choose_case)
            if case not in case_dispo:
                print("la case que vous souhaitez selectionné n'est pas valide. Veuillez choisir une des cases valides ci-dessus")
            else:
                break
        except (ValueError,IndexError,KeyError):
            print("Format invalide. Exemple : A6, D11, 2A...")


    posx,posy=gardiens[second_choice]
    x,y=case
           
    if plateau[x][y]=="R":
       case=jump_robots(gardiens[second_choice],case,plateau)
       x,y=case
       if plateau[x][y]=="C":
            if (x,y) in chat:
                chat.remove((x,y))
                chat_capture+=1
       gardiens[second_choice]=case
       plateau[posx][posy] = '.'
       plateau[x][y] = 'W'
    elif plateau[x][y]=="C":
        if (x,y) in chat:
            chat.remove((x,y))
            chat_capture+=1
        gardiens[second_choice]= case
        plateau[posx][posy] = '.'
        plateau[x][y] = 'W'
    else:
        gardiens[second_choice]= case
        plateau[posx][posy] = '.'
        plateau[x][y] = 'W'

    clear_terminal()
    print_plateau()

    print("\n=== FIN PHASE GARDIENS ===")
    print(f" {chat_capture} chat{'s' if chat_capture > 1 else ''} capturé{'s' if chat_capture > 1 else ''}")
    return gardiens

#place les robots aleatoirement au debut
def robot_placement():
    global robot
    while len(robot) != 9:
        coordonnées = (rd.randint(1,11),rd.randint(1,11))
        if coordonnées not in chat and coordonnées not in gardiens and coordonnées not in sortie and coordonnées not in robot and coordonnées not in bassin :
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
    elif types == "W":
        for i in range(-1 if x > 1 else 0,2 if x < 11 else 1):
            for j in range(-1 if y > 1 else 0, 2 if y < 11 else 1):
                if plateau[x+i][y+j] in (".","C","R"):
                    if plateau[x+i][y+j] == "R":
                        case_dispo=jump_robots(case,(x+i,y+j),plateau)
                        if case_dispo != None:
                            liste_case_disp.append((x+i,y+j))
                    else :
                        liste_case_disp.append((x+i,y+j))
    elif types == "R":
        for i in (-1,1):
            if plateau[x+i if x+i != 12 else 0][y] == ".":
                liste_case_disp.append((x+i,y))
        for j in (-1,1):
            if plateau[x][y+j if y+j != 12 else 0] == ".":
                liste_case_disp.append((x,y+j))
    return liste_case_disp
def main():
    global chat, plateau,robot,gardiens
    robot_placement()
    print_plateau()
    #game 1
    while len(chat) != 0:
        move_chat(chat,plateau,score_A,conversion,what_square)
        move_gardiens(gardiens,chat,plateau)
        move_robot(robot,plateau)
    #game 2
    plateau = plateau_initial[:]
    chat = [(11,4),(11,5),(11,6),(11,7),(11,8),(10,4),(10,5),(10,6),(10,7),(10,8),(9,5),(9,6),(9,7),(8,6)]
    gardiens = [(2,3),(2,9)]
    robot=[]
    robot_placement()
    while len(chat) != 0:
        move_chat(chat,plateau,score_B,conversion,what_square)
        move_gardiens(gardiens,chat,plateau)
        move_robot(robot,plateau)
    if score_A > score_B:
        print("Le joueur A a gagné")
    elif score_A < score_B:
        print("Le joueur B a gagné")
    else:
        print("EGALITE")
def menu() :
    print("Entrer le nom du joueur 1 :")
    nom_j1 = str(input())
    print("Entrer le nom du joueur 2 :")
    nom_j2 = str(input())
    print(nom_j1, nom_j2)
    print("1 : Lancer la partie" \
          "2 : Règles du jeu"\
          "Sélectioner 1 ou 2")
    nb = int(input())
    while nb != 1 or nb != 2 :
        print("Selectioner 1 ou 2")
    if nb == 2 :
        print("Le jeu EsCATe Game se joue à deux joueurs, sur un plateau carré de 11x11 cases," 
        "qui représente une pension pour chats. L’un des joueurs contrôle un groupe de" \
        "quatorze chats qui essaient de s’évader. L’autre joueur contrôle deux gardiens qui" \
        "tentent de capturer les chats avant leur fuite."
        "Il existe trois types d’acteurs dans ce jeu, les chats, les gardiens, et des robots " \
        "aspirateur autonomes, activés par les gardiens pour effrayer les chats:"
                    "- Le groupe de chats est composé de quatorze chats. Chaque chat"
                    "occupe une case du plateau. Ils commencent la partie dans une zone"
                    "qui leur est réservée (voir Figure 1)."
                    "- Les deux gardiens occupent chacun une case. Ils commencent"
                    "toujours la partie en position (2, C) et (2, I) du plateau en Figure 1."
                    "- Neuf robots aspirateur autonomes ont été activés par les gardiens."
                    "Chaque robot occupe une case et forme un obstacle infranchissable"
                    "pour les chats. Ils commencent la partie sur neuf cases tirées"
                    "aléatoirement."
                    "Le plateau est illustré par la Figure 2. Il est composé de 11x11 cases et comporte deux " \
                    "zones spéciales et trois sorties réparties comme suit :"
                    "- Une zone où le groupe de chats débute la partie. Cette zone fait " \
                    "quatorze cases et se situe au centre, en bas du plateau. " \
                    "Les gardiens et les robot aspirateur ne peuvent pas y pénétrer."\
                    "- Une zone centrale qui représente un bassin d’eau infranchissable "\
                    "pour les chats, les gardiens, et les robots aspirateur. Ce bassin est" \
                    " rectangulaire et s’étale sur six cases au total. " \
                    "Il est représenté par six ’O’ dans la Figure 1."
                    "- Trois sorties sont disposées en position (1, F ), (5, A), et (5, K) " \
                    "du plateau en Figure 1, représentées par trois ’S’. Une sortie occupe une" \
                    "case. Un chat s’évade lorsqu’il se positionne sur une case sortie. Les " \
                    "gardiens et les robots ne peuvent pas se positionner sur une sortie."
        "Sur le plateau, chaque acteur (chat, gardien, robot) se déplace au maximum d’une " \
        "case par tour, à l’horizontale, à la verticale, ou en diagonale (pas de déplacement en" \
        "diagonale pour les robots)."
        
        "Les déplacements spécifiques sont les suivants :  "
            "- Un chat s’évade en se déplaçant sur une case sortie, et il disparaît directement du plateau."
            "- Un gardien capture un chat lorsqu’il se déplace sur la case occupé par cechat."
            "- Seuls les gardiens peuvent sauter par-dessus un robot aspirateur : lors " \
            "d’un déplacement, les gardiens peuvent choisir une case occupée" \
            "par un robot ; ils se retrouvent alors sur la case à l’opposée du robot."
            "- Le bassin d’eau est infranchissable pour les chats, les gardiens, et les robots " \
            "  aspirateur"
        "Un tour de jeu est décomposé en trois phases : " \
            "Phase ‘chats’ : Le joueur contrôlant les chats en déplace sept, ceux de son choix"
                ".Un chat ne peut être déplacé qu’une fois par tour." \
            "Phase ‘gardiens’ : L’autre joueur déplace les deux gardiens. " \
                "Un gardien ne peutêtre déplacé qu’une fois par tour." \
            "Phase ‘robots’ : Les robots sont autonomes. A chaque tour, chaque robot a une" \
                "chance sur trois de bouger. Il se déplace alors d’une case dans une directionaléatoire," \
                "horizontale ou verticale."

        "Une manche se termine lorsqu’il ne reste plus de chats sur le plateau, c’est-à-dire que " \
        "chaque chat s’est évadé ou a été capturé par les gardiens avant sa fuite."

        "A la fin d’une manche, le joueur contrôlant les chats gagne un point pour chaque chat qui s’est évadé. " \
        "Le joueur contrôlant les gardiens ne gagne pas de points. Le rôle de chaque joueur est inversé pour la manche suivante. " \
        "Une partie compte deux manches."
        "Lorsque la partie est terminée, le gagnant est le joueur possédant le plus de points.")
    else :
        print(nom_j1, nom_j2, "Que le/la meilleur(e) gagne.")

main()

