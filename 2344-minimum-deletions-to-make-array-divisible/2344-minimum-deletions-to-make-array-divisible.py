class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        
        x = reduce(gcd, numsDivide)
        
        res = 0 
        for n in nums:
            if x%n == 0 :
                return res 
            res += 1 
    
        return -1