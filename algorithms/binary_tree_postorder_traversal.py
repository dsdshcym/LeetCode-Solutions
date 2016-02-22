# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        visited = {}
        stack = [root]
        while stack:
            current = stack.pop(-1)
            if not current:
                continue
            if current not in visited:
                visited[current] = 0
                stack.extend([current, current.left])
            elif visited[current] == 0:
                visited[current] = 1
                stack.extend([current, current.right])
            elif visited[current] == 1:
                ans.append(current.val)
        return ans
