class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # we need to know the base case
        # the last row all cols has only 1 way to reach the end
        # the m-2 row
        row=[1]*n
        for i in range(m-2,-1,-1): #iterate row
            tmp=[1]*n 
            for j in range (n-1,-1,-1):
                if j==n-1:
                    tmp[j]=row[j]
                else:
                    tmp[j]=row[j]+tmp[j+1]
            row=tmp
        return row[0]
        