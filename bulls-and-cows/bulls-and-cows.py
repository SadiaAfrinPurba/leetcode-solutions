class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        
        bucket= [0] * 10
        
        for g, s in zip(guess, secret):
            if g == s:
                bulls += 1
            else:
                bucket[int(s)] += 1
                bucket[int(g)] -= 1
                
        cows = len(secret) - bulls - sum(x for x in bucket if x > 0)
        
        return f'{bulls}A{cows}B'
        