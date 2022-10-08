class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        res = float('inf')
        diff = float('inf')
        
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
                        
            while j < k :
                d = ((nums[i]+nums[j] + nums[k]) - target)
                if d < 0:
                    if abs(d) < diff:
                        res = d + target
                        diff = abs(d)
                    j += 1
                elif d > 0:                    
                    if abs(d) < diff:
                        res = d + target
                        diff = abs(d)
                    k -= 1
                else:
                    return target
        return res
                
            