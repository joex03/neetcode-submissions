class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapper={}
        for i in range(numCourses):
            mapper[i]=[]
        for i in range(len(prerequisites)):
            course=prerequisites[i][0]
            pre=prerequisites[i][1]
            mapper[course].append(pre)
        visited=set()
        visiting=set()
        def helper(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for c in mapper[course]: # we are looping throught this course pre-req
                if not helper(c):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True
        for i in range(numCourses):
            if not helper(i):
                return False
        return True
