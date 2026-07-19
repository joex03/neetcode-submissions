class Solution:
    def reorganizeString(self, s: str) -> str:
        mapper=defaultdict(int)
        for c in s:
            mapper[c]+=1
        minHeap=[]
        for key in mapper:
            heapq.heappush(minHeap,(-mapper[key],key))
        string=""
        while minHeap:
            counter,char=heapq.heappop(minHeap)
            if len(string)>0 and string[-1]==char:
                if not minHeap:
                    return ""
                counter2,char2=heapq.heappop(minHeap)
                string+=char2
                counter2+=1
                if counter2:
                   heapq.heappush(minHeap,(counter2,char2)) 
            else:
                string+=char
                counter+=1
            if counter:
                heapq.heappush(minHeap,(counter,char))

        return string if len(string)==len(s) else ""        