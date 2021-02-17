class Node:
    def __init__(self, id):
        self.id = id
        self.adjacent = []

def has_path_dfs(src, dest, visited = set()):
    if src.id in visited:
        return False

    print(src.id)
    visited.add(src.id)
    if src.id == dest.id:
        return True

    for child in src.adjacent:
        if has_path_dfs(child, dest, visited):
            return True

    return False



def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.adjacent = [n2, n3]
    n2.adjacent = [n6]
    n3.adjacent = [n4]
    n4.adjacent = [n5]

    print(has_path_dfs(n1, n5))
    print(has_path_dfs(n2, n5))

main()



