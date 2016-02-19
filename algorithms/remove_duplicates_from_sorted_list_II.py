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
        pre = dummy = ListNode(None)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head.next = head.next.next
                pre.next = head.next
            else:
                pre = head
            head = head.next
        return dummy.next

t = Solution()
n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(2)
n1.next, n2.next, n3.next = n2, n3, n4
assert(t.deleteDuplicates(n1) == None)
print("tests passed")
