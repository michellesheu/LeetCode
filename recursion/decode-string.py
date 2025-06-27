class Solution:
    def decodeString(self, s: str) -> str:
        # make list to store res str
        # use stack with chars to keep track of closing bracket to pop chars inside [] 
        # add popped char into list left to right
        # once encounter [ keep track of digits
        # multiply k digits to list
        # return list as str
        stack = []
        curr = ''
        k = ''
        for ch in s:
            print(f"ch: {ch}")
            if ch == ']':
                curr = ''
                while stack and stack[-1] != '[':
                    curr = stack.pop() + curr
                print(f"substring: {curr}")
                stack.pop()
                print(f"stack before k: {stack}")
                print(f"res before k: {res}")
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                print(f"k: {int(k)}")
                # res = int(k) * res
                curr = int(k) * curr
                stack.append(curr)
                print(f"res after k: {res}")
            else:
                stack.append(ch)
            print(f"stack: {stack}")
            print(f"res: {res}")
            print("-------------")
        return "".join(stack)
            