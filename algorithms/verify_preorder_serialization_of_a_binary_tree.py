class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        preorder = preorder.split(",")
        for char in preorder:
            stack.append(char)
            while len(stack) > 1 and stack[-1] == stack[-2] == "#":
                stack.pop()
                stack.pop()
                if not stack or stack[-1] == "#":
                    return False
                stack[-1] = "#"
        return stack == ["#"]

t = Solution()
assert(t.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
assert(t.isValidSerialization("#"))
assert(not t.isValidSerialization("1,#"))
assert(not t.isValidSerialization("#,#,#"))
assert(not t.isValidSerialization("9,#,#,1"))
print("tests passed")
