class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        tmp=[]
        def helper(i):
            if i ==len(nums):
                return
            if sum(tmp)==target:
                result.append(tmp.copy())
                return
            if sum(tmp)>target:
                return
            tmp.append(nums[i])
            helper(i)
            tmp.pop()
            helper(i+1)
        helper(0)
        return result
#[2,3] target=6
        