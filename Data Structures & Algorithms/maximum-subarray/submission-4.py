class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=float('-inf')
        maxCurrent=0
        for num in nums:
            maxCurrent+=num
            maxSum=max(maxCurrent,maxSum)
            if maxCurrent<0:
                maxCurrent=0
        return maxSum