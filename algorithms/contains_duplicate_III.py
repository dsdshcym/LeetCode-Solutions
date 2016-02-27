class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        bucket = {}
        for i, num in enumerate(nums):
            hash_val, offset = (num // t, 1) if t else (num, 0)
            for check_val in [hash_val-offset, hash_val, hash_val+offset]:
                if check_val in bucket and abs(bucket[check_val]-num) <= t:
                    return True
            bucket[hash_val] = num

            if i >= k:
                del bucket[nums[i - k] // t if t else nums[i - k]]

        return False

t = Solution()
assert(t.containsNearbyAlmostDuplicate([0,2147483647], 1, 2147483647))
assert(not t.containsNearbyAlmostDuplicate([1, 2], 0, 1))
print("tests passed")
