class Solution:
    def maxArea(self, h: int, w: int, H: List[int], V: List[int]) -> int:
        H.sort()
        V.sort()
        
        H = [0] + H + [h]
        V = [0] + V + [w]
        
        
        hMax = max([H[i] - H[i-1] for i in range(1, len(H))])
        vMax = max([V[i] - V[i-1] for i in range(1, len(V))])
        
        # print(hMax, vMax)
        
        return hMax * vMax % (10**9+7)