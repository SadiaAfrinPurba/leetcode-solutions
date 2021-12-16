class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        
        self.reverse(array=nums, start=0, end=n-1)
        self.reverse(array=nums, start=0, end=k-1)
        self.reverse(array=nums, start=k, end=n-1)
        
        
    def reverse(self, array: List[int], start: int, end: int) -> None:
        while start < end:
            array[start], array[end] = array[end], array[start]
            
            start += 1
            end -= 1
        
    

