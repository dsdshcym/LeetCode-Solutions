from itertools import zip_longest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def search_path(self, node, target):
        if not node:
            return None
        if node == target:
            return [target]
        path = self.search_path(node.left, target) or \
               self.search_path(node.right, target)
        if path:
            return [node] + path
        else:
            return None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path_p = self.search_path(root, p)
        path_q = self.search_path(root, q)
        for (a, b) in zip_longest(path_p, path_q):
            if a == b:
                pre = a
            else:
                return pre

t = Solution()
root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right = right
assert(t.lowestCommonAncestor(root, left, right) == root)
print("tests passed")
