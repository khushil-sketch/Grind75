class Solution:

    # Solution 1
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        for char in s:
            if char not in map_s:
                map_s[char] = 1
            else:
                map_s[char] += 1

        map_t = {}
        for char in t:
            if char not in map_t:
                map_t[char] = 1
            else:
                map_t[char] += 1

        if map_t == map_s:
            return True

        else:
            return False

        # Solution 2

        # if the length of the anagrams don't match, they really ain't anagrams
        if len(s) != len(t):
            return False

        map_s, map_t = {}, {}

        for i in range(len(s)):
            map_s[s[i]] = 1 + map_s.get(s[i], 0)
            map_t[t[i]] = 1 + map_t.get(t[i], 0)

        if map_s != map_t:
            return False

        return True
