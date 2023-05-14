class Solution:
    def canJump(self, nums: List[int]) -> bool:
        des = 0
        for i in range(len(nums)):
            if i > des:
                return False
            des = max(des, i + nums[i])
        
        return True
        