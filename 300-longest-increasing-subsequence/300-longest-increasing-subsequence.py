class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [] 
        for n in nums :
            idx = bisect.bisect_left(res, n)
            res[idx:idx+1] = [n]
        
        return len(res)
                