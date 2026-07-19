class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited=set()
        visiting=set()
        result=[]
        mapper={}
        for i in range (numCourses):
            mapper[i]=[]
        for i in range (len(prerequisites)):
            crs=prerequisites[i][0]
            pre=prerequisites[i][1]
            mapper[crs].append(pre)
        def helper(i):
            if i in visiting:
                return False
            if i in visited:
                return True
            visiting.add(i)
            for c in mapper[i]:
                if not helper(c):
                    return False
            visiting.remove(i)
            visited.add(i)
            result.append(i)
            return True # in case course has no pre-req
        for i in range(numCourses):
            if not helper(i):
                return []
        return result

