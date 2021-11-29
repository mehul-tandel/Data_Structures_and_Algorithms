def createBoard(n):
    board = [[True]*n for i in range(n)]
    return board

def isSafe(board,r,c):
    for i in range(r):
        if board[i][c] == False :
            return False
    for i in range(1,min(r,c)+1):
        if board[r-i][c-i] == False :
            return False
    for i in range(1,min(r,len(board)-1-c)+1) :
        if board[r-i][c+i] == False :
            return False
    return True

def displayQueens(board):
    for row in board:
        for ele in row:
            if ele == False:
                print("Q",end='')
            else:
                print("X",end='')
        print("\n")

def configure(board,r):
    if r == len(board):
        displayQueens(board)
        return 1
    count = 0
    for c in range(len(board)):
        if isSafe(board,r,c) :
            board[r][c] = False
            count += configure(board,r+1)
            board[r][c] = True
    return count

board = createBoard(5)
print(configure(board,0))