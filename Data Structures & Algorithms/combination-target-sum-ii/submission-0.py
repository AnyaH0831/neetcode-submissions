class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        candidates.sort()
        res = []

        def dfs(i, current, total):

            if total == target:
                res.append(current.copy())
                return

            # if total > target:
            #     return

            
            for j in range(i, len(candidates)):

                if j>i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] + total > target:
                    return 
                
                current.append(candidates[j])

                dfs(j+1, current, total+candidates[j])

                current.pop()

        dfs(0,[],0)

        return res
