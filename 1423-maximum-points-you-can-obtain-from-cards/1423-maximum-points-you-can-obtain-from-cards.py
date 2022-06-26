'''
what is remove from head or tail  `n` times to make it sum maximum means?

=> the sum of remain subArray must be minimum

=> using `prefix sum` and `sliding windows` to solve this problem

'''
class Solution:
    def maxScore(self, A: List[int], k: int) -> int:
        
        preSum = [0] + list(accumulate(A))                
        
        min_ = sys.maxsize
        
        winSize = len(A) - k 
        
        if k == len(A): 
            return preSum[-1]
           
        for i in range(len(preSum) - winSize):              
            min_ = min(min_, preSum[i+winSize] - preSum[i])            
            
        return sum(A) - min_ 
    