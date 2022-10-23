'''
Assume the final equal values are x
the total cost function y = f(x) is a convex function
on the range of [min(A), max(A)].

To find the minimum value of f(x),
we can binary search x by comparing f(mid) and f(mid + 1).

If f(mid) <= f(mid + 1),
the minimum f(x) is on the left of mid,
where x <= mid

If f(mid) >= f(mid + 1),
the minimum f(x) is on the right of mid + 1,
where x >= mid.

Repeatly doing this while left < right,
until we find the minimum value and return it.

This method is known as trinary search,
if we check f(mid1) and f(mid2).


https://leetcode.com/problems/minimum-cost-to-make-array-equal/discuss/2734162/C%2B%2BPython-Binary-Search

'''

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        def find(target):
            res = 0 
            for i, n in enumerate(nums):
                res += abs(n-target) * cost[i]                
            return res      
        
        l, r = min(nums), max(nums)
        res = find(l)                
        
        while l < r : 
            m = (l+r) //2
            y1, y2 = find(m), find(m+1)
            res = min(y1, y2)
            
            if y1 < y2:
                r = m
            else:
                l = m + 1
        
        return res
                
            