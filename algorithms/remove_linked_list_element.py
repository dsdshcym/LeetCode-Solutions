# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head is not None:
            if head.val == val:
                head = head.next
            else:
                break
        if head is None:
            return None
        pre = head
        now = head.next
        while now:
            if now.val == val:
                pre.next = now.next
            else:
                pre = now
            now = now.next
        return head
