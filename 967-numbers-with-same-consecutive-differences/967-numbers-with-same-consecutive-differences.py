class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        num_list = list(str(x) for x in range(10))
        def dfs(i):
            
            if i == n:
                return num_list
            
            post = dfs(i+1)
            
            tmp = []            
            for j in num_list:
                for s in post:
                    if abs(ord(j)-ord(s[0])) == k:
                        tmp.append(j + s)            
            return tmp 
        
        res = dfs(1)
        
        return [''.join(x) for x in res if x[0] != '0']
                