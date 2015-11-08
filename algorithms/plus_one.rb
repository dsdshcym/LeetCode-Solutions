class Integer
  def to_a
    num = self
    ans = []
    while num != 0
      digit = num % 10
      num /= 10
      ans.unshift(digit)
    end
    ans
  end
end

# @param {Integer[]} digits
# @return {Integer[]}
def plus_one(digits)
  num = digits.inject { |n, digit| n = n * 10 + digit } + 1
  num.to_a
end

p plus_one([1, 2, 9])
