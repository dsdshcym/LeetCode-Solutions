# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p = head
        second = head.next
        i = 0
        while p:
            i += 1
            temp = p.next
            if not temp:
                if (i % 2 == 1):
                    p.next = second
                break
            if (i % 2 == 1) and (not temp.next):
                p.next = second
                break
            p.next = temp.next
            p = temp
        return head

t = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
t.oddEvenList(n1)
assert n1.next == n3
assert n3.next == n5
assert n2.next == n4
assert n4.next == n6
assert n7.next == n2

t.oddEvenList(None)
print("tests passed")
