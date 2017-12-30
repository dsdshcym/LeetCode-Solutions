defmodule WiggleSubsequence do
  @doc """
  ## Examples

  iex> WiggleSubsequence.calc([1, 7, 4, 9, 2, 5])
  6

  iex> WiggleSubsequence.calc([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])
  7

  iex> WiggleSubsequence.calc([1, 2, 3, 4, 5, 6, 7, 8, 9])
  2
  """
  def calc(array) do
    array
    |> build_wiggle_sub()
    |> length()
  end

  defp build_wiggle_sub(array)  do
    array
    |> Enum.reduce([], &(append_or_replace_head(&1, &2)))
  end

  defp append_or_replace_head(a, []), do: [a]
  defp append_or_replace_head(a, [b]) when a != b, do: [a, b]
  defp append_or_replace_head(a, [b, c | rest]) when (a < b) and (b > c), do: [a, b, c | rest]
  defp append_or_replace_head(a, [b, c | rest]) when (a > b) and (b < c), do: [a, b, c | rest]
  defp append_or_replace_head(a, [b, c | rest]) when (a > b) and (b > c), do: [a, c | rest]
  defp append_or_replace_head(a, [b, c | rest]) when (a < b) and (b < c), do: [a, c | rest]
  defp append_or_replace_head(_, wiggle), do: wiggle
end
