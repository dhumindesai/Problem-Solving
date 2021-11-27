def isValidSudoku(board):

    # check rows
    for i in range(9):
        visited = set()
        for j in range(9):
            if board[i][j] != ".":
                if board[i][j] in visited:
                    return False
                else:
                    visited.add(board[i][j])
    # check rows
    for j in range(9):
        visited = set()
        for i in range(9):
            if board[i][j] != ".":
                if board[i][j] in visited:
                    return False
                else:
                    visited.add(board[i][j])

    # check 3x3 blocks
    block_start = [[0, 0], [0, 3], [0, 6],
                   [3, 0], [3, 3], [3, 6],
                   [6, 0], [6, 3], [6, 6],
                   ]

    for r, c in block_start:
        visited = set()
        for i in range(3):
            for j in range(3):
                if board[r + i][c + j] != ".":
                    if board[r+i][c+j] in visited:
                        return False
                    else:
                        visited.add(board[r+i][c+j])

    return True

board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
print(isValidSudoku(board))