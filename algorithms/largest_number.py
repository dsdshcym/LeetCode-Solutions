class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return str(int(''.join(sorted(map(str, nums),
                                      lambda x, y: cmp(y+x, x+y)))))
