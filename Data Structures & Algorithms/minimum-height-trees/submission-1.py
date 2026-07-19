class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        mapper=defaultdict(list)
        for x,y in edges:
            mapper[x].append(y)
            mapper[y].append(x)
        # we need to get the leaves then
        leaves=deque()
        # we need also to know each node has how many adj node
        edge=defaultdict(int)
        for x,y in mapper.items():
            edge[x]+=len(y)
            if len(y)==1:
                leaves.append(x)
        # we need to peel from outside till inside
        # untill we reach the center 
        while leaves:
            if n<=2:
                return list(leaves)
            for i in range(len(leaves)):
                node=leaves.popleft()
                n-=1
                for x in mapper[node]:
                    edge[x]-=1
                    if edge[x]==1:
                        leaves.append(x)