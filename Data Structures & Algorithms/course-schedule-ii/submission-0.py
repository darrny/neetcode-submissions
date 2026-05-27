class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        do = {i : [] for i in range(numCourses)}
        d = [0] * numCourses
        for a, b in prerequisites:
            do[b].append(a)
            d[a] += 1
        q = deque()
        for i in range(numCourses):
            if d[i] == 0:
                q.append(i)

        res = []
        complete = 0

        while q:
            curr = q.popleft()
            complete += 1
            res.append(curr)
            for dependent in do[curr]:
                d[dependent] -= 1
                if d[dependent] == 0:
                    q.append(dependent)
        
        if complete == numCourses:
            return res
        else:
            return []