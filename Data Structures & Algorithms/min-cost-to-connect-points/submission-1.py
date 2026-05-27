class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                point1, point2 = points[i], points[j]
                dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                edges[i].append((dist, j))
                edges[j].append((dist, i)) 

        res = 0
        minheap = [(0, 0)]
        visited = set()

        while minheap:
            dist, curr = heapq.heappop(minheap)
            if curr in visited:
                continue
            res += dist
            visited.add(curr)
            for edgeCost, edgeNode in edges[curr]:
                heapq.heappush(minheap, (edgeCost, edgeNode))

        return res
