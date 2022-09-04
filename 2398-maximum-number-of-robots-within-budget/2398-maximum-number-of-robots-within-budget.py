class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
        def remove_stale(pq, j):
            while pq and pq[0][1] <= j :
                heappop(pq)
            return -pq[0][0] if pq else 0
    
        
        j, res, tmp, pq = -1, 0, 0, []

        for i in range(len(chargeTimes)):
            tmp += runningCosts[i]
            heappush(pq, [-chargeTimes[i], i])

            while remove_stale(pq, j) + (i- j) * tmp > budget:
                j += 1
                tmp -= runningCosts[j]

            res = max(res, i-j)
        
        return res

                