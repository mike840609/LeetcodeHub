class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        dp = (max(nums)+1) * [0]
        
        for n in nums:
            dp[n] += 1
        
        acc = [0] + list(accumulate(dp)) 
                
        res = 0 
        for i in range(len(acc)):            
            tmp = acc[min(len(acc)-1, i+k+1)] - acc[max(0, i-k)]
            res = max(res, tmp)
        return res