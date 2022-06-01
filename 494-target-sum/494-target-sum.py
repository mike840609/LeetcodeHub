class Solution:
   #DFS + memo
   def findTargetSumWays(self, nums: List[int], S: int) -> int:
       memo = {}
       def dfs(i,summary):
           if i == len(nums):
               if summary == S:
                   memo[(i,summary)] = 1
               else:
                   memo[(i,summary)] = 0
           if (i,summary) not in memo:   
               memo[(i,summary)] = dfs(i+1,summary+nums[i]) + dfs(i+1,summary-nums[i])
           return memo[(i,summary)]
       dfs(0,0)
       return memo[(0,0)]     
            
        