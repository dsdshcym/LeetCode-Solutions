# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, path):
        if root.left is None and root.right is None:
            self.ans.append(path)
            return
        if root.left:
            self.dfs(root.left, path + '->' + str(root.left.val))
        if root.right:
            self.dfs(root.right, path + '->' + str(root.right.val))

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        self.ans = []
        self.dfs(root, str(root.val))
        return self.ans

def test_Solution():
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    t = Solution()
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    left_right = TreeNode(5)
    root.left = left
    root.right = right
    left.right = left_right
    assert set(t.binaryTreePaths(root)) == set(['1->2->5', '1->3'])
    assert t.binaryTreePaths(None) == []

test_Solution()
