# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not k or not head:
            return head

        count = 0
        start = dummy = ListNode(None)
        dummy.next = head

        while head:
            count += 1
            if count > k:
                temp = start.next
                self.reverse_between(start, head)
                start = temp
                count = 1
            head = head.next

        if count >= k:
            self.reverse_between(start, None)

        return dummy.next

    def reverse_between(self, start, end):
        if not start:
            return
        pre = start.next
        if pre:
            p = pre.next
        else:
            return
        while p != end:
            p.next, pre, p = pre, p, p.next
        start.next.next, start.next = end, pre

t = Solution()
tc1 = ListNode(1)
tc2 = ListNode(2)
tc3 = ListNode(3)
tc1.next, tc2.next = tc2, tc3
t.reverseKGroup(tc1, 1)
assert(tc1.next == tc2)
assert(tc2.next == tc3)
t.reverseKGroup(tc1, 2)
assert(tc1.next == tc3)
assert(tc2.next == tc1)
print("tests passed")
