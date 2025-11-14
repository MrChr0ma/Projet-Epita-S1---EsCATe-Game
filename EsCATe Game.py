import random as rd

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
def print_plateau():
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
def move_chat():
    return
def move_gardiens():
    return
def move_robot():
    return
def main():
    robot_placement()
    print_plateau()
main()
        



