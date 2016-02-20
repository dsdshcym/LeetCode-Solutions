# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre = dummy = ListNode(None)
        dummy.next = head

        for i in range(m-1):
            pre, head = head, head.next

        before_mth = pre

        for i in range(m, n+1):
            head.next, pre, head = pre, head, head.next

        nth = pre
        after_nth = head

        before_mth.next.next = after_nth
        before_mth.next = nth

        return dummy.next

t = Solution()
tc1 = ListNode(3)
assert(t.reverseBetween(tc1, 1, 1).val == 3)
tc2 = ListNode(5)
tc1.next = tc2
assert(t.reverseBetween(tc1, 1, 2).val == 5)
print("tests passed")
