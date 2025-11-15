class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        next_zeros = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == "0":
                next_zeros[i + 1] = i
            else:
                next_zeros[i + 1] = next_zeros[i]

        res = 0
        for left in range(1, n + 1):
            cnt0 = 1 if s[left - 1] == "0" else 0
            right = left
            while right > 0 and cnt0 * cnt0 <= n:
                cnt1 = (left - next_zeros[right]) - cnt0
                if cnt0 * cnt0 <= cnt1:
                    res += min(right - next_zeros[right], cnt1 - cnt0 * cnt0 + 1)
                right = next_zeros[right]
                cnt0 += 1
        return res