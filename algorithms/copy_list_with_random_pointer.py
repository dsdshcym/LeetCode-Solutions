# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        node_hash = {None:None}
        p = head
        while p:
            node_hash[p] = RandomListNode(p.label)
            p = p.next

        p = head
        while p:
            node_hash[p].next = node_hash[p.next]
            node_hash[p].random = node_hash[p.random]
            p = p.next

        return node_hash[head]
