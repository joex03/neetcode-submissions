class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        n=len(nums)
        for i in range (n):
            for j in range (i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],1+dp[j])
        maxx=0
        for num in dp:
            maxx=max(maxx,num)
        return maxx
#[4,2,6,4,8]
#[1,1,1,1,1]