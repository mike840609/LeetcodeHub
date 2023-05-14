class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)        
        if len(nums) == 1:
            return nums[0] << k
        
        dp1 = [0] * (len(nums) +1)
        dp2 = [0] * (len(nums) +1)
        # print(nums)
        for i in range(1, len(nums) +1):
            dp1[i] = dp1[i-1] | nums[i-1]
        for i in range(len(nums)-1, -1, -1):
            dp2[i] = dp2[i+1] | nums[i]
        
        res = 0 
        for i in range(len(nums)):
            res = max(res, dp1[i] | dp2[i+1] | nums[i] << k)
        
        return res
            
        