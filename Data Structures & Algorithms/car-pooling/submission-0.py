class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        current=0
        minHeap=[]
        trips.sort(key=lambda r:r[1]) #we will sort based on src
        for a,b,c in trips:
            while minHeap and b>=minHeap[0][0]: # then nazel el rokab
                current-= minHeap[0][1]
                heapq.heappop(minHeap)
            if (current+a) >capacity:
                return False
            current+=a
            heapq.heappush(minHeap,(c,a))
        return True
