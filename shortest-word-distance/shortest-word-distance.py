class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        dis = float('inf')
        seen = {word1: wordsDict.index(word1), word2: wordsDict.index(word2)}
        
           
        for idx, word in enumerate(wordsDict):
            if word in seen:
                seen[word] = idx
                
                dis = min(dis, abs(seen[word1] - seen[word2]))
       
        return dis
        