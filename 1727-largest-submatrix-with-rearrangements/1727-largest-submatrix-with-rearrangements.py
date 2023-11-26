class Solution:
    def largestSubmatrix(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        h = [0] * n
        res = 0 
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0 : h[j] = 0
                else:
                    h[j] += 1
            
            sort_h = sorted(h)
            
            for i in range(n):
                res = max(res, sort_h[i] * (n -i))
        
        return res
                
                