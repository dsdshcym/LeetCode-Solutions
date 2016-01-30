# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = pre = ListNode(None)
        p = dummy.next = head
        while p and p.next:
            pre.next, p.next.next, p.next, pre, p = p.next, p, p.next.next, p, p.next.next
        return dummy.next

t = Solution()
a = ListNode(1)
b = ListNode(2)
a.next = b
assert(t.swapPairs(a) == b)
