# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, path):
        path = path + [root.val]
        if root.left is None and root.right is None:
            if sum(path) == self.sum:
                self.ans.append(path)
            return
        if root.left:
            self.dfs(root.left, path)
        if root.right:
            self.dfs(root.right, path)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.sum = sum
        self.ans = []
        if root:
            self.dfs(root, [])
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
    assert t.pathSum(root, 8) == [[1, 2, 5]]
    assert t.pathSum(None, 0) == []

test_Solution()
