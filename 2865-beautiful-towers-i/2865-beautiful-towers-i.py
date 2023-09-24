class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        res = 0 
        for i in range(len(maxHeights)):            
            l_q, r_q = deque([]), deque([])            
            
            for j in range(i-1, -1, -1):
                n = maxHeights[j]
                max_ = n if not l_q else min(n, l_q[0])                
                l_q.appendleft(max_)

            r_q.append(maxHeights[i])
            
            for j in range(i+1, len(maxHeights)):
                n = maxHeights[j]
                min_ = n if not r_q else min(n, r_q[-1])
                r_q.append(min_)

            # print(l_q)
            # print(r_q)
            # print('-----')
            res = max(res, sum(l_q) + sum(r_q))
        return res
                        
                    
            
            
                
        