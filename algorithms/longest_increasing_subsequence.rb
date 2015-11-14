# @param {Integer[]} nums
# @return {Integer}
def length_of_lis(nums)
  buf = []
  nums.each do |num|
    i = buf.index { |x| x >= num }
    if i
      buf[i] = num
    else
      buf << num
    end
  end
  buf.length
end

raise unless length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
raise unless length_of_lis([]) == 0
raise unless length_of_lis([2, 2]) == 1
