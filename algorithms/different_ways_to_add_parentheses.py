class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if not input:
            return []
        VALID_OPERATOR = '+-*'
        if all(op not in input for op in VALID_OPERATOR):
            return [int(input)]
        ans = []
        for i, c in enumerate(input):
            if c in VALID_OPERATOR:
                a = self.diffWaysToCompute(input[:i])
                b = self.diffWaysToCompute(input[i+1:])
                if c == '+':
                    ans.extend([x + y for x in a for y in b])
                if c == '-':
                    ans.extend([x - y for x in a for y in b])
                if c == '*':
                    ans.extend([x * y for x in a for y in b])
        return ans

t = Solution()
assert(set(t.diffWaysToCompute("2-1-1")) == set([0, 2]))
assert(set(t.diffWaysToCompute("2*3-4*5")) == set([-34, -14, -10, -10, 10]))
print("tests passed")
