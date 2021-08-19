def spiralOrder(matrix):
    result = []

    top = 0
    down = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    dir = 0

    while top <= down and left <= right:
        if dir == 0:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

        elif dir == 1:
            for i in range(top, down + 1):
                result.append(matrix[i][right])
            right -= 1

        elif dir == 2:
            for j in range(right, left - 1, -1):
                result.append(matrix[down][j])
            down -= 1

        elif dir == 3:
            for i in range(down, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        dir += 1
        dir = dir % 4

    return result

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))