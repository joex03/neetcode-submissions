class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s =="" or t=="":
            return""
        tmap={}
        for c in t:
            if c in tmap:
                tmap[c]+=1
            else:
                tmap[c]=1
        smap={}
        result=""
        l=0
        size=float('inf')
        have,need=0,len(tmap)
        for r in range(len(s)):
            if s[r] in smap:
                smap[s[r]]+=1
            else:
                smap[s[r]]=1
            if s[r] in tmap and smap[s[r]]==tmap[s[r]]:
                have+=1
            while have==need:
                if (r-l+1)<size:
                    size=r-l+1
                    result=s[l:r+1]
                smap[s[l]]-=1
                if s[l] in tmap and smap[s[l]]<tmap[s[l]]:
                    have-=1
                l+=1
        return result
