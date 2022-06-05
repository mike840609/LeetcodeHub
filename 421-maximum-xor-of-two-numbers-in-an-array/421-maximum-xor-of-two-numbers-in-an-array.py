class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie, ans = {}, 0
        length = max(nums).bit_length()
        
        for n in nums:
            # cur to record current num, opposite to find the max xor num
            cur = opposite = trie
            
            for c in f'{n:b}'.zfill(length):
                cur = cur.setdefault(c, {})
                opposite = opposite.get(str(1-int(c))) or opposite.get(c)
                
            cur['$'] = n
            ans = max(ans, opposite['$'] ^ n)
            
        return ans
                
                
                    