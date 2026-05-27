class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for src, dst, time in times:
            edges[src].append((time, dst))
        visited = set()
        minheap = []

        time = 0
        heapq.heappush(minheap, (0, k))

        while minheap:
            t, curr = heapq.heappop(minheap)         
            if curr in visited:
                continue
            visited.add(curr)
            time = t
            for newTime, dst in edges[curr]:
                heapq.heappush(minheap, (newTime + time, dst))

        return time if len(visited) == n else -1