class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
def levelOrder(root):
    if not root:
        return []

    result = []
    q = deque()
    q.append(root)

    while q:
        last = None
        for _ in range(len(q)):
            node = q.popleft()
            #level_result.append(node.val)
            last = node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if last:
            result.append(last.val)

    return result

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
print(levelOrder(root))