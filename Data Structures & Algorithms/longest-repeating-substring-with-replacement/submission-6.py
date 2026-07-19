class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxx=float('-inf')
        l=0
        mapper={}
        for r in range(len(s)):
            if s[r] in mapper:
                mapper[s[r]]+=1
            else:
                mapper[s[r]]=1
            if (r-l+1)-max(mapper.values())<=k:
                maxx=max(r-l+1,maxx)
            if (r-l+1)-max(mapper.values())>k:
                mapper[s[l]]-=1
                l+=1

        return maxx

            