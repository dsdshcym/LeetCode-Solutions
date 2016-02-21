# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = p = ListNode(None)
        r = 0
        while l1 or l2 or r:
            p.next = ListNode(0)
            p = p.next

            a = b = 0

            if l1:
                a = l1.val
                l1 = l1.next

            if l2:
                b = l2.val
                l2 = l2.next

            s = a + b + r
            p.val = s % 10
            r = s // 10

        return dummy.next
