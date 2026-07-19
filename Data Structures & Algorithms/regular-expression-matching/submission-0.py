class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo={}
        def helper(i,j):
            if j==len(p) and i ==len(s):
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            matchy= (j<len(p) and  i <len(s)) and (s[i]==p[j] or p[j]=='.')
            # handle the wild card
            # 2 possible cases
            #case 1 : s=a     p=ab* we will skip b* so counter +2
            #case 2 : s=aaa   p=a* we will use it so move i counter only 
            if j+1<len(p) and p[j+1]=='*':
                memo[(i,j)]= helper(i,j+2) or (matchy and helper(i+1,j))
                return memo[(i,j)]
            if matchy:
                memo[(i,j)]= helper(i+1,j+1)
                return memo[(i,j)]
            return False
        return helper(0,0)