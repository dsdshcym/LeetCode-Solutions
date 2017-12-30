defmodule WiggleSubsequenceTest do
  use ExUnit.Case
  doctest WiggleSubsequence

  describe "WiggleSubsequence.calc" do
    test "returns 0 for empty array" do
      assert WiggleSubsequence.calc([]) == 0
    end

    test "returns 1 for array with 1 element" do
      assert WiggleSubsequence.calc([1]) == 1
    end

    test "returns 2 for array with 2 different elements" do
      assert WiggleSubsequence.calc([1, 2]) == 2
    end

    test "returns 1 for array with 2 identical elements" do
      assert WiggleSubsequence.calc([1, 1]) == 1
    end

    test "returns 3 for array with 3 wiggle elements" do
      assert WiggleSubsequence.calc([1, 3, 2]) == 3
    end

    test "handles decrease subsequence correctly" do
      assert WiggleSubsequence.calc([33, 53, 12, 64, 50, 41, 45, 21, 97]) == 8
    end
  end
end
