class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        
        def dfs(target, can, tmp):
            if target == 0 :
                res.append(tmp[::])
            elif target < 0 :
                return 
            
            for i in range(len(can)):
                dfs(target - can[i], can[i:], tmp + [can[i]])
        
        dfs(target, candidates, [])
        
        return res
            
        