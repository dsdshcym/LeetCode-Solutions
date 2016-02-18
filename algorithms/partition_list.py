# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_little_head = dummy_little_tail = ListNode(x-1)
        dummy_big_head = dummy_big_tail = ListNode(x+1)

        while head:
            if head.val < x:
                dummy_little_tail.next = head
                dummy_little_tail = head
            else:
                dummy_big_tail.next = head
                dummy_big_tail = head
            head = head.next

        dummy_little_tail.next, dummy_big_tail.next = dummy_big_head.next, None
        return dummy_little_head.next

t = Solution()
test_case = ListNode(1)
assert(t.partition(test_case, 2).val == 1)
test_case_2 = ListNode(2)
test_case_2.next = test_case
assert(t.partition(test_case_2, 2).next.val == 2)
print("tests passed")
