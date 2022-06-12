class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        dp = [0] * k
        res = sys.maxsize
        
        def dfs(i):
            nonlocal dp 
            nonlocal res 
            
            if i == len(cookies):                
                res = min(res, max(dp))
                return                         
            
            for j in range(len(dp)):
                if dp[j] + cookies[i] < res:
                    dp[j] += cookies[i]                
                    dfs(i+1)
                    dp[j] -= cookies[i]
        dfs(0)
        return res 
                
        