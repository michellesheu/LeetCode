class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1+op2)
            elif t == '-':
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1-op2)
            elif t == '*':
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1*op2)
            elif t == '/':
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1/op2)
            else:
                stack.append(t)
        return stack[-1]