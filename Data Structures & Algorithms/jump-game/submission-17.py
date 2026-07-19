class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # walahy el soal da mota3alk bel index msh valuess
        goal=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i>=goal:
                goal=i
            else:
                continue
        return goal==0