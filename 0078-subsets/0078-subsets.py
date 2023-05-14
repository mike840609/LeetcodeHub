class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            tmp = [] 
            for l in res:
                tmp.append(l + [n])            
            res += tmp 
        return res