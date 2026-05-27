class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        ed = {i : [] for i in range(n)}
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            ed[node1].append(node2)
            ed[node2].append(node1)

        def dfs(node, par):
            if node in visited:
                return False
            visited.add(node)
            for link in ed[node]:
                if link == par:
                    continue
                if not dfs(link, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n