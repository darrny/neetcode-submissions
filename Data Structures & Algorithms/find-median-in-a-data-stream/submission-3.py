class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, num)
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        
    def findMedian(self) -> float:
        if len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (float(self.min_heap[0]) - float(self.max_heap[0])) / 2
        