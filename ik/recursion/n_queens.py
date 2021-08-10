def find_all_arrangements(n):
    result = []
    col_occupied = [False for _ in range(n)]
    slash_occupied = [False for _ in range(2*n-1)]
    backslash_occupied = [False for _ in range(2*n-1)]

    def isConflict(i, j):
        return col_occupied[j] or slash_occupied[i+j] or backslash_occupied[i-j+n-1]

    def getPositions(placements):
        positions = []
        for x in range(len(placements)):
            positions.append([x, placements[x]])
        return positions

    def format_result(combos):
        formatted = []
        for result in combos:
            format = [["-" for _ in range(n)] for _ in range(n)]
            for i,j in result:
                format[i][j] = "q"
            formatted.append([''.join(row) for row in format])
        return formatted

    def helper(i, placements):

        if i == n:
            result.append(getPositions(placements))
            return

        for j in range(n):
            if not isConflict(i, j):
                placements.append(j)
                col_occupied[j] = True
                slash_occupied[i+j] = True
                backslash_occupied[i-j+n-1] = True
                helper(i + 1, placements)
                col_occupied[j] = False
                slash_occupied[i + j] = False
                backslash_occupied[i - j + n - 1] = False
                placements.pop()

    helper(0, [])

    return format_result(result)

print(len(find_all_arrangements(8)))