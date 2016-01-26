class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        width = max(0, min(C, G) - max(A, E))
        height = max(0, min(D, H) - max(B, F))
        covered = width * height
        total = (C - A) * (D - B) + (G - E) * (H - F)
        return total - covered

t = Solution()
assert(t.computeArea(0, 0, 0, 0, -1, -1, 1, 1) == 4)
print("tests passed")
