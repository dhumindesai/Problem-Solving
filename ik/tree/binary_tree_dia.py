class TreeNode():
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

def binary_tree_diameter(root):
    if not root:
        return 0

    max_dia = [0]

    def dfs(node):

        # base case
        if not node.left_ptr and not node.right_ptr:
            return 0

        # recursive case
        left_height = 0
        right_height = 0
        dia = 0
        if node.left_ptr:
            left_height = 1 + dfs(node.left_ptr)
            dia += left_height
        if node.right_ptr:
            right_height = 1 + dfs(node.right_ptr)
            dia += right_height

        max_dia[0] = max(max_dia[0], dia)

        return max(left_height, right_height)

    dfs(root)

    return max_dia[0]

root = TreeNode(0)
root.left_ptr = TreeNode(1)

root.left_ptr.left_ptr = TreeNode(2)
root.left_ptr.left_ptr.left_ptr = TreeNode(4)

root.left_ptr.right_ptr = TreeNode(3)
root.left_ptr.right_ptr.right_ptr = TreeNode(5)

print(binary_tree_diameter(root))