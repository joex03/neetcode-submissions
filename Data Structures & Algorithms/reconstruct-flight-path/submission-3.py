class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        mapper=defaultdict(list)
        for a,b in tickets:
            mapper[a].append(b)
        for key in mapper:
            mapper[key].sort(reverse=True)
        res=[]
        def helper(src):
            while mapper[src]:
                dst=mapper[src].pop()
                helper(dst)
            res.append(src)
        helper('JFK')
        return res[::-1]
        