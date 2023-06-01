# min heap => (val, idx)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        res = [] 
        
        for i in range(k-1):
            heapq.heappush(h, (-nums[i], i))
        
        for i in range(k-1, len(nums)):
            heapq.heappush(h, (-nums[i], i))
            
            v, j = heapq.heappop(h)
            v = -v
            while j < i - k + 1:
                v, j = heapq.heappop(h)
                v = -v
            
            res.append(v)
            
            if j > i-k+1:
                heapq.heappush(h, (-v, j))
        
        return res
                
            
            
        