class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        def dfs(i):
            
            if i == n:
                return list([x] for x in range(10))
            
            l = dfs(i+1)
            
            tmp = []
            
            for j in range(10):
                for sub_l in l:
                    if abs(j-sub_l[0]) == k:
                        tmp.append([j] + sub_l)
            
            return tmp 
        
        res = dfs(1)
        
        return [''.join(map(str, x)) for x in res if x[0] != 0]
                