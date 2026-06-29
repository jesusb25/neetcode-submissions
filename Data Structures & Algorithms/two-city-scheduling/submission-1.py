class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda a:a[0] - a[1])
        n = len(costs) // 2
        res = 0
        for i in range(len(costs)):
            if i < n:
                res += costs[i][0]
            else:
                res += costs[i][1]
        return res