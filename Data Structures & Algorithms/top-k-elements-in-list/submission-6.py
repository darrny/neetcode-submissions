class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_heap = [] # minheap, so need to pass in the negative value of the frequency
        counts = Counter(nums)
        res = []

        for key, count in counts.items():
            heapq.heappush(frequency_heap, (count, key))
            
            if len(frequency_heap) > k:
                heapq.heappop(frequency_heap)

        for count, key in frequency_heap:
            res.append(key)
        
        return res