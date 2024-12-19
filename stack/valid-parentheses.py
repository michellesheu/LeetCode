class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {')': '(', '}': '{', ']':'['}
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                print(stack[-1], close_open[c])
                while stack and stack[-1] == close_open[c]:
                    stack.pop()
                
            print("stack: ", stack)
        return True if not stack else False