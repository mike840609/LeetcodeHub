class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        
        odd_dp, even_dp = 0, 0         
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] & 1:
                odd_dp = max(even_dp + nums[i] - x, odd_dp + nums[i])                
                
            elif nums[i] & 1 == 0:
                even_dp = max(odd_dp + nums[i] - x, even_dp + nums[i])
                        
        return odd_dp if nums[0] & 1 else even_dp
        
        