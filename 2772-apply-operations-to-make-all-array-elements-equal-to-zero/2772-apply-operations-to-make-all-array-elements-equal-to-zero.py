class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        for i, x in enumerate(nums): 
            if i >= k: nums[i] += nums[i-k]
            if i and nums[i-1] > nums[i]: return False 
        return all(nums[~i] == nums[-1] for i in range(k))