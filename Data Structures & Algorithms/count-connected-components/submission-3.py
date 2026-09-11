class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_to_edges = defaultdict(set)
        for first, second in edges:
            node_to_edges[first].add(second)
            node_to_edges[second].add(first)

        seen, components = set(), 0

        def helper(current, parent):
            seen.add(current)
            for edge in node_to_edges[current]:
                if edge == parent or edge in seen:
                    continue
                else:
                    helper(edge, current)

        for node in range(n):
            if node in seen:
                continue
            else:
                helper(node, None)
                components += 1
        
        return components
        