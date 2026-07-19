class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        def helper(start,end)->int:
            dp={start:nums[start],start+1:max(nums[start],nums[start+1])}
            def helper2(i)->int:
                if i in dp:
                    return dp[i]
                else:
                    dp[i]=max(nums[i]+helper2(i-2),helper2(i-1))
                return dp[i]
            return helper2(end)
        case1=helper(0,len(nums)-2)
        case2=helper(1,len(nums)-1)
        return max(case1,case2)