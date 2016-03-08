# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.rob_helper(root))

    def rob_helper(self, root):
        if not root:
            return 0, 0
        rob_left, not_rob_left = self.rob_helper(root.left)
        rob_right, not_rob_right = self.rob_helper(root.right)
        return (root.val + not_rob_left + not_rob_right,
                max(rob_left, not_rob_left) + max(rob_right, not_rob_right))

t = Solution()
root = TreeNode(4)
left = TreeNode(1)
ll = TreeNode(2)
lll = TreeNode(3)

root.left, left.left, ll.left = left, ll, lll

assert(t.rob(root) == 7)
print("tests passed")
