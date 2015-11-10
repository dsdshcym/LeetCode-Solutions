# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
  count = 1
  m = nums[0]
  nums[1..-1].each do |x|
    if x == m
      count += 1
    else
      count -= 1
      if count == 0
        m = x
        count = 1
      end
    end
  end
  m
end

p majority_element([3, 2, 3])
