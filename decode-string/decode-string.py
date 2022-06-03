class Solution:
    def decodeString(self, s: str) -> str:
        stk, num, curStr = [], 0, ''
        
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '[':
                stk.append((curStr, num))
                curStr = ''
                num = 0
            elif c == ']':
                prevStr, prevNum = stk.pop()
                curStr = prevStr + prevNum*curStr
            else:
                curStr += c
        return curStr