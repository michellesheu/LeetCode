class Solution:
    def isValid(self, s: str) -> bool:
        # input: a string of brackets
        # output: true if 1. closed by same type 2. closed in correct order 3. every close bracket has same open bracket type
        # m: stack problem to keep track of last bracket popped is closing for ch in s check if stack is not empty and what the top of the stack is and see if it matches if not return false add opening brackets to stack, if stack is empty in the end return true else return false bc that means opening brackets still inside
        stack = []
        for parenthesis in s:
            print(f'{parenthesis=}')
            if parenthesis == '(' or parenthesis == '[' or parenthesis == '{':
                stack.append(parenthesis)
                print(f'{stack=}')
            elif not stack:
                return False
            else:
                top = stack.pop()
                print(f"{top=}")
                if top == '(' and parenthesis != ')':
                    return False
                elif top == '[' and parenthesis != ']':
                    return False
                elif top == '{' and parenthesis != '}':
                    return False
        print(stack)
        return True if not stack else False
