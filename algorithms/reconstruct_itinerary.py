from collections import defaultdict

class Solution(object):
    START = "JFK"

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        airlines = defaultdict(list)
        for departure, arrival in tickets:
            airlines[departure].append(arrival)

        for airport in airlines:
            airlines[airport].sort()

        N_edges = len(tickets)

        def dfs(airport, remain_edges, path):
            if remain_edges == 0:
                return path
            if airlines[airport]:
                for i, next_airport in enumerate(airlines[airport]):
                    airlines[airport].pop(i)
                    res = dfs(next_airport, remain_edges - 1, path + [next_airport])
                    if res:
                        return res
                    airlines[airport].insert(i, next_airport)
            return False

        return dfs(self.START, N_edges, [self.START])

t = Solution()
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
assert(t.findItinerary(tickets) == ["JFK", "MUC", "LHR", "SFO", "SJC"])
tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
assert(t.findItinerary(tickets) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])
print("tests passed")
