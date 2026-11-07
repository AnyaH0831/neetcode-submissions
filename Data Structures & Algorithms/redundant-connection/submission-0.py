class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        adj = []
        for _ in range(len(edges)+1):
            adj.append([])

        for ai, bi in edges:
            adj[ai].append(bi)
            adj[bi].append(ai)

        visit = [False]*(n+1)
        cycle = set()
        start = -1

        def dfs(node, par):
            nonlocal cycle, start, visit

            if visit[node]:
                start = node
                return True

            visit[node] = True
            for neigh in adj[node]:
                if neigh == par:
                    continue
                if dfs(neigh, node):
                    if start != -1:
                        cycle.add(node)
                    if node == start:
                        start = -1
                    return True
            return False
        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []

