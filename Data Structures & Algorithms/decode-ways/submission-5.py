class Solution:
    def numDecodings(self, s: str) -> int:
        memo={len(s):1}
        if len(s)==1 and s=='0':
            return 0
        def helper(i)->int:
            result=0
            if i in memo:
                return memo[i]
            if s[i]=='0':
                return 0
            result=helper(i+1)
            if i<len(s)-1 and (s[i]=='1' or (s[i]=='2' and s[i+1]<='6')):
                    result+=helper(i+2)
                    memo[i]=result
            return result
        return helper(0)