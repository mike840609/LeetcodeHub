class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        a, b = [], []
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i][j]: a.append((i,j))
                if B[i][j]: b.append((i,j))
                    
        ans = 0
        for x1, y1 in a:
            for x2, y2 in b:
                shift_x, shift_y = (x1-x2, y1-y2)
                
                d[(shift_x, shift_y)] += 1
                ans = max(ans, d[(shift_x, shift_y)])
        
        return ans
                
                
                