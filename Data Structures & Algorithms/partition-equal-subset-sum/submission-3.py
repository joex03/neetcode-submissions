class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        target=sum(nums)//2
        dp=set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            tmp=dp.copy()
            for j in dp:
                tmp.add(nums[i]+j)
            dp=tmp
        for j in dp:
            if j==target:
                return True
        return False
