# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {ListNode}
def delete_duplicates(head)
  while head
    while head.next and head.next.val == head.val
      head.next = head.next.next
    end
    ans ||= head
    head = head.next
  end
  ans
end

a = ListNode.new(1)
b = ListNode.new(1)

a.next = b

p delete_duplicates(a)
