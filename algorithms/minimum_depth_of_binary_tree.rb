# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer}

def min_depth(root)
  return 0 unless root
  queue = [[root, 1]]
  while queue != []
    now, level = queue.shift
    if now
      if (!now.left) && (!now.right)
        return level
      end
      queue.push([now.left, level + 1], [now.right, level + 1])
    end
  end
end

root = TreeNode.new(1)
left = TreeNode.new(2)
ll = TreeNode.new(3)
lll = TreeNode.new(4)
llll = TreeNode.new(5)
root.left = left
left.left = ll
ll.left = lll
lll.left = llll
min_depth(root)
