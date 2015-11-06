# @param {Integer} n
# @return {Boolean}
def can_win_nim(n)
  n % 4 != 0
end

p can_win_nim(3)
p can_win_nim(4)
