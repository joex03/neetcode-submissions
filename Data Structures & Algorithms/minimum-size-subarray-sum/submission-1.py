class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        summ=0
        size=float('inf')
        for r in range(len(nums)):
            summ+=nums[r]
            while summ>=target:
                size=min(r-l+1,size)
                summ-=nums[l]
                l+=1
        if size == float('inf'):
            return 0
        else:
            return size