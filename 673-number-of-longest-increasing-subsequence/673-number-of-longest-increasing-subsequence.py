'''
dp => the length of the Longest Increasing Subsequence which ends with nums[i].
cnt => the number of the Longest Increasing Subsequence which ends with nums[i].
'''
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        cnt = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1 :
                        dp[i] = dp[j] + 1 
                        cnt[i] = cnt[j]
                    elif dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]
                        
                        
        maxLen = max(dp)
        
        return sum(cnt[i] if n == maxLen else 0 for i, n in enumerate(dp))
                        
                        
                    
         