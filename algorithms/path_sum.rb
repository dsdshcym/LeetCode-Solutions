# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} sum
# @return {Boolean}
def has_path_sum(root, sum)
  return false if root.nil?
  sum -= root.val
  if (sum == 0) and (root.left.nil? and root.right.nil?)
    return true
  end
  return (has_path_sum(root.left, sum) or has_path_sum(root.right, sum))
end
