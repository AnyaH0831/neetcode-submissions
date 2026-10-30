class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = {}
        for i in range(n):
            adj_list[i] = []

        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        visited = set()
        counter = 0
        def dfs(node):

            

            if adj_list[node] == []:
                return
            if node in visited:
                return
            visited.add(node)
            for neighbour in adj_list[node]:
                dfs(neighbour)

        idx = 0
        while idx < n:

            if idx not in visited:
                counter += 1
                dfs(idx)
            
            idx += 1

        return counter

