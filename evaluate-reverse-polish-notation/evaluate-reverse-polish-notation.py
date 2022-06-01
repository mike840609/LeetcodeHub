class Solution:
    def evalRPN(self, A: List[str]) -> int:
        stk = []
        for c in A:
            if c in '+-*/':
                b = stk.pop()
                a = stk.pop()
                stk.append(str(int(eval(a+c+b))))
            else:
                stk.append(c)
        return int(stk.pop())