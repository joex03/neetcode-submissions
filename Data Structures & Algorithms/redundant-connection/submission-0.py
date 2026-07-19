class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[0]*(n+1)
        for i in range(n+1):
            parent[i]=i
        # [[1,2],[1,3],[3,4],[2,4]]
        # parents=[0,1,2,3,4] every node is parent of itself
        # 1 is parent of 2
        def root_find(a):
            if a==parent[a]:
                return a
            else:
                return root_find(parent[a])
        def union(a,b):
            root1=root_find(a)
            root2=root_find(b)
            if root1==root2:
                return False
            parent[root2]=root1
            return True
        for i in range(n):
            x=edges[i][0]
            y=edges[i][1]
            if not union(x,y):
                return [x,y]