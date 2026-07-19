class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # walahy el soal da mota3alk bel index msh valuess
        size = len(nums)-1
        goal = size
        for i in range (size-1,-1,-1):
            if nums[i]+i>=goal:
                goal=i
        if goal <=0:
            return True
        else:
            return False