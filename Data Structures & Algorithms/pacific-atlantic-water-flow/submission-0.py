class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pac=set()
        at=set()
        def dfs(x,y,sett,prev):
            if x<0 or y<0 or x>=rows or y>=cols or (x,y) in sett or heights[x][y]<prev:
                return
            sett.add((x,y))
            dfs(x+1,y,sett,heights[x][y])
            dfs(x-1,y,sett,heights[x][y])
            dfs(x,y+1,sett,heights[x][y])
            dfs(x,y-1,sett,heights[x][y])
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,at,heights[r][cols-1])
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,at,heights[rows-1][c])
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in at:
                    res.append([r,c])
        return res

        