from ik.tree.ds import TreeNode


def build_binary_search_tree(preorder):
    inorder = sorted(preorder)
    index_map = {}
    for i in range(len(inorder)):
        index_map[inorder[i]] = i

    def helper(inorder, i_start, i_end, preorder, p_start, p_end):

        # base case
        if i_start > i_end:
            return None

        if i_start == i_end:
            return TreeNode(inorder[i_start])

        # recursive case
        root_val = preorder[p_start]
        node = TreeNode(root_val)

        root_index = index_map[root_val]

        # inorder left and right
        i_left_start = i_start
        i_left_end = root_index - 1
        i_right_start = root_index + 1
        i_right_end = i_end

        left_size = root_index - i_start
        right_size = i_end - root_index

        # prorder left and right
        p_left_start = p_start + 1
        p_left_end = p_start + left_size
        p_right_start = p_left_end + 1
        p_right_end = p_left_end + right_size

        node.left_ptr = helper(inorder, i_left_start, i_left_end, preorder, p_left_start, p_left_end)
        node.right_ptr = helper(inorder, i_right_start, i_right_end, preorder, p_right_start, p_right_end)

        return node

    return helper(inorder, 0, len(inorder) - 1, preorder, 0, len(preorder) - 1)

result = build_binary_search_tree([5, 3, 2, 4, 7, 6, 8])
print(result)