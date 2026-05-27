class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        currVisited = set()

        def dfs(course):
            if preMap[course] == []:
                return True
            if course in currVisited:
                return False
            currVisited.add(course)
            prereqList = preMap[course]
            for prereq in prereqList:
                if prereq in currVisited:
                    return False
                if not dfs(prereq):
                    return False
            return True

        for course in range(numCourses):
            currVisited.clear()
            if not dfs(course):
                return False
        return True