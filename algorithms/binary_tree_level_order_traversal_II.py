# Python List.pop(index)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        travel_result = []
        search_queue = [(root, 0)]
        while search_queue != []:
            node, depth = search_queue.pop(0)
            if node is None:
                continue
            if len(travel_result) <= depth:
                travel_result.append([])
            travel_result[depth].append(node.val)
            search_queue.append((node.left, depth + 1))
            search_queue.append((node.right, depth + 1))
        return travel_result[::-1]

t = Solution()
root = TreeNode(1)
assert t.levelOrderBottom(root) == [[1]]
left = TreeNode(2)
root.left = left
right = TreeNode(3)
root.right = right
assert t.levelOrderBottom(root) == [[2, 3], [1]]
print("tests passed")
