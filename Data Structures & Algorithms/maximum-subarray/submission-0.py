class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=float('-inf')
        maxcurrent=0
        for num in nums:
            maxcurrent+=num
            maxsum=max(maxsum,maxcurrent)
            if maxcurrent<0:
                maxcurrent=0
        return maxsum