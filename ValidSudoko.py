"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""

# My solution

board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]

def isvaldSudoku(board):

    # Checks the rows
    rows = [[] for _ in range(9)]
    for i in range(9):
        rows[i].extend(board[i])
        rows[i] = [int(num) for num in rows[i] if num!="."]

        if len(rows[i]) != len(set(rows[i])):
            return False
        
    # Checks the columns
    cols = [[] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            cols[i].append(board[j][i])
    for k in range(9):
        cols[k] = [int(num) for num in cols[k] if num!="."]
        if len(cols[k]) != len(set(cols[k])):
            return False
        
    # Checks the 3x3 squares
    squares = [[] for _ in range(9)]

    for l in range(9):
        for m in range(9):
            squares[(l//3)*3 + m//3].append(board[l][m])
    for p in range(9):
        squares[p] = [int(num) for num in squares[p] if num!="."]
        if len(squares[p]) != len(set(squares[p])):
            return False
    return True

print(isvaldSudoku(board))
