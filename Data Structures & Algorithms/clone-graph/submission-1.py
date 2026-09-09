"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_mapping = defaultdict(list)
        new_mapping = {}    # map from value to the newly created node

        def dfs(node):
            if node.val in old_mapping:
                return
            else:
                new_mapping[node.val] = Node(val = node.val)
                
                for neighbor in node.neighbors:
                    old_mapping[node.val].append(neighbor.val)
                    dfs(neighbor)

        dfs(node)



        for value, neighbors in old_mapping.items():
            for neighbor in neighbors:
                new_mapping[value].neighbors.append(new_mapping[neighbor])

        return new_mapping[1]