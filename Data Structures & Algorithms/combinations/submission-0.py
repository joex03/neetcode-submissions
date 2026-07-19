class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        tmp=[]
        def helper(num):
            if len(tmp)==k:
                res.append(tmp.copy())
                return
            if num>n:
                return
            tmp.append(num)
            helper(num+1)
            tmp.pop()
            helper(num+1)
        helper(1)
        return res