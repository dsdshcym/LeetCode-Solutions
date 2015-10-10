# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pre_order_traversal(self, root):
        if root is None:
            return
        self.pre_order_traversal(root.left)
        self.tree_val.append(root.val)
        self.pre_order_traversal(root.right)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.tree_val = list()
        self.pre_order_traversal(root)
        for i in range(len(self.tree_val) - 1):
            if self.tree_val[i] >= self.tree_val[i + 1]:
                return False
        return True

t = Solution()

assert t.isValidBST(None)

root = TreeNode(10)
assert t.isValidBST(root)

left = TreeNode(5)
root.left = left
assert t.isValidBST(root)

right = TreeNode(100)
root.right = right
assert t.isValidBST(root)

new_right = TreeNode(1)
left.right = new_right
assert not t.isValidBST(root)

print "tests passed"
