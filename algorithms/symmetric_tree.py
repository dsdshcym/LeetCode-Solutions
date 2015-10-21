# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfsCompare(self, a, b):
        if (a is None) ^ (b is None):
            return False
        if (a is None) and (b is None):
            return True
        if a.val != b.val:
            return False
        return self.dfsCompare(a.right, b.left) and self.dfsCompare(a.left, b.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.dfsCompare(root.left, root.right)


def test():
    t = Solution()

    assert t.isSymmetric(None)

    root = TreeNode(1)

    assert t.isSymmetric(root)

    left = TreeNode(2)
    root.left = left

    assert not t.isSymmetric(root)

    right = TreeNode(2)
    root.right = right

    assert t.isSymmetric(root)
