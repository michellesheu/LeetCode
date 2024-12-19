import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def check_int(s):
            if s[0] in ('-', '+'):
                return s[1:].isdigit()
            return s.isdigit()
        for c in tokens:
            if check_int(c):
                stack.append(int(c)) 
            else:
                denom = stack.pop()
                num = stack.pop()
                if c == '+':
                    res = num + denom
                elif c == '-':
                    res = num - denom
                elif c == '/':
                    res = math.trunc(num / denom)
                else:
                    res = num * denom
                stack.append(res)
            print(stack)
        return stack[0]
    