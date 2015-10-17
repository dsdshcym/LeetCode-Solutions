# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = deque()
        up = False
        while True:
            if root is None:
                if len(stack) == 0:
                    break
                root = stack.pop()
                up = True
            if not up:
                stack.append(root)
                root = root.left
            else:
                ans.append(root.val)
                root = root.right
                up = False
        return ans

t = Solution()
root = TreeNode(1)
right = TreeNode(2)
left = TreeNode(3)
root.right = right
right.left = left
assert t.inorderTraversal(root) == [1, 3, 2]

print "tests passed"
