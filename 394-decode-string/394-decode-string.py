class Solution(object):
    def decodeString(self, s):
        stk, num, cur = [], 0, ''
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c =='[':
                stk.append([num, cur])
                num = 0
                cur = ''
            elif c == ']':
                pre_num, pre_s = stk.pop()
                cur  = pre_s + pre_num *cur
            else:
                cur += c
        return cur