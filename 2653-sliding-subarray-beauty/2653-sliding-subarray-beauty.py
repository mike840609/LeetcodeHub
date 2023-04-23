class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:

        dp = Counter()                
        res = [] 
        for idx, n in enumerate(nums):
            pre_idx = idx - k
            dp[n] += 1
            if pre_idx >= 0 and idx >= k:
                dp[nums[pre_idx]] -= 1
                if dp[nums[pre_idx]] == 0 :
                    del dp[nums[pre_idx]]
            
            if idx >= k - 1:
                cnt = 0 
                for i in range(-50, 51):
                    cnt += dp[i]                     
                    if cnt >= x:
                        break
                        

                res.append(min(i, 0))



                    
                        
        return res
                