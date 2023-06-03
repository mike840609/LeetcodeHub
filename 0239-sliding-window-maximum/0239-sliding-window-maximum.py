# min heap => (val, idx)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        res = [] 
                        
        for i in range(len(nums)):
            
            while q and q[-1][0] < nums[i]:
                q.pop()
            
            q.append((nums[i], i))                        
            
            if i < k-1: continue
                        
            # print(q)
            if q[0][1] < i-k+1:
                q.popleft()
            
            # print(q)
            # print('-------')
            
            res.append(q[0][0])
            
        return res
        
        
                
                
                                            
            
            
                
            
            
        