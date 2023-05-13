class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]] 
        
        for n in nums:
            tmp = [] 
            for l in res:
                for idx in range(len(l)+1):
                    tmp.append(l[:idx] + [n] + l[idx:])

            res = tmp 
        
        return res