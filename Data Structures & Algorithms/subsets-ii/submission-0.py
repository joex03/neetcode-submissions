class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        temp=[]
        def subset(i):
            if i==len(nums):
                result.append(temp.copy())
                return 
            temp.append(nums[i])
            subset(i+1)
            temp.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            subset(i+1)
        subset(0)
        return result