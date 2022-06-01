class Solution:
    def dailyTemperatures(self, A: List[int]) -> List[int]:
        n = len(A)
        res = [0]*n
        stk = [] 
        for i in range(n):
            while stk and A[i] > A[stk[-1]]:
                j = stk.pop()
                res[j] = i-j
            stk.append(i)
        return res