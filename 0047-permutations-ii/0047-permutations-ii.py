class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]] 
        
        for n in nums:    
            tmp = []
            
            for l in res :                
                for i in range(len(l) + 1):
                    tmp += [l[:i]+ [n] + l[i:]]
                    if i<len(l) and l[i]==n:                                 
                        break #handles duplication
            res = tmp 
            # print(res)
            
        return res 