class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        num_list = list(str(x) for x in range(10))
        dp = defaultdict(set)
        for i in range(10):
            dp[i].add(str(i))
            
        for _ in range(n-1):
            tmp = defaultdict(set)
            for i in range(10):
                for l in dp[i+k]:
                    tmp[i].add(str(i)+l)
                for l in dp[i-k]:
                    tmp[i].add(str(i)+l)            
            dp = tmp
                
        return [x for l in dp.values() for x in l if x[0] != '0']
            
            