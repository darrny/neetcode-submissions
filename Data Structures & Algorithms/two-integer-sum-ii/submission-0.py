class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        start = 0
        end = n - 1

        while start < end:
            first = numbers[start]
            last = numbers[end]
            curr = first + last
            if curr > target:
                end -= 1
            elif curr < target:
                start += 1
            else:
                return [start + 1, end + 1]