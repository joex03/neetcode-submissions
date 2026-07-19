class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        mapper=defaultdict(list)
        for a,b in sorted(tickets)[::-1]:
            mapper[a].append(b)
        res=[]
        def helper(tmp):
            while mapper[tmp]:
                dst=mapper[tmp].pop()
                helper(dst)
            res.append(tmp)
        helper('JFK')
        return res[::-1]
