class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #memo
        memo={0:0,1:0}
        size=len(cost)
        def minCost(n)->int:
            if n in memo:
                return memo[n]
            else:
                memo[n] =min(cost[n-2]+minCost(n-2),cost[n-1]+minCost(n-1))
                return memo[n]
        return minCost(size)