def solve_sudoku_puzzle(board):
    result = []

    def condition_violated(i,j):
        for dx, dy in [(1,0), (-1,0), (0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
            if board[i+dx][i+dy] == board[i][j]:
                return True
            for i in range(9):
                if board[i][0] == board[i][j]:
                    return True
            for j in range(9):
                if board[0][j] == board[i][j]:
                    return True

    def helper(i, j):
        # base
        if i == 9:
            result = board[:][:]
            return

        # if condition_violated(i, j):
        #     return

        # recursive
        for num in range(1, 10):
            for k in range(9):
                for l in range(9):
                    if board[k][l] == 0:
                        board[i][j] = num
                        helper(0, 0)
                    # [i][j] = 0

    helper(0, 0)

    return result

print(solve_sudoku_puzzle([

[8, 4, 9, 0, 0, 3, 5, 7, 0],

[0, 1, 0, 0, 0, 0, 0, 0, 0],

[7, 0, 0, 0, 9, 0, 0, 8, 3],

[0, 0, 0, 9, 4, 6, 7, 0, 0],

[0, 8, 0, 0, 5, 0, 0, 4, 0],

[0, 0, 6, 8, 7, 2, 0, 0, 0],

[5, 7, 0, 0, 1, 0, 0, 0, 4],

[0, 0, 0, 0, 0, 0, 0, 1, 0],

[0, 2, 1, 7, 0, 0, 8, 6, 5]

]))

