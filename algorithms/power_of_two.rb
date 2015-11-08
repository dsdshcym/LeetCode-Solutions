# @param {Integer} n
# @return {Boolean}
def is_power_of_two(n)
  return false if n == 0
  (n & (-n)) == n
end

p is_power_of_two(0)
p is_power_of_two(2)
p is_power_of_two(3)
p is_power_of_two(4)
