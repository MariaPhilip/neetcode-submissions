class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map=defaultdict(list)
        freq=[0]*26

        def check_freq(word):
            freq=[0]*26
            for char in word:
                freq[ord(char)-ord('a')]+=1
            return tuple(freq)

        for item in strs:
            key=check_freq(item)
            hash_map[key].append(item)

        return list(hash_map.values())


        



