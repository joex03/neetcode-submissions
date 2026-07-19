class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=defaultdict(int)
        for t in tasks:
            freq[t]+=1
        max_frequency=max(freq.values())
        count=0
        for i in freq.values():
            if i==max_frequency:
                count+=1
        return max((max_frequency-1)*(n+1)+count,len(tasks))