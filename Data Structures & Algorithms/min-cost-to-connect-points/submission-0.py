class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        visited=set()
        totaldistance=0
        minheap=[(0,0)] # distnace, point index
        while len(visited)<n:
            d,i=heapq.heappop(minheap)
            if i in visited:
                continue
            totaldistance+=d
            visited.add(i)
            x,y=points[i]
            for j in range (n):
                if j not in visited:
                    a,b=points[j]
                    dis=abs(x-a)+abs(y-b)
                    heapq.heappush(minheap,(dis,j))
        return totaldistance
