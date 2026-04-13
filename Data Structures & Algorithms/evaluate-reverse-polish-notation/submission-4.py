import math 
class Solution:

    def is_int(self, n):
        
        try:
            int(n)
            return True
        except ValueError: 
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for i in range(len(tokens)):

            cur = tokens[i]

            if self.is_int(cur):
                stack.append(int(cur))
            else:
                # print(stack)
                a = stack[-2]
                b = stack[-1]
                stack.pop()
                stack.pop()

                if cur == "+":
                    stack.append(a+b)
                elif cur == "-":
                    stack.append(a-b)
                elif cur == "*":
                    stack.append(a*b)
                else:
                    if (a < 0 and b < 0) or (a>0 and b>0):
                        stack.append(a//b)
                    else: 
                        # print(a, b)
                        stack.append(math.ceil(a/b))


        return stack[0]