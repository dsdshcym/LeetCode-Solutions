# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generate(1, n + 1)

    def generate(self, start, end):
        if start >= end:
            return []

        result = []
        for i in xrange(start, end):
            left = self.generate(start, i) or [None]
            right = self.generate(i+1, end) or [None]
            for l_node in left:
                for r_node in right:
                    root = TreeNode(i)
                    root.left = l_node
                    root.right = r_node
                    result.append(root)
        return result

t = Solution()
assert(len(t.generateTrees(1)) == 1)
print("tests passed")
