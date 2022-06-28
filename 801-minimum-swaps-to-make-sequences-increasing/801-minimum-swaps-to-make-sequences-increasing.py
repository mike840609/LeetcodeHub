'''
swap[n] means the minimum swaps to make the A[i] and B[i] sequences increasing for 0 <= i <= n,
in condition that we swap A[n] and B[n]
not_swap[n] is the same with A[n] and B[n] not swapped.

@Acker help explain:

A[i - 1] < A[i] && B[i - 1] < B[i].
In this case, if we want to keep A and B increasing before the index i, can only have two choices.
-> 1.1 don't swap at (i-1) and don't swap at i, we can get not_swap[i] = not_swap[i-1]
-> 1.2 swap at (i-1) and swap at i, we can get swap[i] = swap[i-1]+1
if swap at (i-1) and do not swap at i, we can not guarantee A and B increasing.

A[i-1] < B[i] && B[i-1] < A[i]
In this case, if we want to keep A and B increasing before the index i, can only have two choices.
-> 2.1 swap at (i-1) and do not swap at i, we can get notswap[i] = Math.min(swap[i-1], notswap[i] )
-> 2.2 do not swap at (i-1) and swap at i, we can get swap[i]=Math.min(notswap[i-1]+1, swap[i])

'''
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        
        not_swap, swap = [N] * N, [N] * N
        not_swap[0] = 0 
        swap[0] = 1
        
        for i in range(1, N):
            if A[i-1] < A[i] and B[i-1] < B[i]:
                swap[i] = swap[i-1] + 1
                not_swap[i] = not_swap[i-1] 
            
            if A[i-1] < B[i] and B[i-1] < A[i]:
                swap[i] = min(swap[i], not_swap[i - 1] + 1)
                not_swap[i] = min(not_swap[i], swap[i - 1])
        
        return min(swap[-1], not_swap[-1])