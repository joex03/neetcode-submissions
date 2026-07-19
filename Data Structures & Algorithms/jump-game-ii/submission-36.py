class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        jumps=1
        currentJump=nums[0]
        maxx=nums[0]
        for i in range( 1,len(nums)-1):
            maxx=max(maxx,nums[i]+i)
            if currentJump==i:
                jumps+=1
                currentJump=maxx
        return jumps

