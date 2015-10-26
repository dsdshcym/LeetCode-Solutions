# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root):
        if root is None:
            return 0
        l_max = self.dfs(root.left)
        r_max = self.dfs(root.right)
        self.ans = max(self.ans, l_max + r_max + root.val)
        return max(0, l_max + root.val, r_max + root.val)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.ans = root.val
        else:
            self.ans = 0
        self.dfs(root)
        return self.ans

def test():
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    t = Solution()
    root = TreeNode(1)
    left = TreeNode(-2)
    right = TreeNode(3)
    root.left = left
    root.right = right

    assert t.maxPathSum(root) == 4
