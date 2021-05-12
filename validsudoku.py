def isValidSudoku(board):
    def validRow(i):
        seen = set()
        for t in board[i]:
            if t != '.' and t in seen: return False
            seen.add(t)
        return True

    def validCol(j):
        seen = set()
        for i in range(len(board)):
            t = board[i][j]
            if t != '.' and t in seen: return False
            seen.add(t)
        return True

    def validSection(s):
        a, b = s//3, s%3
        seen = set()
        for i in range(3):
            for j in range(3):
                cur = board[a*3+i][b*3+j]
                if cur != "." and cur in seen: return False
                else: seen.add(cur)
        return True

    def validColumns():
        for i in range(len(board)):
            if not validRow(i): return False
        return True

    def validRows():
        for j in range(len(board[0])):
            if not validCol(j): return False
        return True

    def validSubsections():
        for s in range(9):
            if not validSection(s): return False
        return True

    return validColumns() and validRows() and validSubsections()

if __name__ == "__main__":
    board = \
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    board2 = \
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    board3 = \
        [[".",".","4",".",".",".","6","3","."]
        ,[".",".",".",".",".",".",".",".","."]
        ,["5",".",".",".",".",".",".","9","."]
        ,[".",".",".","5","6",".",".",".","."]
        ,["4",".","3",".",".",".",".",".","1"]
        ,[".",".",".","7",".",".",".",".","."]
        ,[".",".",".","5",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]]
    assert isValidSudoku(board) == True
    assert isValidSudoku(board2) == False
    assert isValidSudoku(board3) == False
    print("Tests passed 3/3")

