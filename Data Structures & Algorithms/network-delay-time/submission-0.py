class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mapper=defaultdict(list)
        for a,b,c in times:
            mapper[a].append((b,c))
        visited=set()
        time=0
        heap=[(0,k)]
        while heap:
            w1, n1 = heapq.heappop(heap) 
            if n1 in visited:
                continue
            visited.add(n1)
            time = max(time, w1) 
            for n2, w2 in mapper[n1]:
                if n2 not in visited:
                    heapq.heappush(heap, (w1 + w2, n2))
        if len(visited)==n:
            return time
        return -1