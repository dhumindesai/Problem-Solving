def solution(T):
    if not T:
        return 0
    def dfs(node, max_so_far):
        if node.x >= max_so_far:
            visible[0] += 1
            max_so_far = node.x
        if not node.l and node.r:
            return
        if node.l:
            dfs(node.l, max_so_far)
        if node.r:
            dfs(node.r, max_so_far)

    visible = [0]
    max_so_far = float("-inf")
    dfs(T, max_so_far)

    return visible[0]


print(solution())