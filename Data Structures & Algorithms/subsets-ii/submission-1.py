class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        temp=[]
        def subset(i):
            if i==len(nums) and temp not in result:
                result.append(temp.copy())
                return 
            if i==len(nums):
                return
            temp.append(nums[i])
            subset(i+1)
            temp.pop()
            subset(i+1)
        subset(0)
        return result