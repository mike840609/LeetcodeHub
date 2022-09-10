class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        
        res = 0
        flag = True            
        
        for w in words:
            x, y = w[0], w[1]            
            if x == y:
                if cnt[w] % 2 == 1 and flag:
                    flag = False
                    cnt[w] -= 1
                    res += 2
            
                if cnt[w]//2 > 0:
                    num, remain  = divmod(cnt[w], 2)
                    res += (num * 4)
                    cnt[w] = remain
            else:
                key = y+x
                
                if key in cnt:
                    num = min(cnt[key], cnt[w])
                    cnt[key] -= num
                    cnt[w] -= num
                    res += num*4
                            
        return res
                    
            