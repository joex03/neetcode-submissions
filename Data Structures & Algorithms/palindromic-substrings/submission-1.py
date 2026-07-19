class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        matrix=[]
        n=len(s)
        for i in range (n):
            temp=[0]*n
            matrix.append(temp)
        for i in range (n):
            matrix[i][i]=1
            count+=1
        for c in range (1,n):# we have options first 1 pal is in length 2
            for r in range (c):
                if r==c-1 and s[c]==s[r]:
                    matrix[r][c]=1
                    count+=1
                elif matrix[r+1][c-1]==1 and s[r]==s[c]:
                    matrix[r][c]=1
                    count+=1

        return count