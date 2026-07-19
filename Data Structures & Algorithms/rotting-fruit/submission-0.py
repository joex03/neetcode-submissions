class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        fresh=0
        rotten=deque()
        for r in range (row):
            for c in range (col):
                if grid[r][c]==1: 
                    fresh+=1
                if grid[r][c]==2:
                    rotten.append((r,c))
        if fresh==0:
            return 0
        mint=-1
        while rotten:
            mint+=1
            for t in range(len(rotten)):
                (i,j)=rotten.popleft()
                for r,c in [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]:
                    if 0<=r<row and 0<=c<col and grid[r][c]==1:
                        fresh-=1
                        grid[r][c]=2
                        rotten.append((r,c))
        if fresh==0:
            return mint
        else:
            return -1

