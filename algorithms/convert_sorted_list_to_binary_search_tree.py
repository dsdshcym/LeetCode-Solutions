# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def sorted_list_to_BST(begin, end):
            if not begin or begin is end:
                return None
            slow = fast = begin
            while fast and fast.next:
                if fast is end or fast.next is end:
                    break
                slow = slow.next
                fast = fast.next.next
            root = TreeNode(slow.val)
            if slow != fast:
                root.left = sorted_list_to_BST(begin, slow)
                root.right = sorted_list_to_BST(slow.next, end)
            return root

        return sorted_list_to_BST(head, None)

t = Solution()
root = ListNode(0)
assert(t.sortedListToBST(root).val == 0)
print("tests passed")
