#+TAG: NEEDS_IMPROVE

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def buildIterator(self, root):
        if root is None:
            return
        self.buildIterator(root.left)
        self.iterator.append(root.val)
        self.buildIterator(root.right)

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.pointer = -1
        self.iterator = list()
        self.buildIterator(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pointer < len(self.iterator) - 1

    def next(self):
        """
        :rtype: int
        """
        self.pointer += 1
        return self.iterator[self.pointer]


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
