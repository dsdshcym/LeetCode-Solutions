# @param {Integer} n
# @return {Boolean}
def is_happy(n)
  visited = []
  while n != 1
    if visited.include?(n)
      return false
    else
      visited.push(n)
    end
    n = n.to_s.chars.map(&:to_i).inject(0) { |s, x| s + x * x }
  end
  return true
end

2.upto(10) { |x| p is_happy(x) }
