# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p is not None:
            while p.next is not None and \
                  p.val == p.next.val:
                p.next = p.next.next
            p = p.next
        return head

t = Solution()

a = ListNode(1)
b = ListNode(1)
c = ListNode(1)
a.next = b
b.next = c

t.deleteDuplicates(a)

assert a.next == None

print("tests passed")
