class Solution:
    def longestPalindrome(self, s: str) -> str:
        result=""
        length=0
        for i in range (len(s)):
            #odd
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>length:# why +1 "a" has length 1 r=l so r-l=0 so plus 1
                    length=r-l+1
                    result=s[l:r+1]
                l-=1
                r+=1
            #even
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>length:
                    length=r-l
                    result=s[l:r+1]
                l-=1
                r+=1
        return result