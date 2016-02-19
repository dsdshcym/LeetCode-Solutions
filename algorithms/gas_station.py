class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost or sum(gas) < sum(cost):
            return -1
        total, start = 0, 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            total += g - c
            if total < 0:
                total = 0
                start = i + 1
        return start
