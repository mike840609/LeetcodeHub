class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        
        def dfs(idx, path, target):
            if target < 0:
                return 
            
            if target == 0:
                res.append(path)
                return 
            
            for i in range(idx, len(candidates)):
                val = candidates[i]
                dfs(i, path + [val], target-val)

        dfs(0, [], target)
        return res
                
            
             