class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #memo
        memo={0:0,1:0}
        def helper(i)->int:
            if i in memo:
                return memo[i]
            else:
                memo[i]=min(cost[i-2]+helper(i-2),cost[i-1]+helper(i-1))
                return memo[i]
        return helper(len(cost))