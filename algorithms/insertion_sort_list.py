# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            val = head.next.val
            if val > head.val:
                head = head.next
                continue
            if p and p.val > val:
                p = dummy
            while p.next and p.next.val < val:
                p = p.next
            temp = head.next
            head.next = temp.next
            temp.next = p.next
            p.next = temp
        return dummy.next

t = Solution()
tc1 = ListNode(1)
tc2 = ListNode(1)
assert(t.insertionSortList(tc1).val == 1)
tc1.next = tc2
assert(t.insertionSortList(tc1).val == 1)
assert(t.insertionSortList(None) == None)
print("tests passed")
