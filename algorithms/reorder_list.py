# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        slow.next, prev, p = None, None, slow.next
        while p:
            p.next, prev, p = prev, p, p.next

        half, p = prev, head
        while half:
            p.next, half.next, half, p = half, p.next, half.next, p.next

t = Solution()
tc1 = ListNode(1)
tc2 = ListNode(2)
tc3 = ListNode(3)
tc4 = ListNode(4)
tc5 = ListNode(5)
tc1.next = tc2
tc2.next = tc3
tc3.next = tc4
tc4.next = tc5
t.reorderList(tc1)
assert(tc1.next == tc5 and tc5.next == tc2 and tc2.next == tc4)
print("tests passed")
