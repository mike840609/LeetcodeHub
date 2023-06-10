class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        pos = sorted([x-d if y == "L" else x+d for x, y in zip(nums, s)])        
        
        ans = 0
        nums.sort()
        mod = 10 ** 9 + 7
        s = 0
        
        for i in range(len(pos)):
            ans += (pos[i] * i - s)
            ans %= mod
            s += pos[i]
            s %= mod
        
        return ans % mod
                
        
        