class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {}
        for i in range(numCourses):
            preMap[i] = []

        for courses, prereq in prerequisites:
            preMap[courses].append(prereq)
# {course:[prereq1,prereq2,...], course2: [],...}
        visiting = set()
        # {}
        def dfs(courses):
            if courses in visiting:
                return False

            if preMap[courses] == []:
                return True

            visiting.add(courses)
            # run dfs on the prereq of the current course
            for pre in preMap[courses]:
                if not dfs(pre): #if the prereq return false then we return false
                    return False
            visiting.remove(courses)
            preMap[courses] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
