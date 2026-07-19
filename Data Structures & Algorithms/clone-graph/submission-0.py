"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        mapper={}
        def dfs(nod):
            if nod in mapper:
                return mapper[nod]
            copy=Node(nod.val)
            mapper[nod]=copy
            for n in nod.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node)
        