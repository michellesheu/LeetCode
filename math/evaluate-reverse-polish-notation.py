import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c)) 
            else:
                denom = stack.pop()
                num = stack.pop()
                if c == '+':
                    res = num + denom
                elif c == '-':
                    res = num - denom
                elif c == '/':
                    res = int(num / denom)
                else:
                    res = num * denom
                stack.append(res)
        return stack[0]
    