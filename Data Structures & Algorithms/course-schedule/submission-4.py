class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adj_list = []
        for _ in range(numCourses):
            adj_list.append([])

        for i in range(len(prerequisites)):

            if prerequisites[i][1] == prerequisites[i][0]:
                return False
            adj_list[prerequisites[i][1]].append(prerequisites[i][0])
        
        visited = set()
        def dfs(course):
            
            if course in visited:
                return False
            
            if adj_list[course] == []:
                return True
            visited.add(course)
            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            adj_list[course] = []
            return True


        for i in range(numCourses):

            if dfs(i) == False:
                return False

        return True



            
