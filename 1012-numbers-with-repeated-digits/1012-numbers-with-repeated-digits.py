"""
The corner case is too hard to manage...

count res as N - total number without duplicated digits.
turns into a math and permutation problem.

select m out of n
P(m, n): n! / (n-m)!

Algorithm:

lets say N has k digits.
1) count number less than k digits
lets say number with i digits
first digit 1 ~ 9, following option is 0 ~ 9 without first digit
count = 9 * P(i-1,9)

2) count number has k digits. 
Calculate digits with same prefix. 
Prefix cannot has duplicate digits.
for case like 77xxx, we should stop the calculation.
"""

class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        L = list(map(int, str(N+1)))
        n = len(L)
        s = set()
        
        # count number less than k digits
        res = sum(9 * perm(9, i) for i in range(n-1))                
        
        # count number has k digits
        for i, x in enumerate(L):
            for y in range(i==0, x):
                if y not in s :
                    res += perm(9 - i, n - i -1)
            
            if x in s : break 
            s.add(x)

        return N-res
        