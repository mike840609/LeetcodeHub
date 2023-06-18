class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n, MOD = len(nums), 10**9 + 7
        
        @cache
        def dfs(prev, mask):
            if mask == ((1 << n) - 1):
                return 1 
            cnt = 0 
            for i in range(n):
                if ((1 << i) & mask) == 0 and (prev % nums[i] == 0 or nums[i] % prev == 0):
                    cnt += dfs(nums[i], mask | 1<<i)
            
            return cnt % MOD
            
        return dfs(1, 0)
        