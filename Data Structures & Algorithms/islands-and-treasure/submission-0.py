class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r=len(grid)
        c=len(grid[0])
        q=deque()# we will add the gates here
        v=set()
        for i in range(r):
            for j in range(c):
                    if grid[i][j]==0:
                        q.append([i,j])
                        v.add((i,j))#immutable
        distance=0
        def addcell(x,y):
            if x<0 or x >=r or y<0 or y>=c or grid[x][y]==-1 or (x,y) in v:
                return
            q.append([x,y])
            v.add((x,y))
        while q:
            for p in range(len(q)):
                i,j = q.popleft()
                grid[i][j]=distance
                addcell(i+1,j) # we add cell to q and visited
                addcell(i-1,j)
                addcell(i,j+1)
                addcell(i,j-1)
            distance+=1
        # we intialize gates with zero then add their neighbor t q to iterate on them next time and so

