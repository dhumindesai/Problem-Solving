# In a given 2D binary array grid, 0s represent water and 1s represent islands. (An island is a 4-directionally connected group of 1s not connected to any other 1s.)
# An assumption you can make is, the grid will have exactly two islands. Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
# Return the smallest number of 0s that must be flipped to form one large island.

# Example:

# Input: 
'''
 0 0 0 1 1
 1 1 0 1 0
 0 0 0 0 0

 0 0 0 2 2
 3 3 0 2 0
 0 0 0 0 0

 q = [0,2,2]
 d = 1

 => set -> [("0,3"), (0,4), (1,3)]
 => set -> [(1,0), (1,1)]
 '''
from collections import deque


def min_path_between_islands(grid):
    def get_neighbors(x, y):
        neighbors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            new_r = x + dr
            new_c = y + dc
            if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == 1:
                neighbors.append((new_r, new_c))

        return neighbors

    def get_all_neighbors(x, y):
        neighbors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            new_r = x + dr
            new_c = y + dc
            if 0 <= new_r < m and 0 <= new_c < n:
                neighbors.append((new_r, new_c))

        return neighbors

    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q:
            x1, y1 = q.popleft()
            for nx, ny in get_all_neighbors(x1, y1):
                if visited[nx][ny] == 3:
                    visited[nx][ny] = component[0]

    def bfs_path(x, y):
        distance = 0
        q = deque()
        q.append((x, y))

        while q:
            distance += 1
            x1, y1 = q.popleft()
            for nx, ny in get_neighbors(x1, y1):
                if visited[nx][ny] == 3:
                    distance += 1
                    return distance
            q.append((nx, ny))

    m = len(grid)
    n = len(grid[0])

    visited = [[-1 for _ in range(n)] for _ in range(m)]

    component = [2]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                bfs(i, j)
                component += 1


    result = float("inf")
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 2:
                result = min(bfs_path(i, j), result)

    return result



