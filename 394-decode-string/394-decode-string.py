class Solution:
    def decodeString(self, s: str) -> str:
        stk, num, curStr = [], 0, ''
        
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == '[':
                stk.append((num, curStr))
                num = 0 
                curStr = ''
            elif c == ']':
                preNum, preStr = stk.pop()
                curStr = preStr + preNum * curStr
            else:
                curStr += c
            # print(stk, curStr)
                
        return curStr