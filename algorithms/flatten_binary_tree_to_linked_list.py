# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.pre = TreeNode(None)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        left = root.left
        right = root.right
        self.pre.left = None
        self.pre.right = root
        self.pre = root
        self.flatten(left)
        self.flatten(right)

t = Solution()
root = TreeNode(0)
left = TreeNode(1)
root.left = left
t.flatten(root)
assert(root.val == 0)
assert(root.left == None)
assert(root.right == left)
print("tests passed")
