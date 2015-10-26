# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isLeaf(self, node):
        return node.left is None and node.right is None

    def dfs(self, node, s):
        if node is None:
            return
        s *= 10
        s += node.val
        if self.isLeaf(node):
            self.sum += s
            return
        self.dfs(node.left, s)
        self.dfs(node.right, s)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.sum = 0
        self.dfs(root, 0)
        return self.sum
