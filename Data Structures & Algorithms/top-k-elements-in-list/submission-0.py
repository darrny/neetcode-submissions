class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            bucket[freq].append(num)
        
        res = []

        for i in range(len(nums), 0, -1):
            for number in bucket[i]:
                res.append(number)
                if len(res) == k:
                    return res
                
        return res