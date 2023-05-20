class Solution:
    def sortedSquares(self, A):
        res = collections.deque()        
        l, r = 0, len(A)-1
        
        while l <= r :
            lVal, rVal = A[l]**2, A[r]**2
            
            if lVal > rVal:
                res.appendleft(lVal)
                l += 1
            else:
                res.appendleft(rVal)
                r -= 1
        return res