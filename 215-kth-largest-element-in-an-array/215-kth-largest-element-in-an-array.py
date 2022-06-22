class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:            
            val = nums[r]
            i = l - 1
            
            for j in range(l, r):
                if val < nums[j]:
                    i += 1
                    nums[j], nums[i] = nums[i], nums[j]
            
            i += 1
            nums[r], nums[i] = nums[i], nums[r]
            
            if i == k-1:
                return nums[i]
            elif i > k-1:
                r = i - 1
            else:
                l = i + 1
                
        return -1