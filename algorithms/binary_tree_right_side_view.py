# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def middle_root_traverse(self, root, depth):
        if root is None:
            return
        self.ans[depth] = root.val
        self.middle_root_traverse(root.left, depth + 1)
        self.middle_root_traverse(root.right, depth + 1)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = dict()
        self.middle_root_traverse(root, 0)
        return list(self.ans.values())

t = Solution()

assert t.rightSideView(None) == []

root = TreeNode(1)

assert t.rightSideView(root) == [1]

left = TreeNode(2)
root.left = left

assert t.rightSideView(root) == [1, 2]

right = TreeNode(3)
root.right = right

assert t.rightSideView(root) == [1, 3]

left_right = TreeNode(4)
left.right = left_right

assert t.rightSideView(root) == [1, 3, 4]

print "tests passed"
