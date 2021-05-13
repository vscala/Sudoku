def safeMove(board, x, y, val):
    #Check rows
    for i in range(9):
        if i == x: continue
        if board[i][y] == val: return False
    #Check columns
    for j in range(9):
        if j == y: continue
        if board[x][j] == val: return False
    #Check subgrid
    a, b  = (x//3)*3, (y//3)*3
    for i in range(3):
        for j in range(3):
            if x == a+i and y == b+j: continue
            if board[a+i][b+j] == val: return False
    return True

def solveBoard(board, x=0, y=0):
    #Get next tile
    if x >= 9: 
        y+=1
        x=0
    if y >= 9: return board
    while board[x][y] != '.':
        x+=1
        if x >= 9: 
            y+=1
            x=0
        if y >= 9: return board
    
    #Attempt to fill next tile with 1-9
    for v in range(1,10):
        v = str(v)
        #If safe continue
        if safeMove(board, x, y, v):
            board[x][y] = v
            newBoard = solveBoard(board, x+1, y)
            if newBoard:
                return newBoard
            board[x][y] = '.' #Valid but not correct
    return False #No solutions for given tree
    
if __name__ == "__main__":
    board = \
        [["1",".",".",".",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]]
    out = solveBoard(board)
    if out: print(*out, sep = "\n")
    else: print("No solution")
    
                    
