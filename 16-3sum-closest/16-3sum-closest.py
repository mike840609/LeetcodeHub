class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        res = float('inf')
        diff = float('inf')
        
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            
            t = target - nums[i]
            while j < k :
                
                if nums[j] + nums[k] < t:
                    d = abs(nums[i]+nums[j] + nums[k] - target)
                    if d < diff:
                        res = nums[i]+nums[j] + nums[k]
                        diff = d
                    
                    j += 1
                elif nums[j] + nums[k] > t:
                    d = abs(nums[i]+nums[j] + nums[k] - target)
                    if d < diff:
                        res = nums[i]+nums[j] + nums[k]
                        diff = d
                    k -= 1
                else:
                    return target
        return res
                
            