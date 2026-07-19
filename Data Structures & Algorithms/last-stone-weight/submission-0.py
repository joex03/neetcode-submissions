class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we have heap ready
        # but heapify sort from small to big
        # if we multiplied the array with -ve we can use heapify
        # 2,4,8 -> -8,-4,-2
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while len(stones)>1:
            largest=-heapq.heappop(stones)
            secondlargest=-heapq.heappop(stones)
            new=largest-secondlargest
            if largest> secondlargest:
                heapq.heappush(stones,-new)
        return -heapq.heappop(stones) if len(stones)==1 else 0
