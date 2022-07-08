class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
		# You can use this functools line instead of dp to make it faster, but I cache 
		# manually because I don't want to abstract the caching away from the reader.
        
        @lru_cache(None)
        def dfs(i, t, p):             
            
            if t < 0 or m-i < t:
                return float('inf')
            
            if i == len(houses):
                # base case - we're trying to color 0 houses. Only i == len(houses) is necessary
				# to check here, but it prunes a bit of the search space to make things faster.
                return 0 if t == 0 and i == len(houses) else float('inf')
            
            
            if houses[i] == 0:
                res = float('inf')
                for nc in range(1, n + 1):
                    res = min(res, dfs(i + 1, t - (nc != p), nc) + cost[i][nc - 1])
                return res 
            
            else:            
                return dfs(i + 1, t - (houses[i] != p), houses[i])                            
            
        ret = dfs(0, target, -1)
        # if ret is infinity, then we failed every case because there were too many neighborhoods
        # to start. If we could paint over houses that were previously painted, we could remedy that,
        # but the problem doesn't allow that. so, we return -1 in that case.
        return ret if ret < float('inf') else -1