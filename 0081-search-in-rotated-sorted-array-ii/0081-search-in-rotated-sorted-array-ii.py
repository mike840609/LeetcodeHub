class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l, r = 0, len(nums)-1        
        
        while l < r:
            m = (l+r) // 2 
            if nums[m] == target: 
                return True 
            
            # remove duplicate num
            while l < m and nums[l] == nums[m]:
                l += 1 
            
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
                    
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1 
                else:
                    r = m
                    
        return nums[l] == target