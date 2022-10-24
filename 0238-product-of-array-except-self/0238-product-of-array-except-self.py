class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp1 = [1]
        dp2 = [1]
        l = len(nums)
        for i in range(len(nums)):
            dp1.append(dp1[-1] * nums[i])
            dp2.append(dp2[-1] * nums[l-i-1])
        
        dp2 = dp2[::-1]
        # print(dp1)
        # print(dp2)
        res = [] 
        for i in range(len(nums)):
            res.append(dp1[i] * dp2[i+1])
        return res
            