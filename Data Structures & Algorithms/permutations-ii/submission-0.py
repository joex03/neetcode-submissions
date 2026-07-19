class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        tmp=[]
        nums.sort()
        visited=[False]*len(nums)
        def helper():
            if len(tmp)==len(nums):
                res.append(tmp.copy())
                return
            for i,n in enumerate(nums):
                if visited[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and visited[i-1]==False:
                    continue
                visited[i]=True
                tmp.append(n)
                helper()
                tmp.pop()
                visited[i]=False
        helper()
        return res
