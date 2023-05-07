class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:

        self.res = 0 

        def dfs(i):
            if i >= n :
                return 0 
            
            l = dfs((i+1)*2 -1)
            r = dfs((i+1)*2)
            
            self.res += abs(l-r)
            
            # we can only increase the number but not decrease
            return cost[i] + max(l,r)
            
        dfs(0)        
        return self.res