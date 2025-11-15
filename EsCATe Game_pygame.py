import pygame
import random as rd
pygame.init()
WIDTH,HEIGHT,NB_SQUARE= 1375,720,12
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EsCATe Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (56,93,56)
LIGHT_YELLOW = (255, 255, 150)
LIGHT_ORANGE = (255,129,0)
SQUARE_SIZE = 60
BOARD_Y , BOARD_X = 0,330
image_chat = pygame.image.load("Desktop\Projet EPITA semestre 1\chat.jpg")
image_gardien = pygame.image.load("Desktop\Projet EPITA semestre 1\gardien.jpg")
image_robot = pygame.image.load("Desktop\Projet EPITA semestre 1\Robot.gif")
image_sorti =  pygame.image.load("Desktop\Projet EPITA semestre 1\sortie.png")
image_bassin = pygame.image.load("Desktop\Projet EPITA semestre 1\Bassin.jpg")
image_chat = pygame.transform.scale(image_chat, (SQUARE_SIZE-10 , SQUARE_SIZE-10 ))
image_gardien = pygame.transform.scale(image_gardien, (SQUARE_SIZE -10, SQUARE_SIZE-10 ))
image_robot = pygame.transform.scale(image_robot, (SQUARE_SIZE-10 , SQUARE_SIZE-10 ))
image_sorti = pygame.transform.scale(image_sorti, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
image_bassin = pygame.transform.scale(image_bassin, (2*(SQUARE_SIZE), 3*(SQUARE_SIZE)))
A  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\A.jpg")
B  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\B.jpg")
C  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\C.jpg")
D  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\D.jpg")
E  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\E.jpg")
F  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\F.jpg")
G  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\G.jpg")
H  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\H.jpg")
I  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\I.jpg")
J  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\J.jpg")
K  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\K.jpg")
A = pygame.transform.scale(A, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
B = pygame.transform.scale(B, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
C = pygame.transform.scale(C, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
D = pygame.transform.scale(D, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
E = pygame.transform.scale(E, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
F = pygame.transform.scale(F, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
G = pygame.transform.scale(G, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
H = pygame.transform.scale(H, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
I = pygame.transform.scale(I, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
J = pygame.transform.scale(J, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
K = pygame.transform.scale(K, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
image_chat = pygame.image.load("Desktop\Projet EPITA semestre 1\chat.jpg")
image_gardien = pygame.image.load("Desktop\Projet EPITA semestre 1\gardien.jpg")
image_robot = pygame.image.load("Desktop\Projet EPITA semestre 1\Robot.gif")
image_sorti =  pygame.image.load("Desktop\Projet EPITA semestre 1\sortie.png")
image_bassin = pygame.image.load("Desktop\Projet EPITA semestre 1\Bassin.jpg")
image_chat = pygame.transform.scale(image_chat, (SQUARE_SIZE-10 , SQUARE_SIZE-10 ))
image_gardien = pygame.transform.scale(image_gardien, (SQUARE_SIZE -10, SQUARE_SIZE-10 ))
image_robot = pygame.transform.scale(image_robot, (SQUARE_SIZE-10 , SQUARE_SIZE-10 ))
image_sorti = pygame.transform.scale(image_sorti, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
image_bassin = pygame.transform.scale(image_bassin, (2*(SQUARE_SIZE), 3*(SQUARE_SIZE)))
image_bassin = pygame.transform.rotate(image_bassin, -90)
image_1  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\image_1.png")
image_2  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\image_2.png")
image_3  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\image_3.png")
image_4  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\image_4.png")
image_5  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\image_5.png")
image_6  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\image_6.png")
image_7  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\image_7.png")
image_8  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\image_8.png")
image_9  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\image_9.png")
image_10  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\image_10.png")
image_11  = pygame.image.load("Desktop\Projet EPITA semestre 1\coordonnes image\image_11.png")
img_fond_plateau = pygame.image.load("Desktop\Projet EPITA semestre 1\Fond_plateau.jpg")
image_1 = pygame.transform.scale(image_1, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
image_2 = pygame.transform.scale(image_2, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
image_3 = pygame.transform.scale(image_3, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
image_4 = pygame.transform.scale(image_4, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
image_5 = pygame.transform.scale(image_5, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
image_6 = pygame.transform.scale(image_6, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
image_7= pygame.transform.scale(image_7, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
image_8 = pygame.transform.scale(image_8, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
image_9 = pygame.transform.scale(image_9, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
image_10 = pygame.transform.scale(image_10, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
image_11 = pygame.transform.scale(image_11, (SQUARE_SIZE-10, SQUARE_SIZE-10 ))
img_fond_plateau =  pygame.transform.scale(img_fond_plateau, ((SQUARE_SIZE-1)*NB_SQUARE,(SQUARE_SIZE-1)*NB_SQUARE ))
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
current_turn = 'C'
selected_piece = (None,None) #-> tuple (case,types) avec case (x,y) donc un tuple aussi
valid_move_position = []
def robot_placement():
    while len(robot) != 9:
        coordonnées = (rd.randint(1,11),rd.randint(1,11))
        if coordonnées not in chat and coordonnées not in gardiens and coordonnées not in sortie and coordonnées not in robot and coordonnées not in bassin :
            robot.append(coordonnées)
    for (x,y) in robot:
        plateau[x][y] = "R"
def draw_board():
    screen.blit(img_fond_plateau,(BOARD_X+SQUARE_SIZE, BOARD_Y+SQUARE_SIZE))
    for i in range(1,12):
        for j in range(1,12):
            square_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            pygame.draw.rect(screen,BLACK,(BOARD_X+SQUARE_SIZE*i,BOARD_Y+SQUARE_SIZE*j,SQUARE_SIZE,SQUARE_SIZE),1)

            if (j,i) in valid_move_position:
                square_surface.fill((*LIGHT_YELLOW, 128))
                screen.blit(square_surface, (BOARD_X + i * SQUARE_SIZE, BOARD_Y + j * SQUARE_SIZE))
    liste =[A,B,C,D,E,F,G,H,I,J,K]
    j =1
    for lettre in liste:
        screen.blit(lettre,(BOARD_X+SQUARE_SIZE*j+5,BOARD_Y))
        j += 1
    liste_nb = [image_1,image_2,image_3,image_4,image_5,image_6,image_7,image_8,image_9,image_10,image_11]
    i = 1
    for nb in liste_nb:
        screen.blit(nb,(BOARD_X,BOARD_Y+SQUARE_SIZE*i+5))
        i +=1
def draw_piece():
    global selected_piece
    for i in range(1,len(plateau)):
        for j in range(1,len(plateau[i])):
            if plateau[j][i] == "W":
                screen.blit(image_gardien,(BOARD_X+SQUARE_SIZE*i+5,BOARD_Y+SQUARE_SIZE*j+5))
            elif plateau[j][i] == "C":
                screen.blit(image_chat,(BOARD_X+SQUARE_SIZE*i+5,BOARD_Y+SQUARE_SIZE*j+5))
            elif plateau[j][i] == "R":
                screen.blit(image_robot,(BOARD_X+SQUARE_SIZE*i+5,BOARD_Y+SQUARE_SIZE*j+5))
            elif plateau[j][i] == "S":
                screen.blit(image_sorti,(BOARD_X+SQUARE_SIZE*i+5,BOARD_Y+SQUARE_SIZE*j+5))
            elif j==3 and i == 5:
                screen.blit(image_bassin,(BOARD_X+SQUARE_SIZE*i,BOARD_Y+SQUARE_SIZE*j))
            if (j,i) == selected_piece[0]:
                pygame.draw.circle(screen,YELLOW,((i+1/2)*SQUARE_SIZE+BOARD_X,(j+1/2)*SQUARE_SIZE),SQUARE_SIZE//2-2,3)
def select_piece(pos):
    global selected_piece,current_turn,valid_move_position
    x,y = pos
    x -= BOARD_X
    x,y = x//SQUARE_SIZE,y//SQUARE_SIZE
    if (0 < x <= 11 and 0 < y <= 11) and not(5 <= x <= 7 and 3 <= y <= 4):
        if plateau[y][x] == 'R' and current_turn == 'R' :
            selected_piece = ((y,x),'R')
            valid_move_position = what_square(selected_piece[0],selected_piece[1])
            return
        elif plateau[y][x] == 'W' and current_turn == 'W':
            selected_piece =((y,x),'W')
            valid_move_position = what_square(selected_piece[0],selected_piece[1])
            return
        elif plateau[y][x] == 'C' and current_turn == 'C':
            selected_piece = ((y,x),'C')
            valid_move_position = what_square(selected_piece[0],selected_piece[1])
            return
        selected_piece = (None,None)
        valid_move_position = []
def what_square(case :tuple,types:str)->list:
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
def main():
    screen.fill(WHITE)
    robot_placement()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                select_piece(event.pos)
        draw_board()
        draw_piece()
        pygame.display.flip()
main()
