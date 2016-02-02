class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans, l, r = 0, 0, len(height) - 1
        while l != r:
            width = r - l
            if height[l] < height[r]:
                ans, l = max(ans, height[l] * width), l + 1
            else:
                ans, r = max(ans, height[r] * width), r - 1
        return ans
