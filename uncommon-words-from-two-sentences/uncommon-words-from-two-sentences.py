import collections
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        token_1 = s1.split(' ')
        token_2 = s2.split(' ')
        
        tokens = token_1 + token_2
        count = {}
        for token in tokens:
            if token not in count:
                count[token] = 1
                
            else:
                count[token] += 1
        answer = []
        for token, token_count in count.items():
            if token_count == 1:
                answer.append(token)
                
        return answer
                
            
        
        
     
        