class Solution:
    def wiggleMaxLength(self, A: List[int]) -> int:
        length = 1
        up = None # current is increasing or not
        
        for i in range(1, len(A)):
            
            if A[i] > A[i - 1] and up != True:
                length += 1
                up = True
                
            if A[i] < A[i - 1] and up != False:
                length += 1
                up = False
                
        return length