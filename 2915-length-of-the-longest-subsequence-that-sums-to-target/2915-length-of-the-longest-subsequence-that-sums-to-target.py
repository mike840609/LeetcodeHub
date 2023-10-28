class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        cnt = Counter()
        cnt[target] = 0
        
        for n in nums:
            next_cnt = {}
            for k, v in cnt.items():
                if k >= n:
                    new_k = k-n                    
                    next_cnt[new_k] = max(cnt[new_k], v+1)
                        
            for k,v in next_cnt.items():        
                cnt[k] = v
            
        
        return cnt[0] if cnt[0] >=1 else -1
        
    