class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(node):
            if par[node] == node:
                return node
            else:
                par[node] = find(par[node])
                return par[node]

        def union(node1, node2):
            par1 = find(node1)
            par2 = find(node2)
            if par1 == par2:
                return False
            if rank[par1] > rank[par2]:
                par[par2] = par1
                rank[par1] += rank[par2]
            else:
                par[par1] = par2
                rank[par2] += rank[par1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]