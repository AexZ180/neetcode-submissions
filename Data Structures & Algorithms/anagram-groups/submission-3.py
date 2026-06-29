class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}
        for i in range(len(strs)):
            sorted_word = ''.join(sorted(strs[i]))
            if sorted_word not in grouped_anagrams:
                grouped_anagrams[sorted_word] = []
            grouped_anagrams[sorted_word].append(strs[i])
        return list(grouped_anagrams.values())