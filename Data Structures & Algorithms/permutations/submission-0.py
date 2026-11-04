class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(temp, visit):

            if len(temp) == len(nums):
                res.append(temp.copy())

                return

            # while len(temp) < len(nums):

            for i in range(len(visit)):

                if visit[i] == 0:

                    temp.append(nums[i])
                    visit[i] = 1

                    backtrack(temp,visit)

                    temp.pop()
                    visit[i] = 0


        visit = [0]*len(nums)

        backtrack([],visit)
        return res
            

            