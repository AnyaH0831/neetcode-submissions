class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        res = []
        def backtrack(temp, open_count, close_count):

            if len(temp) == 2*n:
                res.append(temp)
                return

            if open_count < n:
                if open_count > close_count:

                    temp += ")"
                    backtrack(temp, open_count, close_count+1)
                    temp = temp[:-1]
                    temp += "("
                    backtrack(temp, open_count+1, close_count)
                elif open_count == close_count:
                    temp += "("
                    backtrack(temp, open_count+1, close_count)

            elif open_count == n:
                if open_count > close_count:
                    temp += ")"
                    backtrack(temp, open_count, close_count+1)
            elif open_count == close_count:
                temp += "("
                backtrack(temp, open_count+1, close_count)


        backtrack("",0,0)
        return res

