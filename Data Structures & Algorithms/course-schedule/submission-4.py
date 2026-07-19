class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapper=defaultdict(list)
        for a,b in prerequisites:
            mapper[b].append(a)
        visiting=set()
        def helper(node):
            if mapper[node]==[]:
                return True
            if node in visiting:
                return False
            visiting.add(node)
            # this means we found the cycle
            for x in mapper[node]:
                #we'll loop on the pres if node appeared twice then cycle detected
                if not helper(x):
                    return False
            visiting.remove(node)
            return True
        for i in range(numCourses):
            if not helper(i):
                return False
        return True