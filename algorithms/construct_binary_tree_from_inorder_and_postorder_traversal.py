# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def dfs(l_post, r_post, l_in, r_in):
            if l_post >= r_post or l_in >= r_in:
                return None
            root_val = postorder[r_post - 1]
            root = TreeNode(root_val)
            left_length = inorder[l_in:r_in].index(root_val)
            root.left = dfs(l_post, l_post + left_length, l_in, l_in + left_length)
            root.right = dfs(l_post + left_length, r_post - 1, l_in + left_length + 1, r_in)
            return root

        return dfs(0, len(postorder), 0, len(inorder))
