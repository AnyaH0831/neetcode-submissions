class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # {0:[1,2], 1:[], 2:...}

        valid = set()
        valid_array = []
        visited = set()
        def dfs(course):

            if course in visited:
                # valid_array = []
                return False
            if preMap[course] == []:

                if course not in valid:
                    valid.add(course)
                    valid_array.append(course)
                return True

            visited.add(course)
            for crs in preMap[course]:
                if dfs(crs) == False:
                    # valid_array = []
                    return False

            preMap[course] = []
            visited.remove(course)
            if course not in valid:
                valid.add(course)
                valid_array.append(course)
            return True
            
        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return valid_array



