class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        end = nums[0]
        farthest = 0
        if n==1:
            return 0
        for i in range(1,n - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                jumps += 1
                end = farthest
        jumps+=1
        return jumps

