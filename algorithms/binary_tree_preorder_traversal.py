# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = [root]
        while stack:
            p = stack.pop(-1)
            while p:
                ans.append(p.val)
                stack.append(p.right)
                p = p.left
        return ans
