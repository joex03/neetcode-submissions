class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        def helper(i,target):
            if target==amount:
                return 1
            if i>= len(coins) or target > amount:
                return 0
            if (i,target) in memo:
                return memo[(i,target)]
            take = helper(i,target+coins[i])
            skip= helper(i+1,target)
            memo[(i,target)]=take+skip
            return memo[(i,target)]
        return helper(0,0) 