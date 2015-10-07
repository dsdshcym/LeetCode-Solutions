# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, des):
        if node is None:
            return None
        if node == des:
            return [node]
        left_results = self.dfs(node.left, des)
        if left_results:
            return left_results + [node]
        right_results = self.dfs(node.right, des)
        if right_results:
            return right_results + [node]
        return None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_ancesters = self.dfs(root, p)
        q_ancesters = self.dfs(root, q)
        for ancester in p_ancesters:
            if ancester in q_ancesters:
                return ancester
