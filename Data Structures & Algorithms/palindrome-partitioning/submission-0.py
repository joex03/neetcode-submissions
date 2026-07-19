class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        tmp=[]
        def helper(i):
            if i ==len(s):
                result.append(tmp.copy())
                return
            for j in range (i,len(s)):
                if self.palindrome(s,i,j):
                    tmp.append(s[i:j+1])
                    helper(j+1)
                    tmp.pop()
        helper(0)
        return result
    def palindrome(self,s,l,r)->bool:
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
