class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numberOfDependencies = [0] * numCourses
        courseDependentOn = {i : [] for i in range(numCourses)}
        for a, b in prerequisites:
            courseDependentOn[b].append(a)
            numberOfDependencies[a] += 1
        
        queue = deque()
        for i in range(numCourses):
            if numberOfDependencies[i] == 0:
                queue.append(i)

        complete = 0
        while queue:
            currentCourse = queue.popleft()
            complete += 1
            for dependent in courseDependentOn[currentCourse]:
                numberOfDependencies[dependent] -= 1
                if numberOfDependencies[dependent] == 0:
                    queue.append(dependent)

        return complete == numCourses