import random as rd
import subprocess
import platform

plateau = [["  ","A","B","C","D","E","F","G","H","I","J","K"],
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
gardiens = [(2,3),(2,9)]
sortie = [(1,6),(5,1),(5,11)]
robot = []
bassin = [(3,5),(3,6),(3,7),(4,5),(4,6),(4,7)]
score_A ,score_B = 0,0

def print_plateau():
    subprocess.run('cls', shell = True)
    for ligne in plateau:
        for case in ligne:
            print(case,end = " ")
        print("")
               
def robot_placement():
    while len(robot) != 9:
        coordonnées = (rd.randint(1,11),rd.randint(1,11))
        if coordonnées not in chat and coordonnées not in gardiens and coordonnées not in sortie and coordonnées not in robot and coordonnées not in bassin :
            robot.append(coordonnées)
    for (x,y) in robot:
        plateau[x][y] = "R"
               
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
        print(f"{RED} FERREUR : {msg}{RESET}")
        print(f"{RED}!{RESET}"*50 + "\n")

    # -----------------#
    #  Clear terminal  #
    # -----------------#
    def clear_terminal():
        if platform.system() == "Windows":
            subprocess.run('cls', shell=True)
        else:
            subprocess.run('clear', shell=True)

    sorties = [(1, 6), (5, 1), (5, 11)]
    nb_chats_a_bouger = min(7, len(chat))

    if len(chat) == 0:
        print("Il n'y a plus de chats sur le plateau !")
        return chat, score

    print("\n=== PHASE CHATS ===")
    print(f"Vous devez déplacer {nb_chats_a_bouger} chat(s).")
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
            print("Chats disponibles :")
            for c in chats_non_deplaces:
                ligne, col = c
                lettre = plateau[0][col]
                print(f"  - {lettre}{ligne}")

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
            cases_possibles = what_square(chat_a_bouger, "C")

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
                            print(f"Score : {score} chat(s) évadé(s)\n")

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
    print(f"Score actuel : {score} chat(s) évadé(s)")

    return chat, score
           
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
           print(f"\n=== PHASE GARDIENS ===")
    for x,y in gardiens:
        plateau[x][y]="."

    choice=int(input("Entrer le gardien que vous souhaitez déplacer 0 ou 1: "))
    first_choice=choice
    second_choice=1-first_choice
    chat_capture=0

    while True:
        choose_case=input("entrer la case ou va le premier gardien: ")
        case=conversion(choose_case)
        posx,posy=gardiens[first_choice]
        x,y=case

        if plateau[x][y]=="R":
            saut_x=x-posx
            saut_y=y-posy
            new_x=x+saut_x
            new_y=y+saut_y
            case=(new_x,new_y)

        if plateau[x][y]=="C":
            if (x,y) in chat:
                chat.remove((x,y))
                chat_capture+=1
                       
        case_dispo= what_square(gardiens[first_choice],"W")
        if case not in case_dispo:
            case_dispo.append(case)
        if case in case_dispo:
            break
        print("case invalide, nouvelle case: ")
    gardiens[first_choice]= case
    while True:
        choose_case=input("Entrer une case ou va le second gardien: ")
        case=conversion(choose_case)
        posx,posy=gardiens[second_choice]
        x,y=case

        if plateau[x][y]=="R":
            saut_x=x-posx
            saut_y=y-posy
            new_x=x+saut_x
            new_y=y+saut_y
            case=(new_x,new_y)

        if plateau[x][y]=="C":
            if (x,y) in chat:
                chat.remove((x,y))
                chat_capture+=1

        case_dispo= what_square(gardiens[second_choice],"W")
        if case not in case_dispo:
            case_dispo.append(case)
        if case in case_dispo:
            break
        print("case invalide, nouvelle case: ")
    gardiens[second_choice]= case

    for x,y in gardiens:
        plateau[x][y]="W"

    print_plateau()

    print(f"\n=== FIN PHASE GARDIENS ===")
    print(f" {chat_capture} chat(s) capturé(s)")
    return gardiens

#calculer une proba de 1/3
#si 1 alors appeller what_square()
#effectuer un mvt aleatoire parmi ceux retourner par what_square()
def move_robot(robot,chat,plateau): # A Enzo
        for x,y in robot :
            peut_bouger = rd.randint(1,3)
            if peut_bouger == 1 :
                case_dispo = what_square((x,y), "R")
                nouvelle_coordonne_x, nouvelle_coordonne_y = rd.choice(case_dispo)
                plateau[x][y] = "."
                plateau[nouvelle_coordonne_x][nouvelle_coordonne_y] = "R"
                indice = robot.index((x,y))
                robot[indice] = (nouvelle_cordonne_x, nouvelle_cordonney)
           return




#La fonction prend en entrée la case de la piece etudié et son type : "chat","gardien" ou "robot" 
#Elle retourne la liste des cases diponibles pour un deplacement autour
#Elle est appelée dans les fonctions move_robot, move_chat et move_gardien
def what_square(case :tuple,types:str)->list: # A Gaël
    liste_case_disp = []
    x,y = case
    if types == "C":
        for i in range(-1 if x > 1 else 0,2 if x < 11 else 1):
            for j in range(-1 if y > 1 else 0, 2 if y < 11 else 1):
                if plateau[x+i][y+j] == "." or plateau[x+i][y+j] == "S":
                    liste_case_disp.append((x+i,y+j))
    elif types == "W":
        for i in range(-1 if x > 1 else 0,2 if x < 11 else 1):
            for j in range(-1 if y > 1 else 0, 2 if y < 11 else 1):
                if plateau[x+i][y+j] == "." or plateau[x+i][y+j] == "C" or plateau[x+i][y+j] == "R":
                    liste_case_disp.append((x+i,y+j))
    elif types == "R":
        if plateau[x+1 if x < 11 else 0][y] == ".":
            liste_case_disp.append((x+1,y))
        if plateau[x-1][y] == ".":
            liste_case_disp.append((x-1,y))
        if plateau[x][y+1 if y < 11 else 0] == ".":
            liste_case_disp.append((x,y+1))
        if plateau[x][y-1] == ".":
            liste_case_disp.append((x,y-1))
    return liste_case_disp

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

def main():
    robot_placement()
    print_plateau()
main()













