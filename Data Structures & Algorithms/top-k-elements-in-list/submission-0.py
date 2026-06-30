class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        freq_count = [[] for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            freq[nums[i]] += 1
        for n in freq.keys():
            freq_count[freq[n]].append(n)

        topKFreqLst = []
        last_idx = -1
        while len(topKFreqLst) < k:
            topKFreqLst.extend(freq_count[last_idx])
            last_idx -= 1

        return topKFreqLst[:k] 