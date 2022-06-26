class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 +7
        m = [[4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [7, 1, 0],
            [6, 2],
            [1, 3],
            [4, 2]] 
        
        dp0 = [0] * 10 
        dp1 = [0] * 10
        
        for i in range(10):
            dp1[i] = 1
            
        for _ in range(n-1):
            dp0 = dp1[::]
            
            for i in range(10):
                dp1[i] = 0
            for i in range(10):
                for x in m[i]:
                    dp1[x] += dp0[i]

        return sum(dp1) % mod
                