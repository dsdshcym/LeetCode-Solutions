# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def __init__(self):
        self.pre = None

    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        if self.pre:
            if root == self.pre.left:
                root.next = self.pre.right
            if root == self.pre.right:
                if self.pre.next:
                    root.next = self.pre.next.left
        self.pre = root
        self.connect(root.left)
        self.pre = root
        self.connect(root.right)
