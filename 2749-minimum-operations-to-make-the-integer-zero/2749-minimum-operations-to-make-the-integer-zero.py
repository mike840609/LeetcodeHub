class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        
        # brute force: iterate operation k 
        # 問題轉換成假設: 
        # x = num1 - num2 * k 
        # 計算 x 是否能分解成 k 個 2^i
        
        # k ∈ [x.bit_count(), x]
        
        for k in range(1, 64):
            x = num1 - num2 * k 
            if x < k: return -1             
            if k >= x.bit_count(): return k
        