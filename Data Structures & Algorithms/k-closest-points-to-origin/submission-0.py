class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        res=[]
        for x,y in points:
            dist=math.sqrt((x)**2+(y)**2)
            heapq.heappush(heap,(dist,x,y))
        for j in range(k):
            a,b,c=heapq.heappop(heap)
            res.append([b,c])
        return res
        
        