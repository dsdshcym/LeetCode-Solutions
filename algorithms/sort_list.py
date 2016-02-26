# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre = fast = slow = head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next

        pre.next = None
        return self.merge(*(map(self.sortList, (head, slow))))

    def merge(self, a, b):
        p = dummy = ListNode(None)
        while a and b:
            if a.val < b.val:
                p.next = a
                a = a.next
            else:
                p.next = b
                b = b.next
            p = p.next
        p.next = a or b
        return dummy.next

t = Solution()
tc1 = ListNode(1)
tc2 = ListNode(2)
tc2.next = tc1
assert(t.sortList(tc2).val == 1)
print("tests passed")
