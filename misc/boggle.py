"""

Boggle

2d board of letters, and try to form words with those letters

board = [[ A, C, E],
         [ F, I, N],
         [ I, F, U]]

word = ACE # True
word = FINE # True
word = ZEBRA # False
word = FIFA # False
word = ACENIFIPUD

boolean output, can we find this word in the board?


form words, by going up down left right, and cannot reuse letters in the same word

"""

# 1. find a first letter in the 2d board ==> (1,0), (2,1)

# 2. Bfs from the first node and keep iterate over the given word
# mark the letter visited if matching with current char


# 3.if there is no more char to visit return True,
from collections import deque


def form_word(board, word):
    def bfs(l, first):
        q = deque()
        visited[first[0]][first[1]] = True
        q.append((first[0], first[1]))

        while q:
            node = q.popleft()
            x = node[0]
            y = node[1]

            if l >= len(word):
                return True

            for x1, y1 in get_neighbors(x, y):
                if l < len(word) and  not visited[x1][y1] and word[l] == board[x1][y1]:
                    visited[x1][y1] = True
                    q.append((x1, y1))
                    l += 1

        return False

    def get_neighbors(i, j):
        result = []

        # left
        if j > 0:
            result.append((i, j - 1))

        # right
        if j < n - 1:
            result.append((i, j + 1))

        # up
        if i > 0:
            result.append((i - 1, j))

        # down
        if i < m - 1:
            result.append((i + 1, j))

        return result

    def find_first(board, c):
        result = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == c:
                    result.append((i, j))

        return result

    m = len(board)
    n = len(board[0])

    # Find first letter
    firsts = find_first(board, word[0])  # (1,0)
    if not firsts:
        return False

    # perforn bfs from that letter
    found = False
    for first in firsts:
        visited = [[False for _ in range(n)] for _ in range(m)]
        if found:
            return True
        found = bfs(1, first)

    return found

print(form_word([[ 'A', 'C', 'E'],
         [ 'F', 'I', 'N'],
         [ 'I', 'F', 'U']], "ZEBRA"))