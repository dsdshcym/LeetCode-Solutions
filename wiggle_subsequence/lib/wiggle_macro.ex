defmodule WiggleMacro do
  defmacro wiggle?(a, b) do
    quote do
      unquote(a) != unquote(b)
    end
  end

  defmacro wiggle?(a, b, c) do
    quote do
      ((unquote(a) < unquote(b)) and (unquote(b) > unquote(c))) or
      ((unquote(a) > unquote(b)) and (unquote(b) < unquote(c)))
    end
  end
end
