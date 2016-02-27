class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        pos_hash = {}

        for i, x in enumerate(nums):
            if len(pos_hash) > 2 * t:
                for y in xrange(x-t, x+t+1):
                    if y in pos_hash and i - pos_hash[y] <= k:
                        return True
            else:
                for y in pos_hash:
                    if abs(x-y) <= t and i - pos_hash[y] <= k:
                        return True
            pos_hash[x] = i

        return False

t = Solution()
assert(t.containsNearbyAlmostDuplicate([0,2147483647], 1, 2147483647))
print("tests passed")
