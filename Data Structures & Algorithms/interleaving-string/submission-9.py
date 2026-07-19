class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        memo={}
        def helper(i,j,k):
            if i==len(s1) and j==len(s2) and k==len(s3):
                return True
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            ans=False
            if i<len(s1) and s1[i]==s3[k]:
                ans=ans or helper(i+1,j,k+1)
            if j<len(s2) and s2[j]==s3[k]:
                ans=ans or helper(i,j+1,k+1)
            memo[(i,j,k)]=ans
            return ans
        return helper(0,0,0)
            