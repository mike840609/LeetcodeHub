# can we early break? no, consider case: k == 1
# no need to compare full subarray, compare current number and previous gcd number is good enough.
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0 
        for i, n in enumerate(nums):
            gcd = n 
            for j in range(i, len(nums)):
                gcd = math.gcd(gcd, nums[j])                                
                if gcd == k:
                    # print(nums[i:j+1])
                    res += 1
        return res 
                
            
        