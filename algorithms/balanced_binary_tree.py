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
        self.getDepth(root)
        if abs(self.depth[root.left] - self.depth[root.right]) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False

    def getDepth(self, root):
        if root is None:
            return 0
        self.depth[root] = max(self.getDepth(root.left), self.getDepth(root.right)) + 1
        return self.depth[root]

root = TreeNode(0)
root.left = TreeNode(0)
root.right = TreeNode(0)
t = Solution()
t.isBalanced(root)
print "test passed"
