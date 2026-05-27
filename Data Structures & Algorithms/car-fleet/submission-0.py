class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeed = []
        for i in range(len(position)):
            heapq.heappush(positionSpeed, (position[i], speed[i]))

        stack = []
        while positionSpeed:
            currPosition, currSpeed = heapq.heappop(positionSpeed)
            time = float(target - currPosition) / float(currSpeed)
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)

        return len(stack)