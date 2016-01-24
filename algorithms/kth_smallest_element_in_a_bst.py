# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = [(root, False)]
        count = 0
        while stack:
            p, visited = stack.pop(-1)
            if not visited:
                while p:
                    stack.append((p, True))
                    p = p.left
            else:
                count += 1
                if count == k:
                    return p.val
                if p.right:
                    stack.append((p.right, False))

t = Solution()
root = TreeNode(2)
left = TreeNode(1)
right = TreeNode(3)
root.left = left
root.right = right
assert(t.kthSmallest(root, 2) == 2)
print("tests passed")
