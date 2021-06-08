#Time: O(N)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        for i in range(2, n):
            cost[i] = min(cost[i-1]+cost[i], cost[i-2]+ cost[i-1])
        return min(cost[-1], cost[-2])