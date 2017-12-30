require 'minitest/autorun'

require_relative 'wiggle_subsequence'

class WiggleSubsequenceTest < Minitest::Test
  def test_returns_0_for_empty_array
    assert_equal WiggleSubsequence.wiggle_max_length([]), 0
  end

  def test_returns_1_for_one_element_array
    assert_equal WiggleSubsequence.wiggle_max_length([1]), 1
  end

  def test_returns_2_for_array_with_2_different_elements
    assert_equal WiggleSubsequence.wiggle_max_length([1, 2]), 2
  end

  def test_returns_1_for_array_with_2_identical_elements
    assert_equal WiggleSubsequence.wiggle_max_length([1, 1]), 1
  end

  def test_returns_3_for_array_with_3_wiggle_elements
    assert_equal WiggleSubsequence.wiggle_max_length([1, 3, 2]), 3
  end

  def test_examples
    assert_equal WiggleSubsequence.wiggle_max_length([1, 7, 4, 9, 2, 5]), 6
    assert_equal WiggleSubsequence.wiggle_max_length([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]), 7
    assert_equal WiggleSubsequence.wiggle_max_length([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2
  end

  def test_handles_decrease_subsequence_correctly
    assert_equal WiggleSubsequence.wiggle_max_length([33, 53, 12, 64, 50, 41, 45, 21, 97]), 8
  end
end
