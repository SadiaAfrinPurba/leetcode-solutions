class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = []
        w_f = [self.f(word) for word in words]
        
        for query in queries:
            q_f = self.f(query)
            count = 0
            for i in w_f:
                if q_f < i:
                    count += 1
            ans.append(count)
            
        return ans

    def f(self, string: str):

        counter = Counter(string)
        return counter[min(string)]
            
        
        
        
        
