class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size=len(nums)-1
        if size==0:
            return True
        goal=size
        for i in range (size-1,-1,-1):
            # if nums[i]==0:
            #     continue
            if i+nums[i]>=goal:
                goal=i
            if goal<=0:
                return True
        return False