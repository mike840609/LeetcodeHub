class Solution:
    def maxArea(self, h: int, w: int, H: List[int], V: List[int]) -> int:
        H.sort()
        V.sort()
        
        H = [0] + H + [h]
        V = [0] + V + [w]    
            
        hMax = self.getMaxDiff(H)
        vMax = self.getMaxDiff(V)
        
        # print(hMax, vMax)        
        return hMax * vMax % (10**9+7)
    
    def getMaxDiff(self, A):
        res = 0
        for i in range(1, len(A)):
            if A[i] - A[i-1] > res:
                res = A[i] - A[i-1]
        return res