class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for idx in range(1, n+1):
            if (idx % 3 == 0) and (idx % 5 == 0):
                result.append("FizzBuzz")
            elif idx % 3 == 0:
                result.append("Fizz")
            elif idx % 5 == 0:
                result.append("Buzz")
            else:
                 result.append(str(idx))
        return result
                
                
                
                
                
        