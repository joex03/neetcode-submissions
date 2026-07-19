class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        min_heap=[]
        string=""
        if a>0:
            heapq.heappush(min_heap,(-a,"a"))
        if b>0:
            heapq.heappush(min_heap,(-b,"b"))
        if c>0:
            heapq.heappush(min_heap,(-c,"c"))
        while min_heap:
            count,char=heapq.heappop(min_heap)
            if len(string)>1 and string[-1]==string[-2]==char:
                if not min_heap:
                    break
                count2,char2=heapq.heappop(min_heap)
                string+=char2
                count2+=1
                if count2:
                    heapq.heappush(min_heap,(count2,char2))
            else:
                string+=char
                count+=1
            if count:
                heapq.heappush(min_heap,(count,char))
        return string