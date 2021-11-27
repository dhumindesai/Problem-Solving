import collections

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCousins(root, x, y):
    def find_cousin(nums, q):
        for node in q:
            if node.left and node.left.val in nums:
                return True
            if node.right and node.right.val in nums:
                return True
        return False

    if not root:
        return False

    nums = set({x, y})
    q = collections.deque([root])

    while q:
        num_of_nodes = len(q)
        for _ in range(num_of_nodes):
            node = q.popleft()
            if node.left:
                if node.left.val in nums:
                    nums.remove(node.left.val)
                    return find_cousin(nums, q)
                q.append(node.left)
                if node.right:
                    if node.right.val in nums:
                        nums.remove(node.right.val)
                        return find_cousin(nums, q)
                    q.append(node.right)

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
# root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(isCousins(root, 4,7))