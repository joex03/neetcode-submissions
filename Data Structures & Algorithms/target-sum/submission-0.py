class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def helper(i,amt):
            if i==len(nums) and amt==target:
                return 1
            if i>=len(nums):
                return 0
            pos=helper(i+1,amt+nums[i])
            neg=helper(i+1,amt-nums[i])
            return pos+neg
        return helper(0,0)