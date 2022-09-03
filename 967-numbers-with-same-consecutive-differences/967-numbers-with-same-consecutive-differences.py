class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        dp = defaultdict(set)
        
        for i in range(10):
            dp[i].add(str(i))
            
        for j in range(n-1):
            tmp = defaultdict(set)
            for i in range((j==n-2), 10):
                for l in dp[i+k] | dp[i-k]:
                    tmp[i].add(str(i)+l)                
            dp = tmp
                
        return [x for l in dp.values() for x in l ]
            
            