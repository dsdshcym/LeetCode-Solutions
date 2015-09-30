#+TAG: NEEDS_IMPROVE

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pointer = head
        array = []
        while (pointer != None):
            array.append(pointer.val)
            pointer = pointer.next
        N = len(array)
        for i in range(N / 2):
            if (array[i] != array[N - i - 1]):
                return False
        return True
