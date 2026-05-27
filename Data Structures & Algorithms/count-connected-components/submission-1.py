class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ed = { i : [] for i in range(n)}
        visited = set()
        for edge1, edge2 in edges:
            ed[edge1].append(edge2)
            ed[edge2].append(edge1)

        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for e in ed[node]:
                if e == parent:
                    continue
                dfs(e, node)

        components = 0
        for i in range(n):
            if i in visited:
                continue
            components += 1
            dfs(i, -1)

        return components