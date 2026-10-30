class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw_str = "".join(filter(str.isalnum,s.strip().lower()))
        for i in range(len(raw_str)):
            if raw_str[i] != raw_str[-i-1]:
                return False
        return True