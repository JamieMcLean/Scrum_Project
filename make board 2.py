import random

def showGrid():
    board = []
    for i in range(9):
        board.append([])
        for x in range(9):
            board[i].append('+')
    for row in board:
        print (" ".join(row))

def bombBoard():
    bombGrid = []
    for i in range(9):
        bombGrid.append([])
        for x in range(9):
            bombGrid[i].append('@')
            bombGrid[i].append('+')
            bombGrid[i].append('+')
            bombGrid[i].append('+')
            randGrid = print(random.choice(bombGrid))
            randGrid()
    for row in bombGrid:
        print("".join(row))

bombBoard()
        
        
        




            
