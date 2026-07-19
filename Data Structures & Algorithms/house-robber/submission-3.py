class Solution:
    def rob(self, nums: List[int]) -> int:
        #memo
        n=len(nums)
        if n==1:
            return nums[0]
        memo={0:nums[0],1:max(nums[0],nums[1])}
        def helper(n)->int:
            if n in memo:
                return memo[n]
            else:
                memo[n]=max(nums[n]+helper(n-2),helper(n-1))
                return memo[n]
        return helper(n-1)
