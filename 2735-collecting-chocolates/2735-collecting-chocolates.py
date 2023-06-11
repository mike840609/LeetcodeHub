class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        res = [i*x for i in range(len(nums))]
        
        for i in range(n):
            cur = nums[i]
            for k in range(n):
                cur = min(cur, nums[i-k])
                
                res[k] += cur
        
        return min(res)