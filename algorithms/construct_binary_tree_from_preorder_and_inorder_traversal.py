# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        def dfs(l_pre, r_pre, l_in, r_in):
            if l_pre >= r_pre or l_in >= r_in:
                return None
            root_val = preorder[l_pre]
            root = TreeNode(root_val)
            left_length = inorder[l_in:r_in].index(root_val)
            root.left = dfs(l_pre + 1, l_pre + left_length + 1, l_in, l_in + left_length)
            root.right = dfs(l_pre + left_length + 1, r_pre, l_in + left_length + 1, r_in)
            return root

        return dfs(0, len(preorder), 0, len(inorder))
