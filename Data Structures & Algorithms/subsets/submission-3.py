class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result,tmp=[],[]
        def helper(i)->int:
            if i ==len(nums):
                result.append(tmp.copy())
                return
            tmp.append(nums[i])
            helper(i+1)
            tmp.pop()
            helper(i+1)
        helper(0)
        return result