class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_mapper = {}
        
        start = 0
        max_number_of_fruits = 0
        for end, fruit in enumerate(fruits):
            if len(fruit_mapper) < 2 and fruit not in fruit_mapper:
                fruit_mapper[fruit] = True
                window_size = (end - start) + 1
                max_number_of_fruits = max(max_number_of_fruits, window_size)
            
            elif fruit in fruit_mapper:
                window_size = (end - start) + 1
                max_number_of_fruits = max(max_number_of_fruits, window_size)
            else:
                fruit_mapper = {}
                fruit_mapper[fruits[end - 1]] = True
                fruit_mapper[fruit] = True
                start = end - 1
                
                while fruits[start] == fruits[start - 1]:
                    start -= 1
                    
                window_size = (end - start) + 1
                max_number_of_fruits = max(max_number_of_fruits, window_size)
                
        return max_number_of_fruits
                    
                
                
                
                