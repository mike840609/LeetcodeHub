class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(tmp, l, idx):
            nonlocal res
            if tmp == target:
                res.append(l[::])                
                return 
            
            if tmp > target:
                return 
            
            if tmp < target:
                for i in range(idx, len(candidates)):
                    n = candidates[i]
                    dfs(tmp+n, l + [n], i)
            
        
        dfs(0, [], 0)
        return res
        
                