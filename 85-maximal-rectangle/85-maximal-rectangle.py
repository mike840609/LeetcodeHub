class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        height = [0] * (n+1)
        res = 0 
        
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            
            
            stk = [-1]
            for i in range(n+1):
                # monatic stk
                while height[i] < height[stk[-1]]:
                    h = height[stk.pop()]
                    w = i - 1 - stk[-1]
                    res = max(res, h*w)
                stk.append(i)
        return res 