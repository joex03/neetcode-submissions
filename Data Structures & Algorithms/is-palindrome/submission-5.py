class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        temp=""
        for c in s:
            if c.isalnum():
                temp+=c
        left=0
        right=len(temp)-1

        while left<right:
            if temp[left]!=temp[right]:
                return False
            else:
                left+=1
                right-=1
        return True

        