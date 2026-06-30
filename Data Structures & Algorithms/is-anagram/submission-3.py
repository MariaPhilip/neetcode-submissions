class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_len = len(s)
        # t_len = len(t)
        # if s_len != t_len:
        #     return False
        # else:
        #     count = {}
        #     for char in s:
        #         count[char] = count.get(char, 0) + 1
            
        #     for char in t:
        #         if char not in count:
        #             return False
        #         count[char] = count.get(char) -1
        #         if count[char] < 0:
        #             return False

        #     return True

        s_hashmap = {}
        t_hashmap = {}

        for char in s:
            if char in s_hashmap:
                s_hashmap[char] += 1
            else:
                s_hashmap[char] = 1

        for char in t:
            if char in t_hashmap:
                t_hashmap[char] += 1
            else:
                t_hashmap[char] = 1

        if len(s_hashmap) != len(t_hashmap):
            return False
        else:
            for char , count in s_hashmap.items():
                if  char  not in t_hashmap:
                    return False

                if s_hashmap[char]!=t_hashmap[char]:
                    return False
            
            return True



        
            