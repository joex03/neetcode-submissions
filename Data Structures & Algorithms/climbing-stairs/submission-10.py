class Solution:
    def climbStairs(self, n: int) -> int:
        #memo
        memo={1:1,2:2}
        def stairs(n)->int:
            if n in memo:
                return memo[n]
            else:
                memo[n]=stairs(n-2)+stairs(n-1)
                return memo[n]
        return stairs(n)