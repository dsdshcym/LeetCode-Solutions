# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre

t = Solution()

assert t.reverseList(None) == None

head = ListNode(1)
assert t.reverseList(head) == head

next = ListNode(2)
head.next = next
assert t.reverseList(head).val == 2

print "tests passed"
