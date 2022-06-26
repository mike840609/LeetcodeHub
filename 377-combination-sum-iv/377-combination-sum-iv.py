class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        cnt = {0:1}
        
        res = 0 
        while cnt:            
            tmp = defaultdict(int)
            flag = False 
            for k, v in cnt.items():
                for n in nums:
                    if k+n <= target:
                        tmp[k+n] += v
                        flag = True 

            cnt = tmp            
            res += cnt.get(target, 0)
            
        return res 
            
                
            
        
                    
            
            
                
        