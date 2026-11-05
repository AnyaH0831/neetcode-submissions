class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []

        if digits == "":
            return res

        digit_to_letter = {
            2: ["a","b","c"],
            3: ["d","e","f"],
            4: ["g","h","i"],
            5: ["j","k","l"],
            6: ["m","n","o"],
            7: ["p","q","r","s"],
            8: ["t","u","v"],
            9: ["w","x","y","z"]
        }

        temp = ""
        def backtrack(i):
            nonlocal temp
            if i >= len(digits):
                res.append(temp)
                return

            current_list = digit_to_letter[int(digits[i])]
            length = len(current_list)
            for j in range(length):

                temp += current_list[j]

                backtrack(i+1)

                temp = temp[:-1]

        backtrack(0)

        return res



