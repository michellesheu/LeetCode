class Solution:
    def romanToInt(self, s: str) -> int:
        sym_val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        
        # Iterate through the string, but be careful about the last iteration
        for i in range(len(s)):
            # If this is not the last symbol and current symbol's value is less than next symbol's
            if i < len(s) - 1 and sym_val[s[i]] < sym_val[s[i+1]]:
                total -= sym_val[s[i]]
            else:
                total += sym_val[s[i]]
        
        return total
    # def romanToInt(self, s: str) -> int:
    #     sym_val = {'I':1,'V':5,'X':10,'L':50, 'C':100, 'D':500, 'M':1000}
    #     stack = []
    #     ans = 0
    #     for i, sym in enumerate(s):
    #         print(i, sym)
    #         print(stack)
    #         if sym != 'V' or sym != 'X' or sym!='L' or sym!='C' or sym!='D' or sym!='M':
    #             stack.append(sym)
    #             ans += sym_val[sym]
    #         else:
    #             print("hi")
    #             if stack and (stack[-1] == 'I' or stack[-1]=='X' or stack[-1]=='C'):
    #                 ans -= sym_val[stack.pop()]
    #             else:
    #                 stack.append(sym)
    #                 ans += sym_val[sym]
    #         print(ans)
    #     return ans