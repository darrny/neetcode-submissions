class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_counts = sorted(counts, key=lambda x: counts[x], reverse = True)
        return sorted_counts[:k]