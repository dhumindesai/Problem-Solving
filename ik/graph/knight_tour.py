from collections import deque


def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    # if start_row == end_row and start_col == end_col:
    #     return 0

    # def is_valid(a, b):
    #     if 0 <= a < rows and 0 <= b < cols:
    #         return True
    #
    # def get_neighbor(cell):
    #     i = cell[0]
    #     j = cell[1]
    #     result = []
    #
    #     if is_valid(i + 2, j +1 ):
    #         result.append((i + 2, j + 1))
    #     if is_valid(i + 2, j - 1):
    #         result.append((i + 2, j - 1))
    #     if is_valid(i - 2, j + 1):
    #         result.append((i - 2, j + 1))
    #     if is_valid(i - 2, j - 1):
    #         result.append((i - 2, j - 1))
    #     if is_valid(j + 2, i + 1):
    #         result.append((j + 2, i + 1))
    #     if is_valid(j + 2, i - 1):
    #         result.append((j + 2, i - 1))
    #     if is_valid(j - 2, i + 1):
    #         result.append((j - 2, i + 1))
    #     if is_valid(j - 2, i - 1):
    #         result.append((j - 2, i - 1))
    #     return result
    DIRECTIONS = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    def get_neighbors(cell):
        r = cell[0]
        c = cell[1]
        neighbors = []
        for dr, dc in DIRECTIONS:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < rows and 0 <= new_c < cols:
                neighbors.append((new_r, new_c))

        return neighbors

    visited = [[-1 for _ in range(cols)] for _ in range(rows)]
    q = deque()
    q.append((start_row, start_col))
    visited[start_row][start_col] = 0

    while q:
        cell = q.popleft()
        if end_row == cell[0] and end_col == cell[1]:
            return visited[cell[0]][cell[1]]
        for neighbor in get_neighbors(cell):
            x, y = neighbor[0], neighbor[1]
            if visited[x][y] == -1:
                visited[x][y] = visited[cell[0]][cell[1]] + 1
                q.append((x, y))

    return -1

print(find_minimum_number_of_moves(5, 5, 0, 0, 4, 1))
print(find_minimum_number_of_moves(2, 7, 0, 5, 1, 1))
print(find_minimum_number_of_moves(3, 8, 0, 6, 1, 3))