class Solution:
    def rob(self, nums: List[int]) -> int:
        #memo
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        dp={0:nums[0],1:max(nums[0],nums[1])}
        def helper(i)->int:
            if i in dp:
                return dp[i]
            else:
                dp[i]=max(helper(i-2)+nums[i],helper(i-1))
            return dp[i]
        return helper(len(nums)-1)

        