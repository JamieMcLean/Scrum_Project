def showGrid():
    board = []
    for i in range(9):
        board.append([])
        for x in range(9):
            board[i].append('+')

    for row in board:
        print (" ".join(row))

showGrid()


            
