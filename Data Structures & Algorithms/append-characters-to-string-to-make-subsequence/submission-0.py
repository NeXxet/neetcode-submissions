class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # handle case where t is already subsequence of s
        # if loop ends when t_pointer == len(t) 

        s_ptr = 0
        t_ptr = 0
        s_sub_length = 0

        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_sub_length += 1
                s_ptr += 1
                t_ptr += 1
            else:
                s_ptr += 1

        if t_ptr == len(t):
            return 0
        
        return len(t) - s_sub_length
