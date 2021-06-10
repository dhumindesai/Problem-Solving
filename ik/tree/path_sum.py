class TreeNode():
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

def path_sum(root, k):
    result = [False]
    def dfs(node, s):

        # base case
        if not node.left_ptr and not node.right_ptr:
            if s == node.val:
                result[0] = True
            return

        # recursive case
        if node.left_ptr:
            dfs(node.left_ptr, s - node.val)

        if node.right_ptr:
            dfs(node.right_ptr, s - node.val)

    dfs(root, k)
    return result[0]

def all_paths_sum_k(root, k):
    result = []
    slate = []
    def dfs(node, s):

        # base case
        if not node.left_ptr and not node.right_ptr:
            if s == node.val:
                slate.append(node.val)
                result.append(slate[:])
                slate.pop()
            return

        # recursive case
        slate.append(node.val)
        if node.left_ptr:
            dfs(node.left_ptr, s - node.val)

        if node.right_ptr:
            dfs(node.right_ptr, s - node.val)
        slate.pop()

    dfs(root, k)
    return result

root = TreeNode(0)
root.left_ptr = TreeNode(1)
root.right_ptr = TreeNode(2)
root.left_ptr.left_ptr = TreeNode(3)
root.left_ptr.right_ptr = TreeNode(4)

print(path_sum(root, 4))
print(all_paths_sum_k(root, 4))