class Solution:
    def minOperations(self, nums: List[int]) -> int:

        def gcd(a, b):
            while a and b:
                a = a % b
                b, a = a, b

            return max(a, b) # to handle gcd(0, some_num)

        one_count = 0
        curr_gcd = 0
        
        for n in nums:
            if n == 1:
                one_count += 1
            curr_gcd = gcd(curr_gcd, n)

        if one_count > 0:
            return len(nums) - one_count
        
        if curr_gcd != 1:
            return -1
        
        min_sub_arr_len = float("inf")

        for left in range(len(nums)):
            curr_gcd = 0
            for right in range(left, len(nums)):
                if right - left + 1 > min_sub_arr_len:
                    break
                
                curr_gcd = gcd(curr_gcd, nums[right])
                
                if curr_gcd == 1:
                    min_sub_arr_len = right - left + 1
                    break
        

        ops = min_sub_arr_len - 1
        return ops + len(nums) - 1
        