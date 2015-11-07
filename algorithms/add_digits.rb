# @param {Integer} num
# @return {Integer}
def add_digits(num)
  num < 10 ? num : add_digits(num.to_s.chars.map(&:to_i).reduce(:+))
end

add_digits(38)
