# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        n = 0
        p = head
        while p:
            n += 1
            if p.next:
                p = p.next
            else:
                break

        p.next = head
        for i in range((n - k) % n): # In case n < k
            p = p.next

        head, p.next = p.next, None
        return head
