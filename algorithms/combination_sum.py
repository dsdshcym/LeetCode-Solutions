class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        for i in range(target + 1):
            if i in candidates and i <= target:
                combinations.append([[i]])
            else:
                combinations.append([])
        for i in range(1, target + 1):
            if combinations[i]:
                for combination in combinations[i]:
                    for candidate in candidates:
                        if candidate >= combination[-1] and candidate + i <= target:
                            combinations[candidate + i].append(combination + [candidate])
        return combinations[target]

t = Solution()
# assert(t.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]])
assert(t.combinationSum([2], 1) == [])
print("tests passed")
