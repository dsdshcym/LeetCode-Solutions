# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.depth = dict()
        self.depth[None] = 0

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        leftIsBalanced = self.isBalanced(root.left)
        rightIsBalanced = self.isBalanced(root.right)

        self.depth[root] = max(self.depth[root.left], self.depth[root.right]) + 1

        if abs(self.depth[root.left] - self.depth[root.right]) <= 1:
            return leftIsBalanced and rightIsBalanced
        return False

root = TreeNode(0)
root.left = TreeNode(0)
root.right = TreeNode(0)
t = Solution()
t.isBalanced(root)
print "test passed"
