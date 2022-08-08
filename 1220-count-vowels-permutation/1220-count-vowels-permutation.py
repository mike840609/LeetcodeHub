class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = defaultdict(int)
        dp['a'] = 1 
        dp['e'] = 1
        dp['i'] = 1
        dp['o'] = 1
        dp['u'] = 1
        
        for _ in range(n-1):
            tmp = defaultdict(int)
            
            tmp['e'] += dp['a']
            
            tmp['a'] += dp['e']
            tmp['i'] += dp['e']
            
            tmp['a'] += dp['i']
            tmp['e'] += dp['i']
            tmp['o'] += dp['i']
            tmp['u'] += dp['i']
            
            tmp['i'] += dp['o']
            tmp['u'] += dp['o']
            
            tmp['a'] += dp['u']      
            
            for k in tmp :
                tmp[k] = tmp[k] % (10**9 + 7)
            
            dp = tmp 
                            
        return sum(dp.values()) % (10**9 + 7)