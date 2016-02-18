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
        dummy = ListNode(x-1)
        dummy.next = head
        little = pre = dummy
        to_check = head
        first_big = None
        while to_check:
            print(to_check.val)
            if to_check.val < x:
                little.next = to_check
                little = to_check
                if first_big:
                    pre.next = to_check.next
            else:
                if not first_big:
                    first_big = to_check
                pre = to_check
            to_check = to_check.next
        little.next = first_big
        return dummy.next

t = Solution()
test_case = ListNode(1)
assert(t.partition(test_case, 2).val == 1)
test_case_2 = ListNode(2)
test_case_2.next = test_case
assert(t.partition(test_case_2, 2).next.val == 2)
print("tests passed")
