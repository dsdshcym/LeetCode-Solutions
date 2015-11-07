# @param {Integer} num
# @return {Boolean}
def is_ugly(num)
  return false if num == 0
  [2, 3, 5].each do |x|
    while num % x == 0
      num /= x
    end
  end
  num == 1
end

p is_ugly(10)
p is_ugly(4)
p is_ugly(0)
