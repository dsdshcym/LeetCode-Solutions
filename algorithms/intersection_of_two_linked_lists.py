# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = lenB = 0
        pA = headA
        pB = headB
        while pA:
            lenA += 1
            pA = pA.next
        while pB:
            lenB += 1
            pB = pB.next

        pA = headA
        pB = headB
        while lenA > lenB:
            pA = pA.next
            lenA -= 1
        while lenB > lenA:
            pB = pB.next
            lenB -= 1

        while pA != pB:
            pA = pA.next
            pB = pB.next

        return pA
