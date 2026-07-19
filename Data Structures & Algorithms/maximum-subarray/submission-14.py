class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx=float('-inf')
        if len(nums)==1:
            return nums[0]
        total=0
        for i in range (len(nums)):
            total+=nums[i]                        
            maxx=max(maxx,total)
            if total<0:
                total=0
        return maxx
