class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        tmp=[]
        def helper():
            if len(tmp)==len(nums):
                result.append(tmp.copy())
                return
            for n in nums:
                if n not in tmp:
                    tmp.append(n)
                    helper()
                    tmp.pop()
        helper()
        return result