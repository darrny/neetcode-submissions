class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [0] * len(stones)
        for i in range(len(stones)):
            maxheap[i] = stones[i] * -1
        heapq.heapify(maxheap)
        print(maxheap)

        while len(maxheap) > 1:
            stoneOne = heapq.heappop(maxheap)
            stoneTwo = heapq.heappop(maxheap)
            if stoneOne == stoneTwo:
                continue
            heapq.heappush(maxheap, - abs(stoneOne - stoneTwo))
        
        if maxheap:
            return -1 * maxheap[0]
        return 0
