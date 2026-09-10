class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        node_to_connected_nodes = {i: set() for i in range(n)}

        for a, b in edges:
            node_to_connected_nodes[a].add(b)
            node_to_connected_nodes[b].add(a)

        seen = set()

        def dfs(curr, parent):
            if curr in seen:
                return False
            else:
                seen.add(curr)
                for connected_node in node_to_connected_nodes[curr]:
                    if connected_node == parent:
                        continue
                    else:
                        if not dfs(connected_node, curr):
                            return False
                return True

        return dfs(0, None) and len(seen) == n