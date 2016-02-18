import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)

        def list_iterator(node):
            while node:
                yield (node.val, node)
                node = node.next

        heap = heapq.merge(*map(list_iterator, lists))

        for _, node in heap:
            pre.next, pre = node, node

        return dummy.next
