class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        tmp=[]
        candidates.sort()
        def helper(i):
            if sum(tmp)==target and tmp not in result:
                result.append(tmp.copy())
                return
            if i==len(candidates):
                return
            if sum(tmp)>target:
                return
            tmp.append(candidates[i])
            helper(i+1)
            tmp.pop()
            helper(i+1)
        helper(0)
        return result
            