class Solution:
    def isValid(self, s: str) -> bool:
        #stack check if curr is open push on stack if curr is closed then pop off top if it's open continue else return False return false is stack not empty O(n) time O(n) space
        close_open = {')':"(", ']':'[', '}':'{'}
        stack = []
        for ch in s:
            if ch not in close_open:
                stack.append(ch)
            elif ch in close_open:
                if not stack:
                    return False
                top = stack[-1]
                if top != close_open[ch]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0 