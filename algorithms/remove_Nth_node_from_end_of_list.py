# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = 0
        nodes = []
        p = head
        while p:
            nodes.append(p)
            p = p.next
        length = len(nodes)
        if n == length:
            return head.next
        if 1 < n < length:
            nodes[length - n - 1].next = nodes[length - n + 1]
        if n == 1:
            nodes[length - 2].next = None
        return head

t = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
t.removeNthFromEnd(n1, 2)
assert n3.next == n5

n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
t.removeNthFromEnd(n1, 1)
assert n1.next == None

print("tests passed")
