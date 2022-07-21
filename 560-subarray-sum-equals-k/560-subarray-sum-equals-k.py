class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = list(accumulate([0] + nums))
        
        d = defaultdict(int)
        res = 0 
        for accu in l:
            res += d[accu-k]
            d[accu] += 1
                
        return res 
                
            
            
                    