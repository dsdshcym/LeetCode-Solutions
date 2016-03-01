# Definition for a binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.root or self.stack)

    def next(self):
        """
        :rtype: int
        """
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        temp = self.stack.pop()
        self.root = temp.right
        return temp.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
