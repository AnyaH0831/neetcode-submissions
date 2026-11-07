class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = []
        for _ in range(n):
            adj.append([])
        for i in range(len(edges)):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])

        visit = set()

        def dfs(node, par):

            if node in visit:
                return False

            visit.add(node)

            for neigh in adj[node]:
                if neigh == par:
                    continue

                if not dfs(neigh, node):
                    return False
            return True

        if len(edges) > n-1:
            return False

        return dfs(0,-1) and len(visit) == n