from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = [] 
        l = SortedList()
        
        for i, v in enumerate(nums):
            l.add(v)
            
            if len(l) > k: l.remove(nums[i-k])
            
            if i >= k-1: res.append(min(0, l[x-1]))
                        
        
        return res
            
            