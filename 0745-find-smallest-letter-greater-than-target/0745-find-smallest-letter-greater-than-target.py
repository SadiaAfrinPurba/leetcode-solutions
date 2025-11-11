class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) - 1

        if target < letters[start] or target >= letters[end]:
            return letters[start]
    
        while start <= end:
            middle = start + (end - start) // 2
            if letters[middle] <= target:
                start = middle + 1
            else:
                end = middle - 1
           
        return letters[start]
            
        