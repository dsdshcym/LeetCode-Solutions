# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
  l = ListNode.new(0)
  head = l
  r = 0
  while l1 or l2 or r != 0
    a = b = 0
    a = l1.val if l1
    b = l2.val if l2
    s = a + b + r
    l.val = s % 10
    r = s / 10
    pre = l
    l = ListNode.new(0)
    pre.next = l
    l1 = l1.next if l1
    l2 = l2.next if l2
  end
  pre.next = nil
  head
end

def create_test_list(*digits)
  l = ListNode.new(0)
  head = pre = l
  digits.each do |digit|
    l.val = digit
    pre = l
    pre.next = l = ListNode.new(0)
  end
  pre.next = nil
  head
end

l1 = create_test_list(2, 4, 3)
l2 = create_test_list(5, 6, 4)

p add_two_numbers(l1, l2)
p add_two_numbers(ListNode.new(4), ListNode.new(6))
