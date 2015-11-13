# @param {String} pattern
# @param {String} str
# @return {Boolean}
def word_pattern(pattern, str)
  words = str.split
  return false if pattern.length != words.length
  hash = Hash.new()
  pattern.each_char.with_index do |c, i|
    hash[c] ||= words[i]
    return false if hash[c] != words[i]
    return false if (i > 0) and
      ((pattern[i] == pattern[i - 1]) ^ (words[i] == words[i - 1]))
  end
  return true
end

raise unless word_pattern('abba', 'a b b a')
raise if word_pattern("abba", "dog dog dog dog")
raise if word_pattern("abba", "dog dog dog")
