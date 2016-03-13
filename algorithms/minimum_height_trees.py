from collections import defaultdict

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        adjancy = defaultdict(set)
        for u, v in edges:
            adjancy[u].add(v)
            adjancy[v].add(u)
        queue = [u for u in range(n) if len(adjancy[u]) == 1]
        while len(adjancy) > 2:
            new_queue = set()
            for u in queue:
                for v in adjancy[u]:
                    adjancy[v].remove(u)
                    if len(adjancy[v]) == 1:
                        new_queue.add(v)
                del adjancy[u]
            queue = list(new_queue)
        return list(adjancy.keys())

t = Solution()
assert(t.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]) == [1])
assert(t.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]) == [3, 4])
print("tests passed")
