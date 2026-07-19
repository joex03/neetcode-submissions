class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        memo={n:1} # [1,2,3] 3 has only 1 way won't work in case of [1,2,0]
        def dfs(i)->int:
            ressult=0
            if i in memo:
                return memo[i]
            if s[i]=='0':
                return 0
            result=dfs(i+1)
            if i+1<len(s) and ((s[i]=='1') or (s[i]=='2' and s[i+1]>='0' and s[i+1]<='6')):
                result+=dfs(i+2)
            memo[i]=result
            return result
        return dfs(0)