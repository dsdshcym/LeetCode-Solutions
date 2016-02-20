class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        major1 = major2 = count1 = count2 = 0
        for num in nums:
            if num == major1:
                count1 += 1
            elif num == major2:
                count2 += 1
            elif count1 == 0:
                major1 = num
                count1 = 1
            elif count2 == 0:
                major2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        ans = []
        if nums.count(major1) > N // 3:
            ans.append(major1)
        if major1 != major2 and nums.count(major2) > N // 3:
            ans.append(major2)
        return ans
