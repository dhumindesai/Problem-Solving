from collections import deque

import math


class Node:
    def __init__(self, id):
        self.id = id
        self.adjacent = []


'''
TODO:
improve the algorithm when edges are not directed
'''
def connectedSum(n, edges):
    nodeMap = {}
    for id in range(1, n + 1):
        nodeMap[id] = Node(id)

    for edge in edges:
        first = nodeMap[edge[0]]
        second = nodeMap[edge[1]]
        first.adjacent.append(second)

    result = 0
    visited = set()

    for node in nodeMap.values():
        if node.adjacent and node.id not in visited:
            result += math.ceil(math.sqrt(dfs_sum(node, visited)))

    for node in nodeMap.values():
        if node.id not in visited:
            result += 1

    return result



def dfs_sum(root, visited):
    sum = 0
    visited.add(root.id)

    queue = deque()
    queue.append(root)

    while queue:
        lastNode = queue.popleft()
        visited.add(lastNode.id)
        sum += 1
        for child in lastNode.adjacent:
            queue.append(child)

    return sum

def main():

    print(connectedSum(4, [[1, 2], [1, 4]]))
    print(connectedSum(8, [[8, 1], [5, 8], [7, 3], [8, 6]]))
    print(connectedSum(4, [[1, 2], [1, 4], [3, 1]]))  # 2

main()



