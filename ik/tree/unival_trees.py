from ik.tree.ds import TreeNode


def findSingleValueTrees(root):
    if not root:
        return 0
    univals = [0]

    def dfs(node):
        # base case
        if not node.left_ptr and not node.right_ptr:
            univals[0] += 1
            return True

        # recursion
        isUnival = True
        if node.left_ptr:
            isUnival = dfs(node.left_ptr) and node.val == node.left_ptr.val
        if node.right_ptr:
            isUnival = dfs(node.right_ptr) and node.val == node.right_ptr.val and isUnival

        if isUnival:
            univals[0] += 1

        return isUnival

    dfs(root)

    return univals[0]

root = TreeNode(5)
root.left_ptr = TreeNode(5)
root.right_ptr = TreeNode(5)

root.left_ptr.left_ptr = TreeNode(5)
root.left_ptr.right_ptr = TreeNode(5)

root.right_ptr.left_ptr = TreeNode(5)
root.right_ptr.right_ptr = TreeNode(5)

print(findSingleValueTrees(root))

