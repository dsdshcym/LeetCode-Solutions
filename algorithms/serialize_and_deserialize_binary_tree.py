# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        return ''.join([str(root.val), ',', self.serialize(root.left), ',', self.serialize(root.right)])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        nodes = []
        for node in data:
            if node:
                nodes.append(TreeNode(int(node)))
            else:
                nodes.append(None)

        self.index = -1
        N = len(nodes)

        def build_tree():
            self.index += 1
            if self.index >= N or not nodes[self.index]:
                return None
            root = nodes[self.index]
            root.left = build_tree()
            root.right = build_tree()
            return root

        return build_tree()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
