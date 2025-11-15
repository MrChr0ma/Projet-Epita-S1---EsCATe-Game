import random as rd
import subprocess

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
    subprocess.run('clear', shell = True)
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
def move_chat(): # A Hector
    return





#verifie que l'utilisateur bouge les 2 gardiens
#demande le gardiens à bouger et la case choisi
#appelle what_square() pour savoir si la case est valide
#si elle est valide effectuer le mouvement
#et demande le deuxieme gardien
#!ATTENTION prendre en compte les chat(si on le mange il faut le retirer de la liste)(et ils peuvent sauter par dessus les robot donc rajouter 1 de range)
def move_gardiens(): # A Florentin
    return



#calculer une proba de 1/3
#si 1 alors appeller what_square()
#effectuer un mvt aleatoire parmi ceux retourner par what_square()
def move_robot(): # A Enzo
    return




#La fonction prend en entrée la case de la piece etudié et son type : "chat","gardien" ou "robot" 
#Elle retourne la liste des cases diponibles pour un deplacement autour
#Elle est appelée dans les fonctions move_robot, move_chat et move_gardien
def what_square(case :tuple,types:str)->list: # A Gaël
    liste_case_disp = []
    x,y = case
    if types == "chat":
        for i in range(-1 if x > 1 else 0,2 if x < 11 else 1):
            for j in range(-1 if y > 1 else 0, 2 if y < 11 else 1):
                if plateau[x+i][y+j] == "." or plateau[x+i][y+j] == "S":
                    liste_case_disp.append((x+i,y+j))
    elif types == "gardien":
        for i in range(-1 if x > 1 else 0,2 if x < 11 else 1):
            for j in range(-1 if y > 1 else 0, 2 if y < 11 else 1):
                if plateau[x+i][y+j] == "." or plateau[x+i][y+j] == "C" or plateau[x+i][y+j] == "R":
                    liste_case_disp.append((x+i,y+j))
    elif types == "robot":
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
def conversion(): # A Hector
    return

def main():
    robot_placement()
    print_plateau()
main()
