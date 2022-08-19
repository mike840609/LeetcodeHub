class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left, end = Counter(nums), Counter()
        
        for n in nums:
            if left[n] <= 0 :
                continue 
            left[n] -= 1
            
            if end[n-1] :
                end[n-1] -= 1
                end[n] += 1
            
            elif left[n+1] and left[n+2]:
                left[n+1] -= 1
                left[n+2] -= 1
                end[n+2] += 1
            else:
                return False 
        return True
            
                