class Solution:
    def climbStairs(self, n: int) -> int:
        # i will try the top down approach
        memo={1:1,2:2}
        def topDown(n:int)->int:
            if n in memo:
                return memo[n]
            else:
                memo[n]=topDown(n-2)+topDown(n-1)
                return memo[n]
        return topDown(n)