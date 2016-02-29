# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, start, end):
        if not start or not start.next:
            return
        prev, p = start, start.next
        while p != end:
            p.next, prev, p = prev, p, p.next
        start.next.next, start.next = end, prev

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        self.reverse(slow, None)

        l, r = head, slow.next
        while l and r:
            if l.val != r.val:
                return False
            l, r = l.next, r.next

        return True
