# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = [root]
        pre = TreeNode(None)
        while stack:
            now = stack.pop(-1)
            while now:
                pre.left = None
                pre.right = now
                if now.right:
                    stack.append(now.right)
                pre = now
                now = now.left

t = Solution()
root = TreeNode(0)
left = TreeNode(1)
root.left = left
t.flatten(root)
assert(root.val == 0)
assert(root.left == None)
assert(root.right == left)
print("tests passed")
