class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:                 
        nums = set(nums)
        cnt = Counter()
        for n in nums:
            cnt[bin(n).count('1')] += 1
            
        
        return sum([v1 * v2 for k1, v1  in cnt.items() for k2, v2 in cnt.items() if k1+k2 >= k])