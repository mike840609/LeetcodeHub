class Solution:
    def maxScore(self, A: List[int], k: int) -> int:
        preSum = [0] + list(accumulate(A))        
        
        min_ = sys.maxsize
        winSize = len(A) - k 
        
        if k == len(A): 
            return preSum[-1]
        
        # print(preSum)
        for i in range(len(preSum) - winSize):            
            # print(i+winSize, i)
            min_ = min(min_, preSum[i+winSize] - preSum[i])            
            
        return sum(A) - min_ 