class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {')': '(', '}': '{', ']':'['}
        stack = []

        for c in s:
            # If current char is an opening bracket
            if c in "({[":
                stack.append(c)
            else:
                # If stack is empty or doesn't match expected opening bracket
                if not stack or stack[-1] != close_open[c]:
                    return False
                # Pop the last opening bracket if matched
                stack.pop()
        
        # Check if stack is empty (all brackets matched)
        return not stack
