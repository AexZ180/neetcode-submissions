class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = defaultdict(int)
        t_seen = defaultdict(int)

        for char in s:
            s_seen[char] += 1
        for char in t:
            t_seen[char] += 1

        if s_seen != t_seen:
            return False
        return True

