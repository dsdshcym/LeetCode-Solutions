class WiggleSubsequence
  class << self
    def wiggle_max_length(array)
      array.reduce([]) do |wiggle_sub, current|
        case wiggle_sub.length
        when 0; then wiggle_sub + [current]
        when 1
          if current != wiggle_sub[-1]
            wiggle_sub + [current]
          else
            wiggle_sub
          end
        else
          if ((current < wiggle_sub[-1]) && (wiggle_sub[-1] > wiggle_sub[-2])) || ((current > wiggle_sub[-1]) && (wiggle_sub[-1] < wiggle_sub[-2]))
            wiggle_sub + [current]
          elsif ((current < wiggle_sub[-1]) && (wiggle_sub[-1] < wiggle_sub[-2]))
            wiggle_sub[0..-2] + [current]
          elsif ((current > wiggle_sub[-1]) && (wiggle_sub[-1] > wiggle_sub[-2]))
            wiggle_sub[0..-2] + [current]
          else
            wiggle_sub
          end
        end
      end
        .length
    end
  end
end
