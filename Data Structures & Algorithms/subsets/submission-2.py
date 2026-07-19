class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        temp=[]
        def leaf(i):
            if i == len(nums):
                result.append(temp.copy())
                return
            temp.append(nums[i])
            leaf(i+1)
            temp.pop()
            leaf(i+1)
        leaf(0)
        return result
        