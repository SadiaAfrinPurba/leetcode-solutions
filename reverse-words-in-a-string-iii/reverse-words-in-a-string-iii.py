class Solution:
        def reverseWords(self, s: str) -> str:
            still = 0
            moving = 0
            s_list = list(s)

            for idx, ch in enumerate(list(s)):
                if ch.isspace() or idx == len(s_list) - 1:
                    space_at = idx

                    if idx == len(s_list) - 1:
                        moving = idx
                        
                    while still <= moving:
                        s_list[still], s_list[moving] = s_list[moving], s_list[still]
                        still += 1
                        moving -= 1

                    moving, still = space_at+1, space_at+1
                else:
                    moving = idx

            return "".join(s_list)
            
        