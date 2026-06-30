class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        else:
            count = {}
            for char in s:
                count[char] = count.get(char, 0) + 1
            
            for char in t:
                if char not in count:
                    return False
                count[char] = count.get(char) -1
                if count[char] < 0:
                    return False

            return True


        
            