# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        queue = [root]
        direction = 1
        while queue:
            ans.append([node.val for node in queue[::direction]])
            new_queue = []
            direction = -direction
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return ans

t = Solution()
root = TreeNode(1)
print(t.zigzagLevelOrder(root))
assert(t.zigzagLevelOrder(root)[0] == [1])
print("tests passed")
