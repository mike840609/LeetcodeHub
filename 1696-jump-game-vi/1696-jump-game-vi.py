class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        d = deque([(nums[0], 0)])
        
        for i in range(1, len(nums)):
            dp[i] = nums[i] + d[0][0]
            
            # the queue is a mono queue, decreasing
            while d and d[-1][0] < dp[i]: 
                d.pop()
            d.append([dp[i], i])
            
            # expired step, we couldn't reach the next step from the idx d[0][1]
            if d[0][1] == i-k : 
                d.popleft()
                
        return dp[-1]
            
                    