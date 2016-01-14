# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.new = None
        self.pre = None
        self.head = None

    def append(self, new_val):
        self.new = ListNode(new_val)
        if self.pre is None:
            self.head = self.new
        else:
            self.pre.next = self.new
        self.pre = self.new

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        while l1 and l2:
            if l1.val < l2.val:
                new_val = l1.val
                l1 = l1.next
            else:
                new_val = l2.val
                l2 = l2.next
            self.append(new_val)

        while l1:
            self.append(l1.val)
            l1 = l1.next

        while l2:
            self.append(l2.val)
            l2 = l2.next

        return self.head

l1 = ListNode(1)
l2 = None

t = Solution()
assert t.mergeTwoLists(l1, l2).val == 1

print("tests passed")
