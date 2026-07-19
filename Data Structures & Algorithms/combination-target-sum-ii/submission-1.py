class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        tmp=[]
        candidates.sort()
        def helper(i):
            if sum(tmp)==target:
                result.append(tmp.copy())
                return
            if i==len(candidates):
                return

            if sum(tmp)>target:
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                tmp.append(candidates[j])
                helper(j+1)
                tmp.pop()
        helper(0)
        return result
            